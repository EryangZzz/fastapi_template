"""
V1 API路由
"""

from fastapi import APIRouter
from app.routers.v1 import health

# 创建v1路由器
router = APIRouter()

# 包含所有v1路由
router.include_router(health.router, prefix="/health", tags=["健康检查接口"])