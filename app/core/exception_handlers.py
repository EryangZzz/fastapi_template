"""
全局异常处理器
"""
from typing import Union
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from app.core.responses import CustomerJsonResponse, CustomerBusinessCode
from app.core.exceptions import CustomerException


def _format_validation_errors(exc: Union[RequestValidationError, ValidationError]) -> list:
    """格式化校验错误的内部函数"""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": " -> ".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    return errors


def register_exception_handlers(app: FastAPI):
    """全局异常处理器注册函数"""
    
    @app.exception_handler(CustomerException)
    async def customer_exception_handler(request: Request, exc: CustomerException):
        """处理自定义业务异常"""
        return CustomerJsonResponse(
            content={
                "code": exc.custom_code.value,
                "msg": exc.msg,
                "data": exc.content
            },
            status_code=exc.status_code
        )
    
    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        """处理 FastAPI 请求校验异常"""
        errors = _format_validation_errors(exc)
        
        return CustomerJsonResponse(
            content={
                "code": CustomerBusinessCode.BAD_REQUEST.value,
                "msg": "参数校验失败",
                "data": {"errors": errors}
            },
            status_code=200
        )

    @app.exception_handler(ValidationError)
    async def pydantic_validation_exception_handler(request: Request, exc: ValidationError):
        """处理 Pydantic 校验异常"""
        errors = _format_validation_errors(exc)
        
        return CustomerJsonResponse(
            content={
                "code": CustomerBusinessCode.BAD_REQUEST.value,
                "msg": "参数校验失败",
                "data": {"errors": errors}
            },
            status_code=200
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """处理通用异常"""
        # 日志打印错误调用栈
        return CustomerJsonResponse(
            content={
                "code": CustomerBusinessCode.SERVER_ERROR.value,
                "msg": "服务器内部错误",
                "data": None
            },
            status_code=200
        )
    return app 