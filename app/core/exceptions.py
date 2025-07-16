"""
全局异常处理器
"""
from typing import Union
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from app.core.responses import CustomerJsonResponse


async def validation_exception_handler(request: Request, exc: Union[RequestValidationError, ValidationError]):
    """处理 Pydantic 校验异常"""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": " -> ".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    
    return CustomerJsonResponse(
        content={
            "code": 422,
            "msg": "参数校验失败",
            "data": {"errors": errors}
        },
        status_code=422
    )


async def general_exception_handler(request: Request, exc: Exception):
    """处理通用异常"""
    from app.settings.config import settings
    
    # 在生产环境中，不应该暴露详细的错误信息
    if settings.debug:
        error_detail = str(exc)
    else:
        error_detail = "服务器内部错误"
    
    return CustomerJsonResponse(
        content={
            "code": 500,
            "msg": error_detail,
            "data": None
        },
        status_code=500
    ) 