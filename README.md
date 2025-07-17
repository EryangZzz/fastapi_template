# FastAPI Template

[English](README_EN.md) | [中文](README.md)

A production-ready FastAPI template with modular architecture, global exception handling, unified response format, and comprehensive development tools.

## ✨ Features

- 🚀 **High Performance**: Built with FastAPI and uvloop for maximum speed
- 🏗️ **Modular Architecture**: Clean separation of concerns with layered structure
- 🔧 **Global Exception Handling**: Comprehensive error handling with business code system
- 📝 **Unified Response Format**: Consistent API response structure across all endpoints
- 🎯 **Custom JSON Encoding**: Enhanced serialization for datetime and decimal types
- ⚙️ **Configuration Management**: Environment-based configuration with Pydantic Settings
- 🧪 **Testing Ready**: Pre-configured testing setup with pytest and httpx
- 📦 **Modern Dependency Management**: Using uv for fast and reliable package management
- 🔄 **Database Ready**: SQLAlchemy 2.0 and Alembic integration (ready to use)
- 📊 **API Versioning**: Built-in API versioning support

## 🏛️ Architecture

```
app/
├── core/                   # Core functionality
│   ├── exceptions.py       # Custom exception classes
│   ├── exception_handlers.py # Global exception handlers
│   ├── responses.py        # Response models and business codes
│   └── json_encoders.py    # Custom JSON encoders
├── routers/               # API routing
│   ├── v1/               # API version 1
│   └── test/             # Test endpoints
├── schemas/              # Pydantic models
├── models/               # Database models
├── controllers/          # Request controllers
├── services/             # Business logic
├── settings/             # Configuration
└── utils/                # Utility functions
```

## 🚦 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fastapi-template.git
   cd fastapi-template
   ```

2. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Set up environment (optional)**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run the application**
   ```bash
   # Development mode
   uv run python main.py
   
   # Or using uvicorn directly
   uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

The application will be available at `http://localhost:8000`

## 📖 API Documentation

Once the application is running, you can access:

- **Interactive API Documentation (Swagger UI)**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

### Response Format

All API endpoints return responses in the following unified format:

```json
{
  "code": 200,
  "msg": "success", 
  "data": {
    // Your actual data here
  }
}
```

### Business Codes

| Code | Description |
|------|-------------|
| 200  | SUCCESS     |
| -1   | FAILURE     |
| 400  | BAD_REQUEST |
| 401  | UNAUTHORIZED|
| 500  | SERVER_ERROR|

### Example Endpoints

**Health Check**
```bash
GET /api/v1/health
```

**Test Endpoints**
```bash
# Test validation error handling
GET /api/test/test/test-validation-error

# Test general error handling  
GET /api/test/test/test-general-error

# Test datetime formatting
GET /api/test/test/test-datetime

# Test user creation
POST /api/test/test/users
Content-Type: application/json
{
  "name": "John Doe",
  "email": "john@example.com", 
  "age": 30
}
```

## ⚙️ Configuration

The application uses environment-based configuration. Create a `.env` file in the root directory:

```env
# Application
APP_NAME=FastAPI Template
APP_VERSION=1.0.0
DEBUG=true

# Server
HOST=0.0.0.0
PORT=8000

# Database (when needed)
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app

# Run specific test file
uv run pytest tests/test_health.py
```

## 🔧 Development

### Adding New Endpoints

1. **Create a new router** in `app/routers/v1/`
2. **Define Pydantic schemas** in `app/schemas/`
3. **Add business logic** in `app/services/`
4. **Register the router** in `app/routers/__init__.py`

Example:
```python
# app/routers/v1/users.py
from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    # Your business logic here
    return {"message": "User created successfully"}
```

### Custom Exceptions

Use the `CustomerException` for business logic errors:

```python
from app.core.exceptions import CustomerException
from app.core.responses import CustomerBusinessCode

# Raise a business exception
raise CustomerException(
    msg="User not found",
    custom_code=CustomerBusinessCode.BAD_REQUEST,
    content={"user_id": user_id}
)
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] Add authentication and authorization
- [ ] Add rate limiting middleware
- [ ] Add request/response logging
- [ ] Add database migration examples
- [ ] Add Docker support
- [ ] Add CI/CD workflows
- [ ] Add monitoring and metrics

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
- [uv](https://github.com/astral-sh/uv) - Package management

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you have any questions or need help, please:

1. Check the [Documentation](https://github.com/yourusername/fastapi-template/wiki)
2. Search existing [Issues](https://github.com/yourusername/fastapi-template/issues)
3. Create a new [Issue](https://github.com/yourusername/fastapi-template/issues/new)

---

**⭐ Star this repository if you find it helpful!** 