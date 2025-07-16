# FastAPI 脚手架模板 - 单文件版本

这是一个 FastAPI 脚手架的单文件版本，实现了需求点 4、5、6：

## 实现的功能

### 4. 全局异常处理机制 ✅
- 处理 Pydantic 校验异常 (`RequestValidationError`, `ValidationError`)
- 处理通用异常 (`Exception`)
- 异常信息格式化，开发环境显示详细信息，生产环境隐藏敏感信息

### 5. 统一 JSON 响应处理 ✅
- 所有接口返回统一格式：`{code: xx, msg: xx, data: xx}`
- 自动处理 Python 对象、Pydantic 模型等不同类型的返回值
- 对接口无感，自动包装响应

### 6. 精简的 app 启动文件 ✅
- 精简的启动逻辑，只包含核心配置
- 中间件注册 (CORS)
- 异常处理器注册
- 使用 uvloop 高性能事件循环
- 使用 uvicorn 启动服务

## 快速开始

### 1. 安装依赖
```bash
cd fastapi_template
uv sync
```

### 2. 创建环境变量文件（可选）
```bash
# 创建 .env 文件
echo "APP_NAME=FastAPI Template" > .env
echo "APP_VERSION=0.1.0" >> .env
echo "DEBUG=true" >> .env
```

### 3. 运行服务
```bash
# 方式1：直接运行
uv run python main.py

# 方式2：使用 uvicorn
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 测试接口

### 1. 基础接口测试
```bash
# 根路径 - 测试统一响应格式
curl http://localhost:8000/

# 健康检查 - 测试 Pydantic 模型响应
curl http://localhost:8000/health
```

### 2. 参数校验测试
```bash
# 正确的请求
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "张三", "email": "zhangsan@example.com", "age": 25}'

# 错误的请求 - 测试参数校验异常
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "", "email": "invalid-email", "age": "not-a-number"}'
```

### 3. 异常处理测试
```bash
# 测试 Pydantic 校验异常
curl http://localhost:8000/test-validation-error

# 测试通用异常处理
curl http://localhost:8000/test-general-error
```

## 响应格式示例

### 成功响应
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "message": "FastAPI Template is running!"
  }
}
```

### 校验错误响应
```json
{
  "code": 422,
  "msg": "参数校验失败",
  "data": {
    "errors": [
      {
        "field": "age",
        "message": "Input should be a valid integer",
        "type": "int_parsing"
      }
    ]
  }
}
```

### 服务器错误响应
```json
{
  "code": 500,
  "msg": "服务器内部错误",
  "data": null
}
```

## 技术特性

- ✅ 使用 Python 3.12
- ✅ 使用 uv 管理依赖
- ✅ 使用 uvloop 高性能事件循环
- ✅ 使用 uvicorn 启动服务
- ✅ 全局异常处理
- ✅ 统一响应格式
- ✅ 精简的启动文件
- ✅ CORS 中间件支持
- ✅ 配置文件支持 (.env)

## 下一步

当您测试通过后，我将把单文件版本拆分为完整的脚手架架构，包括：
- 接口路由层（版本控制）
- Controller 层
- Service 层  
- Models 层
- Core 层
- Utils 层
- Schemas 层
- Alembic 数据库迁移
- Tests 层 