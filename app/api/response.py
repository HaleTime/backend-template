from typing import Any, Optional, TypeVar

from pydantic import BaseModel
import builtins

from core.db.dao import BaseDO

SUCCESS_CODE = "200"
SUCCESS_MSG = "success"

T = TypeVar('T', bound=BaseDO)


class ResponseModel(BaseModel):
    """接口响应封装类"""
    code: str = SUCCESS_CODE
    msg: str = SUCCESS_MSG
    data: Any = None
    errorInfo: Any = None

    def __init__(
            self,
            code: str = SUCCESS_CODE,
            msg: str = SUCCESS_MSG,
            data: Optional[Any] = None,
            errorInfo: Optional[Any] = None
    ) -> None:
        if data and type(data) not in vars(builtins).values():
            if issubclass(type(data), BaseDO):
                data = data.get_non_private_vars
            else:
                data = vars(data)
        super().__init__(code=code, msg=msg, data=data, errorInfo=errorInfo)


class PaginateModel:

    def __init__(
            self,
            page_no: Optional[int] = None,
            page_size: Optional[int] = None,
            total: Optional[int] = None,
            items: Optional[list[T]] = None
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.total = total
        if items:
            self.items = [item.get_non_private_vars for item in items]
