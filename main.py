"""
FastAPI 脚手架模板 - 应用启动入口
重构后的版本：只负责应用启动和模块组装
"""
import asyncio
import sys
from contextlib import asynccontextmanager

import uvloop
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.json_encoders import setup_global_json_encoders
from app.core.responses import CustomerJsonResponse
from app.core.exception_handlers import register_exception_handlers
from app.settings.config import settings
from app.routers import main_router


# =============================================================================
# 应用生命周期
# =============================================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时设置 uvloop
    if sys.platform != "win32":
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    
    # 启用全局JSON编码器
    setup_global_json_encoders()
    
    print(f"🚀 {settings.app_name} v{settings.app_version} 启动成功")
    print("✅ 全局datetime/Decimal格式化已启用")
    yield
    print("👋 应用关闭")


def register_middleware(current_app: FastAPI) -> FastAPI:
    """注册中间件"""
    current_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 生产环境应该设置具体的域名
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return current_app


def register_routers(current_app: FastAPI) -> FastAPI:
    """注册路由"""
    current_app.include_router(main_router)
    return current_app


def create_app() -> FastAPI:
    """创建FastAPI应用实例"""
    current_app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
        default_response_class=CustomerJsonResponse,  # 使用自定义响应类
    )
    
    # 注册组件
    register_middleware(current_app)
    register_exception_handlers(current_app)
    register_routers(current_app)
    
    return current_app


# =============================================================================
# 创建应用实例
# =============================================================================
app = create_app()


# =============================================================================
# 应用启动
# =============================================================================
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        loop="uvloop" if sys.platform != "win32" else "asyncio"
    ) 