"""
健康检查API
"""
from datetime import datetime
from fastapi import APIRouter

from app.settings.config import settings

router = APIRouter()


@router.get("/", summary="根路径")
async def root():
    """根路径"""
    return {"message": f"{settings.app_name} is running!", "version": settings.app_version}


@router.get("/health")
async def health_check():
    """健康检查"""
    return {
        "code": 200,
        "msg": "服务运行正常",
        "data": {
            "status": "healthy", 
            "version": settings.app_version,
            "timestamp": datetime.now()
        }
    } 