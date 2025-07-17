"""
测试API路由
包含datetime/Decimal格式化测试和异常处理测试
"""
from datetime import datetime, date, time
from decimal import Decimal
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.schemas.base import BaseSchema
from app.core.exceptions import CustomerException
from app.core.responses import CustomerBusinessCode

router = APIRouter()


# 测试用的Schema类（仅用于测试）
class UserCreate(BaseSchema):
    name: str
    email: str
    age: int


class UserResponse(BaseSchema):
    id: int
    name: str
    email: str
    age: int


class OrderModel(BaseSchema):
    id: int
    order_date: datetime
    delivery_date: date
    created_time: time
    amount: Decimal


# ========== DateTime/Decimal 格式化测试 ==========
@router.get("/test-datetime")
async def test_datetime():
    """测试datetime/Decimal格式化"""
    return {
        "python_objects": {
            "current_datetime": datetime.now(),
            "current_date": date.today(),
            "current_time": datetime.now().time(),
            "price": Decimal("99.99"),
        },
        "pydantic_model": OrderModel(
            id=1,
            order_date=datetime(2024, 1, 1, 12, 30, 45),
            delivery_date=date(2024, 2, 1),
            created_time=time(9, 0, 0),
            amount=Decimal("299.99")
        ),
        "orm_object": {
            "id": 2,
            "created_at": datetime.now(),
            "updated_date": date.today(),
            "process_time": time(14, 30, 0),
            "price": Decimal("199.99")
        },
        "nested_data": {
            "metadata": {
                "created": datetime.now(),
                "cost": Decimal("19.99")
            },
            "items": [
                {
                    "timestamp": datetime(2024, 1, 1, 10, 0, 0),
                    "amount": Decimal("100.50")
                }
            ]
        }
    }


@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    """创建用户 - 测试参数校验和响应处理"""
    return {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }


# ========== 异常处理测试 ==========
@router.get("/test-validation-error")
async def validation_error():
    """测试校验异常处理"""
    raise ValidationError.from_exception_data(
        "test",
        [{"type": "missing", "loc": ("test_field",), "msg": "Field required"}]
    )


@router.get("/test-general-error")
async def general_error():
    """测试通用异常处理"""
    raise ValueError("这是一个测试异常")


@router.get("/test-custom-response")
async def test_custom_response():
    """测试直接返回 Response 对象（不会被CustomerJsonResponse处理）"""
    return JSONResponse(
        content={
            "custom_format": True,
            "message": "这是一个自定义格式的响应",
            "timestamp": "2024-01-01T00:00:00Z"
        },
        status_code=200
    )


# ========== 自定义异常测试 ==========
@router.get("/test-business-exception")
async def test_business_exception():
    """测试业务异常处理"""
    raise CustomerException(
        msg="用户名已存在", 
        custom_code=CustomerBusinessCode.FAILED,
        content={"suggested_names": ["user1", "user2"]}
    )


@router.get("/test-bad-request-exception")
async def test_bad_request_exception():
    """测试请求参数异常处理"""
    raise CustomerException(
        msg="年龄参数无效",
        custom_code=CustomerBusinessCode.BAD_REQUEST,
        content={"field": "age", "value": -1, "min": 0, "max": 120}
    ) 