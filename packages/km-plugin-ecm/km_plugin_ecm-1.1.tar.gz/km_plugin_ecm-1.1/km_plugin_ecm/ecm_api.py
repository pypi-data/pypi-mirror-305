import datetime
import hashlib
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from random import randint
from typing import Dict, Tuple, Set, Iterable

import requests
from apscheduler.triggers.interval import IntervalTrigger
from elasticsearch_dsl import Q
from elasticsearch_dsl.query import Query
from km_sdk.api_provider import ApiProvider, FileDto, BaseType, PermissionDto, UserDto
from km_sdk.utils.cache_utils import CacheUtils
from km_sdk.utils.lock_utils import LockUtils
from km_sdk.utils.log_utils import LogUtils
from km_sdk.utils.notification_utils import SystemNotificationUtils, FileChangeType
from km_sdk.utils.scheduler_utils import SchedulerUtils
from km_sdk.utils.setting_utils import SettingUtils

sync_logger = LogUtils.get_logger()


class PermissionType(Enum):
    UserGroup = 8
    Department = 2
    Position = 4
    User = 1


class CacheDto:
    time: float
    files: [FileDto]

    def __init__(self, d):
        self.__dict__ = d


class FilePermission(Enum):
    NOTIN = 1
    IN = 2


class FolderPermission(Enum):
    NOTIN = 7
    IN = 8


class PermissionChanged(Enum):
    PERMISSION = [311, 312]


class FileChanged(Enum):
    FILE_CHANGE = [305, 309, 318, 332, 346, 347, 377, 378]


class FileUpdate(Enum):
    FILE_UPDATE = [301, 302, 304, 325, 372]


class FileDeleted(Enum):
    FILE_DELETE = [303, 316, 317]


@dataclass
class LastRecordsDto(BaseType):
    OptType: int
    OptTime: str
    UserId: str
    OptSourceId: str


