from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from controllers.response import ResponseModel
from exception import SystemException, BaseHttpException


async def fastapi_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, RequestValidationError):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content=jsonable_encoder(
                                ResponseModel(code="9001", msg="参数校验错误", errorInfo=exc.errors())))
    elif isinstance(exc, BaseHttpException):
        return JSONResponse(status_code=exc.status_code,
                            content=jsonable_encoder(ResponseModel(code=exc.error_code, msg=exc.msg)))
    elif isinstance(exc, SystemException):
        return JSONResponse(status_code=exc.status_code,
                            content=jsonable_encoder(ResponseModel(code=exc.error_code, msg=exc.msg)))
    else:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=jsonable_encoder(ResponseModel(code="100000", msg="未知错误")))
