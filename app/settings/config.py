"""
应用配置管理
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用配置"""
    app_name: str = "FastAPI Template"
    app_version: str = "1.0.0"
    debug: bool = False
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# 全局设置实例
settings = Settings() 