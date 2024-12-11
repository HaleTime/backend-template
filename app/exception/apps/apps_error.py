from exception import BaseServiceError, BaseHttpException


class AppModelConfigBrokenError(BaseServiceError):
    pass


class AppNotFoundException(BaseHttpException):
    msg = "请求Agent不存在！"
    error_code = "1801001"


class TaskIdRequiredException(BaseHttpException):
    msg = "Task_id不能为空"
    error_code = "1801002"


class AppNoToolsException(BaseHttpException):
    msg = "Agent没有绑定tools！"
    error_code = "1801003"


class SystemAppNotFoundException(BaseHttpException):
    msg = "请求的系统App不存在！"
    error_code = "1801004"


class ToolsNotFoundException(BaseHttpException):
    msg = "未找到对应tools！"
    error_code = "1801005"


class FileSearchErrorException(BaseHttpException):
    msg = "文档查询失败！"
    error_code = "1801006"


class ExtractFieldErrorException(BaseHttpException):
    msg = "提取字段失败！"
    error_code = "1801007"


class ArgsMissingErrorException(BaseHttpException):
    msg = "缺少参数'{arg}'"
    error_code = "1801008"

    def __init__(self, arg, *args, **kwargs):
        self.msg = self.msg.format(arg=arg)
        super().__init__(*args, **kwargs)


class AccountSearchErrorException(BaseHttpException):
    msg = "客户查询失败！"
    error_code = "1801009"
