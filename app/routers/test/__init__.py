"""
测试API路由
"""

from fastapi import APIRouter
from app.routers.test import test

# 创建test路由器
router = APIRouter()

# 包含所有test路由
router.include_router(test.router, prefix="/test", tags=["测试相关接口"])