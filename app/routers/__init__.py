"""
Routers 模块
包含所有API路由定义
"""

from fastapi import APIRouter
from app.routers.v1 import router as v1_router
from app.routers.test import router as test_router

# 创建总路由器
main_router = APIRouter()

# 包含V1 API路由
main_router.include_router(v1_router, prefix="/api/v1")

# 包含测试路由 
main_router.include_router(test_router, prefix="/api/test")