def decode_request(func):
    """
    返回json结构
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            result = func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            sync_logger.exception("同步文件出错")
            return e, None

        result_json = result.json()
        if "errorCode" in result_json and "errorMsg" in result_json and result_json['errorCode']:
            raise PermissionError("PermissionError", result_json['errorMsg'])
        if "data" in result_json:
            return None, result_json['data']
        return None, result_json

    return wrapper


def get_current_end_time_str():
    now = datetime.datetime.now()
    end_time = now.replace(hour=23, minute=59, second=59, microsecond=0)
    return end_time.strftime('%Y-%m-%d %H:%M:%S')


def map_opt_type(opt_type) -> FileChangeType | None:
    if opt_type in PermissionChanged.PERMISSION.value:
        return FileChangeType.FILE_PERMISSION
    elif opt_type in FileChanged.FILE_CHANGE.value:
        return FileChangeType.FILE_EDIT
    elif opt_type in FileUpdate.FILE_UPDATE.value:
        return FileChangeType.FILE_EDIT
    elif opt_type in FileDeleted.FILE_DELETE.value:
        return FileChangeType.FILE_DELETE
    else:
        return None


class EcmApi(ApiProvider):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = kwargs.get('base_url')
        self.token = kwargs.get('token')
        self.verify = kwargs.get("verify")
        self.headers = {
            'accept': 'application/json',
        }
        self.timeout = kwargs.get("timeout", 30)
        md5 = hashlib.md5()
        md5.update(self.related_sync_system.encode("utf-8") if self.get_related_sync_system() else self.base_url.encode(
            "utf-8"))
        self.redis_key = f"{md5.hexdigest()}.lastPage"

    def test_connection(self):
        """
        不抛异常就认为是测试成功
        :return:
        """
        for _ in self.get_all_file():
            break

    def build_filter(self, user_id: str, related_sync_system: str, bqry: Query) -> Query:
        user_info = self.get_user(user_id)
        inesp = {}
        notinesp = {}
        for x in user_info.permissions:
            inesp["permission.IN" + "." + x.type] = x.value
            notinesp["permission.NOTIN" + "." + x.type] = x.value

        def filter_q(k, v):
            return Q("bool", filter=[
                Q("term", related_sync_system=related_sync_system),
                Q({"terms": {k: v}})
            ])

        return Q("bool",
                 should=[
                     Q("bool",
                       should=[filter_q(k, v) for k, v in inesp.items()],
                       must_not=[
                           Q("bool",
                             filter=[
                                 Q("term", related_sync_system=related_sync_system),
                                 Q({"terms": {"permission.NOTIN.User": [user_info.id]}})
                             ]
                             ),
                           *[filter_q(k, v) for k, v in notinesp.items()]
                       ]
                       ),
                     Q("bool",
                       filter=[
                           Q("term", related_sync_system=related_sync_system),
                           Q({"terms": {"permission.IN.User": [user_info.id]}})
                       ]
                       )
                 ]
                 )

    def fetch_file(self, **kwargs) -> Iterable[FileDto]:
        return self.get_all_file()

    def get_files(self, page_size=20, current=1) -> [FileDto]:
        pass

    def get_file(self, file_id: str) -> FileDto:
        err, response = self.get_file_by_id(file_id)
        if err:
            raise err
        _, response1 = self.get_file_md5(file_id)
        f = FileDto({
            "id": response.get('FileId', ''),
            "md5": response1,
            "name": response.get('FileName', ''),
            "size": response.get('FileSize', '')
        })
        return f

    def list_file_permission(self, file_id: str) -> [PermissionDto]:
        err, data = self.file_permission(file_id)
        if err:
            raise err
        if not data:
            return []
        datas = data.get('FilePermissionList', [])

        permission_dict: Dict[Tuple[str, str], PermissionDto] = {}

        for item in datas:
            perm_cate_id = item['permCateId']
            member_value = item['memberType']
            if member_value not in [pt.value for pt in PermissionType]:
                continue  # 跳过未知类型

            permission_type = PermissionType(member_value).name
            if 1 <= perm_cate_id <= 12:
                if perm_cate_id <= 6:
                    if perm_cate_id == 1:
                        permission_extend = FilePermission.NOTIN.name
                    else:
                        permission_extend = FilePermission.IN.name
                else:
                    if perm_cate_id == 7:
                        permission_extend = FolderPermission.NOTIN.name
                    else:
                        permission_extend = FolderPermission.IN.name
                key = (permission_type, permission_extend)
                if permission_type == 'Department':
                    err, department_info = self.get_department_information([item['memberId']])
                    if err:
                        return err

                    department_id = department_info.get('ID', '')
                    err, sub_department = self.get_sub_department(department_id)
                    if err:
                        return err
                    member_ids = [item['memberId']] + (
                        [sub_dept['IdentityId'] for sub_dept in sub_department] if sub_department else [])
                    if item['parentId'] != 0:
                        member_ids.append(item['parentId'])
                    if key not in permission_dict:
                        permission_dict[key] = PermissionDto(
                            type=permission_type,
                            value=member_ids,
                            extend=permission_extend
                        )
                    else:
                        permission_dict[key].value.extend(member_ids)

                elif permission_type == 'Position':
                    err, position_info = self.get_position_information([item['memberId']])
                    if err:
                        return err

                    position_id = position_info.get('ID', '')
                    errs, sub_position = self.get_sub_position(position_id)
                    if err:
                        return err
                    member_ids = [item['memberId']] + (
                        [sub_poi['IdentityId'] for sub_poi in sub_position] if sub_position else [])
                    if item['parentId'] != 0:
                        member_ids.append(item['parentId'])
                    if key not in permission_dict:
                        permission_dict[key] = PermissionDto(
                            type=permission_type,
                            value=member_ids,
                            extend=permission_extend
                        )
                    else:
                        permission_dict[key].value.extend(member_ids)

                else:
                    if key not in permission_dict:
                        permission_dict[key] = PermissionDto(
                            type=permission_type,
                            value=[item['memberId']],
                            extend=permission_extend
                        )
                    else:
                        permission_dict[key].value.append(item['memberId'])
            else:
                # 如果 perm_cate_id 不在 1 到 12 之间，跳过当前项
                continue
        permission_dtos = list(permission_dict.values())
        return permission_dtos

    def list_user_file_permission(self, user_id: str, file_ids: [str]) -> [str]:
        file_ids = list(set(file_ids))
        results = []
        for file_id in file_ids:
            err, result = self.get_list_file_permission(user_id, file_id, 1)
            if err:
                raise err
            if result:
                results.append(file_id)

        return results

    def get_user(self, user_id: str) -> UserDto:
        err, response = self.get_user_by_id(user_id)
        if err:
            raise err

            # 用户组
        if response:
            errs, response1 = self.get_user_group_by_id(response.get('ID', ''))
            if errs:
                raise errs
            #  职位-部门
            errs, response2 = self.get_user_position_by_id(response.get('ID', ''))
            if errs:
                raise errs

            # 初始化数组
            permissions = []
            department_ids: Set[int] = set()

            def add_or_merge_permission(types: str, value: str):
                for permission in permissions:
                    if permission.type == types:
                        permission.value.append(value)
                        return
                # 类型不同创建新的
                permissions.append(PermissionDto(type=types, value=[value], extend=None))

            # 添加用户组
            if response1:
                for item in response1:
                    add_or_merge_permission('UserGroup', item['IdentityId'])
            # 添加职位 部门
            if response2:
                for item in response2:
                    add_or_merge_permission('Position', item['IdentityId'])
                    if 'DepartmentId' in item and item['DepartmentId'] != 'null':
                        err, sub_departments = self.get_sub_department(item['DepartmentId'])
                        if err:
                            return err

                        if sub_departments:
                            for sub_dept in sub_departments:
                                if sub_dept['IdentityId'] not in department_ids:
                                    department_ids.add(sub_dept['IdentityId'])
                                    add_or_merge_permission('Department', sub_dept['IdentityId'])
                        if item['DepartmentIdentityId'] and item['DepartmentIdentityId'] not in department_ids:
                            department_ids.add(item['DepartmentIdentityId'])
                            add_or_merge_permission('Department', item['DepartmentIdentityId'])
            # 添加用户
            add_or_merge_permission('User', response.get('IdentityId', ''))
            # 返回用户信息
            user_dto = UserDto(
                name=response.get('Name', ''),
                id=response.get('IdentityId', ''),
                permissions=permissions
            )
            return user_dto

        else:
            raise Exception(f"Failed to fetch user info")

    @LockUtils.lock()
    def file_log_listener(self, module: str = 'LogOperationManager', fun: str = 'LoadLogOperationByCondition',
                          **kwargs):
        """
        监听文件日志事件

        参数:
        - module (str): 日志模块，默认为 'LogOperationManager'
        - fun (str): 日志函数，默认为 'LoadLogOperationByCondition'

        返回:
        - err (str): 错误信息
        - result (list): 结果数据
        """
        # 从 Redis 获取页码数据
        sync_logger.info("start log task!")
        page_num = CacheUtils.get(self.redis_key)
        if not page_num:
            page_num = 0
        else:
            page_num = int(page_num)  # 确保将其转换为整数

        page_size = 50
        optTimeStartStr = '2000-01-01 00:00:00'
        optTimeEndStr = get_current_end_time_str()
        # 调用文件日志接口获取总页数
        try:
            result = self.file_logger(module, fun, 1, page_size, optTimeStartStr, optTimeEndStr)
            response = result.json()
            # 计算总页数
            total_pages = response.get('pageCount', 0)
        except Exception as e:
            return

        pages_to_sync = max(1, total_pages - page_num)
        # 从第最后一页开始同步，直到同步完本次需要同步的页数
        for current_page in range(pages_to_sync, 0, -1):
            # 调用文件日志接口
            result = self.file_logger(module, fun, current_page, page_size, optTimeStartStr, optTimeEndStr)
            response = result.json()
            if "errorCode" in response and "errorMsg" in response and response['errorMsg']:
                raise PermissionError(response.get('errorMsg'))
            permission_codes = response.get('logOpteration', [])

            # 翻转列表，以便从旧到新
            permission_codes = permission_codes[::-1]
            for x in permission_codes:
                mapped_opt_type = map_opt_type(x['OptType'])
                if mapped_opt_type is None:
                    continue
                SystemNotificationUtils.file_change(self, mapped_opt_type, x['OptSourceId'])
            # 更新 Redis 中的页码值
            CacheUtils.set(self.redis_key, str(pages_to_sync - current_page + page_num + 1))
        sync_logger.info("end log task!")

    @decode_request
    def file_permission(self, file_id: str):
        params = {
            'token': self.token,
            'fileId': file_id,
        }

        response = requests.get(
            f'{self.base_url}/api/services/FilePermission/GetFilePermission',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

        return response

    @decode_request
    def get_child_list_by_folder_id(self, folder_id, page_number=1, page_size=10):
        params = {
            'token': self.token,
            'folderId': folder_id,
            'pageNumber': page_number,
            'pageSize': page_size,
            'sortField': 'basic:name',
            'sortDesc': 'false',
        }
        return requests.get(f'{self.base_url}/api/services/Doc/GetChildListByFolderId', params=params,
                            headers=self.headers, verify=self.verify, timeout=self.timeout)

    @decode_request
    def get_download_file_hash(self, file_id, r):
        params = {
            'fileIds': file_id,
            'r': r,
            'isIe': 'false',
            'token': self.token,
        }
        return requests.get(
            f'{self.base_url}/downLoad/DownLoadCheck',
            params=params,
            headers=self.headers,
            verify=self.verify,
            timeout=self.timeout
        )

    def download_file(self, file_id, region_hash, r):
        params = {
            "fileIds": file_id,
            "regionHash": region_hash,
            "r": r,
            'token': self.token
        }
        return requests.get(f'{self.base_url}/downLoad/index', params=params, verify=self.verify, timeout=self.timeout)

    def download(self, file_id):
        """
        下载文件。

        通过文件ID下载指定的文件。此方法首先获取文件的下载哈希值，
        如果出错则抛出异常，之后使用得到的RegionHash进行实际的文件下载。

        参数:
        file_id (str): 要下载的文件的唯一标识符。

        返回:
        bytes: 下载的文件流内容。

        抛出:
        Exception: 如果获取下载文件哈希值过程中出现错误。
        AssertionError: 如果获取到的下载文件信息中不包含必需的RegionHash。
        """
        # 生成一个随机数，用于防止缓存
        r = randint(1, 10000)

        # 尝试获取文件的下载哈希值
        err, result = self.get_download_file_hash(file_id, r)

        # 如果遇到错误，则抛出异常
        if err:
            raise err

        # 确保返回的结果中包含必要的RegionHash信息
        assert 'RegionHash' in result, "获取下载文件信息失败"

        # 执行下载操作，并返回下载的文件内容
        response = self.download_file(file_id, result["RegionHash"], r)
        return response.content

    def get_all_file(self, folder_id=1, page_size=50) -> Iterable[FileDto]:
        """
        递归获取指定文件夹ID下的所有文件。

        参数:
            folder_id (int): 文件夹的ID，默认为1。
            page_size (int): 每页获取的文件数量，默认为50。

        返回:
            list[FileDto]: 包含所有文件的列表，每个文件用FileDto对象表示。
        """
        # 初始化文件列表
        # 初始化页码
        page_number = 1
        # 循环获取文件列表，直到没有更多文件为止
        while True:
            # 尝试获取指定文件夹ID的子项列表
            err, result = self.get_child_list_by_folder_id(folder_id, page_number, page_size)
            if err:
                sync_logger.exception("同步任务时网络错误")
                break
            # 计算当前页的文件夹和文件总数
            count = len(result['FoldersInfo']) + len(result['FilesInfo'])
            # 如果没有更多项，则退出循环
            if count <= 0:
                break
            # 遍历并添加文件到文件列表
            for x in result['FilesInfo']:
                _, data = self.get_file_md5(x["FileId"])
                # 创建FileDto对象并添加到临时列表
                yield FileDto({"id": x["FileId"], "name": x['FileName'], "size": x['FileCurSize'], "md5": data})
            # 遍历文件夹，递归获取每个文件夹下的所有文件
            for x in result['FoldersInfo']:
                # 递归调用get_all_file，将子文件夹中的所有文件添加到临时列表
                for file in self.get_all_file(x["FolderId"], page_size=page_size):
                    yield file
                # pass
            # 检查是否已获取所有文件
            if page_number * page_size >= result['Settings']['TotalCount']:
                break
            # 增加页码，准备获取下一页的文件列表
            page_number = page_number + 1

    @decode_request
    def get_file_md5(self, file_id: str):
        params = {
            'token': self.token,
            'fileId': file_id
        }
        return requests.get(
            f'{self.base_url}/api/services/File/GetFileMd5ByFileId',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_list_file_permission(self, user_id, file_id, perm_value):
        params = {
            'token': self.token,
            'userId': user_id,
            'fileId': file_id,
            'permValue': perm_value
        }
        return requests.get(
            f'{self.base_url}/api/services/FilePermission/IsFileHasPermission',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_file_by_id(self, file_id):
        params = {
            'token': self.token,
            # 'token': '0034c942be7027b04ef09392a653ba65982d',
            'fileId': file_id
        }

        return requests.get(
            f'{self.base_url}/api/services/File/GetFileInfoById',
            # f'http://222.128.108.161:131/api/services/File/GetFileInfoById',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_user_by_id(self, user_id):
        params = {
            'token': self.token,
            'userId': user_id,
        }

        return requests.get(
            f'{self.base_url}/api/services/OrgUser/GetUserInfoByUserId',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_user_group_by_id(self, user_id):
        params = {
            'token': self.token,
            'userId': user_id,
        }
        return requests.get(
            f'{self.base_url}/api/services/OrgUserGroup/GetGroupListOfUserByUserId',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_user_position_by_id(self, user_id):
        params = {
            'token': self.token,
            'userId': user_id,
        }
        return requests.get(
            f'{self.base_url}/api/services/OrgPosition/GetChildPositionListByUserId',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_department_information(self, identify_id):
        params = {
            'token': self.token,
            'identityId': identify_id
        }

        return requests.get(
            f'{self.base_url}/api/services/OrgDepartment/GetDepartmentInfoByIdentityId',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_sub_department(self, department_id):
        params = {
            'token': self.token,
            'departmentId': department_id
        }
        return requests.get(
            f'{self.base_url}/api/services/OrgDepartment/GetChildDepartmentList',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_position_information(self, identity_id):
        param = {
            'token': self.token,
            'identityId': identity_id
        }
        return requests.get(
            f'{self.base_url}/api/services/OrgPosition/GetPositionInfoByIdentityId',
            params=param,
            headers=self.headers,
            timeout=self.timeout
        )

    @decode_request
    def get_sub_position(self, position_id):
        params = {
            'token': self.token,
            'positionId': position_id
        }
        return requests.get(
            f'{self.base_url}/api/services/OrgPosition/GetChildPositionList',
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    def file_logger(self, module, fun, page_num, page_size, opt_time_start_str, opt_time_end_str):
        params = {
            'token': self.token,
            'module': module,
            'fun': fun
        }

        data = {
            'module': module,
            'fun': fun,
            'optUserIdstr': '',
            'pageNum': page_num,
            'pageSize': page_size,
            'destName': '',
            'OptSourceName': '',
            'OptSourceId': '',
            'objType': '0',
            'optTimeStartStr': opt_time_start_str,
            'optTimeEndStr': opt_time_end_str,
            'userRealName': '',
            'userIdArray': '',
            'optType': '',
            'curLang': 'zh-cn',
        }
        return requests.post(
            f'{self.base_url}/WebCore',
            params=params,
            data=data,
            headers=self.headers,
            verify=self.verify,
            timeout=self.timeout
        )

    @staticmethod
    def get_description() -> dict:
        return {
            "name": "鸿翼",
            "type": "ECM",
            "params": [
                {
                    "name": "Base URL",
                    "key": "base_url",
                    "remark": "鸿翼系统的网址,例如 http://www.baidu.com",
                    "required": True,
                    "type": "input",
                    "rules": [{"type": "url"}]
                },
                {
                    "name": "API Key",
                    "key": "token",
                    "remark": "鸿翼系统的登录token",
                    "required": True,
                    "type": "input"
                }
            ]
        }

    def system_init(self):
        sync_logger.info(f"添加定时同步文件任务,{self.related_sync_system}")
        SchedulerUtils.add_job(
            id=f'{self.related_sync_system}_log',
            func=self.file_log_listener,
            trigger=IntervalTrigger(
                seconds=randint(
                    int(SettingUtils.get_system_setting("ECM_API_LOG_JOB_INTERVAL_S", 1800)),
                    int(SettingUtils.get_system_setting("ECM_API_LOG_JOB_INTERVAL_E", 2100))
                )
            ),
            kwargs={}
        )


if __name__ == '__main__':
    ecm = EcmApi(base_url='a', token='b')
    print(ecm.to_dict())
    ecm.system_init()
