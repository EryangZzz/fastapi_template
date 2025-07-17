"""
自定义异常类
"""
from typing import Any
from app.core.responses import CustomerBusinessCode


class CustomerException(Exception):
    """自定义业务异常类"""
    
    def __init__(
        self,
        msg: str = "",
        custom_code: CustomerBusinessCode = CustomerBusinessCode.FAILED,
        content: Any = None,
        status_code: int = 200,
    ):
        """
        初始化自定义异常
        
        Args:
            msg: 错误消息
            custom_code: 业务错误码，默认为FAILED(-1)
            content: 额外数据内容
            status_code: HTTP状态码，默认为200
        """
        # 校验custom_code是否为CustomerBusinessCode枚举类型
        assert isinstance(
            custom_code, CustomerBusinessCode
        ), "custom_code must be CustomerBusinessCode"
        
        self.msg = msg
        self.custom_code = custom_code
        self.content = content
        self.status_code = status_code
        super().__init__(self.msg)

