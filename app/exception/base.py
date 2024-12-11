from typing import Optional


class BaseServiceError(Exception):
    def __init__(self, description: str = None):
        self.description = description


class BaseHttpException(Exception):
    status_code: int = 400
    msg: Optional[str] = None
    error_code: Optional[str] = None

    def __init__(self, *args, **kwargs):
        self.status_code = kwargs.get('status_code', self.status_code) if kwargs else self.status_code
        self.msg = kwargs.get('msg', self.msg) if kwargs else self.msg
        self.error_code = kwargs.get('error_code', self.error_code) if kwargs else self.error_code


class SystemException(BaseHttpException):
    error_code = "1010001"
    msg = "系统异常"
    status_code = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = args[0] if args else self.msg


if __name__ == '__main__':
    a = SystemException()
    print(a.status_code)
    print(a.msg)
    print(a.error_code)
