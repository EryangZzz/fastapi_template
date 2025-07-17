"""
统一响应格式处理
"""
from enum import Enum
from typing import Any
from fastapi.responses import JSONResponse


class CustomerBusinessCode(Enum):
    """业务响应码枚举"""
    SUCCESS = 200  # 成功
    FAILED = -1   # 失败(需要将信息展示给用户)
    SERVER_ERROR = 500  # 服务器未知错误
    BAD_REQUEST = 400   # 请求参数错误
    UNAUTHORIZED = 401  # 身份认证失败


class CustomerJsonResponse(JSONResponse):
    """
    自定义JSON响应类，负责统一响应格式包装
    序列化格式化由monkey patch的jsonable_encoder统一处理
    """
    
    def __init__(self, content: Any = None, status_code: int = 200, **kwargs):
        # 只负责包装为统一响应格式，不使用Pydantic类避免序列化干扰
        if isinstance(content, dict) and all(key in content for key in ["code", "msg", "data"]):
            # 已经是统一格式
            processed_content = content
        else:
            # 自动包装为统一格式（使用纯字典，避免Pydantic干扰）
            processed_content = {
                "code": CustomerBusinessCode.SUCCESS.value if status_code == 200 else status_code,
                "msg": "success" if status_code == 200 else "error",
                "data": content
            }
        
        # 直接传给父类，让FastAPI+monkey patch处理序列化
        super().__init__(content=processed_content, status_code=status_code, **kwargs) 