"""
Schema基类
统一配置所有Pydantic模型的序列化行为
"""
from pydantic import BaseModel
from app.core.json_encoders import GLOBAL_JSON_ENCODERS


class BaseSchema(BaseModel):
    """
    所有Pydantic模型的基类
    统一配置json_encoders，确保序列化格式一致
    """
    class Config:
        json_encoders = GLOBAL_JSON_ENCODERS 