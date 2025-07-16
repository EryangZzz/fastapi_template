"""
全局JSON编码器配置
负责datetime、date、time、Decimal的统一格式化
"""
from datetime import datetime, date, time
from decimal import Decimal


# 全局JSON编码器配置
GLOBAL_JSON_ENCODERS = {
    datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S"),
    date: lambda d: d.strftime("%Y-%m-%d"),
    time: lambda t: t.strftime("%H:%M:%S"),
    Decimal: str,
}


def setup_global_json_encoders():
    """
    设置全局JSON编码器，通过monkey patch重写jsonable_encoder的默认行为
    这确保了所有数据类型都能使用统一的格式化规则
    """
    from fastapi import encoders
    import fastapi.routing
    
    # 保存原始的jsonable_encoder函数
    original_jsonable_encoder = encoders.jsonable_encoder
    
    def patched_jsonable_encoder(obj, **kwargs):
        """增强版的jsonable_encoder，自动使用我们的自定义编码器"""
        if 'custom_encoder' not in kwargs:
            kwargs['custom_encoder'] = GLOBAL_JSON_ENCODERS
        else:
            # 如果已经有custom_encoder，将我们的编码器合并进去
            custom_encoder = kwargs['custom_encoder']
            merged_encoder = {**GLOBAL_JSON_ENCODERS, **custom_encoder}
            kwargs['custom_encoder'] = merged_encoder
        
        return original_jsonable_encoder(obj, **kwargs)
    
    # 替换全局的jsonable_encoder函数
    encoders.jsonable_encoder = patched_jsonable_encoder
    fastapi.routing.jsonable_encoder = patched_jsonable_encoder 