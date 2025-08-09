# 🚀 AI Development Guidelines & Standards

## 📜 MANDATORY WORKFLOW & RESPONSE FORMAT

**THE AI AGENT MUST FOLLOW THIS WORKFLOW FOR EVERY TASK. NO DEVIATIONS.**

### 1. Acknowledge Core Principles
At the beginning of every response, you MUST include the following acknowledgement verbatim:

> I acknowledge and will follow all development guidelines, including the mandatory workflow, journaling, and research protocols.

### 2. Pre-Implementation Analysis
Before writing any code, you MUST perform the following checks:

*   **Development Journal**: Review `docs/DEVELOPMENT_JOURNAL.md` for previous entries related to the current task.
*   **Problem Patterns**: Review `docs/COMMON_PROBLEMS.md` to avoid repeating past mistakes.
*   **Success Patterns**: Review `docs/SUCCESS_PATTERNS.md` to apply established best practices.
*   **Package Research**: If the task involves a new package, you MUST first consult the `research/` directory as per the [Package Research & Integration](#-package-research--integration) guidelines.

### 3. Adhere to the Response Template
Structure your entire response according to this template.

---
**START OF RESPONSE TEMPLATE**
---

#### 🔍 Pre-Implementation Analysis
*   **Journal Check**: [Link to related entries, or "No related entries found."]
*   **Common Problems Review**: [Note on relevant patterns checked, or "No relevant patterns found."]
*   **Success Patterns Review**: [Note on patterns to be applied, or "No relevant patterns to apply."]
*   **Package Research Check**: [e.g., "Consulted `research/steelpy_README_LLM.md` for usage patterns." or "Not applicable."]

#### 🎯 Implementation Plan
1.  **Step 1**: [Description of the first step]
2.  **Step 2**: [Description of the second step]
3.  ...

#### 📂 Files to be Modified
*   `path/to/file1.py`: [Summary of changes]
*   `path/to/file2.py`: [Summary of changes]

#### 💻 Implementation```python
# Code for the implementation goes here.
# It must be clean, commented, and follow all quality standards.
```

#### 📔 Development Journal Entry
A new, complete journal entry MUST be generated for every task.

```markdown
### 📅 [Date] - [Time] - Entry #[Number]

#### 📋 Task/Request
> [Brief description of what was requested]

#### 🎯 Approach
- Step-by-step approach taken.
- Key decisions made.
- Files modified: `[list of files]`
- Design patterns used: [e.g., Repository, Singleton]

#### 🐛 Problems Encountered
- **Problem**: [Description or "None"]
- **Root Cause**: [Analysis or "N/A"]
- **Solution**: [How it was fixed or "N/A"]

#### ✅ Solution Implemented
```python
# Final code snippet of the solution.
```

#### 📝 Lessons Learned
- [What worked, what to avoid, patterns to remember]

#### 🏷️ Tags
[e.g., #feature, #bugfix, #refactor]
```

---
**END OF RESPONSE TEMPLATE**
---

### 4. Post-Implementation
After the implementation is complete, you MUST perform the following steps:

*   **Verify Changes**: Double-check all modifications to ensure they are correct, complete, and exactly as intended.
*   **Debug and Finalize**: Run tests, check code quality, and ensure the implementation is free of errors before concluding the task.

## ⚡ Core Principles (Unmodifiable)
<principles>
1.  **Follow Guidelines**: Adhere to these guidelines explicitly. They are not open to interpretation.
2.  **Explicit Implementation**: Only implement what is explicitly requested. Do not make unauthorized changes.
3.  **Code Consistency**: Maintain consistency with existing codebase patterns and style.
4.  **Security First**: Prioritize security and best practices in all implementations.
5.  **Journaling is Mandatory**: Document all problems and solutions in the development journal for every task.
6.  **Human-Readable Code**: Write code for humans to read, not just for machines to execute.
7.  **Research Before Integrating**: Always follow the [Package Research & Integration](#-package-research--integration) protocol before adding new dependencies.
8.  **Verify and Finalize**: Always verify changes and finalize the code quality before completing a task.
</principles>

## 📋 Table of Contents
1. [MANDATORY WORKFLOW & RESPONSE FORMAT](#-mandatory-workflow--response-format)
2. [Core Principles (Unmodifiable)](#-core-principles-unmodifiable)
3. [Development Journal System](#-development-journal-system)
4. [Code Quality Standards](#-code-quality-standards)
5. [Python Best Practices](#-python-best-practices)
6. [Security Requirements](#-security-requirements)
7. [Testing & Validation](#-testing--validation)
8. [Performance Guidelines](#-performance-guidelines)
9. [Documentation Standards](#-documentation-standards)
10. [Error Handling](#-error-handling)
11. [Package Research & Integration](#-package-research--integration)
12. [Code Smells to Avoid](#-code-smells-to-avoid)
13. [Git & Version Control](#-git--version-control)
14. [Monitoring & Logging](#-monitoring--logging)
15. [Code Review Checklist](#-code-review-checklist)
16. [Continuous Learning](#-continuous-learning)
17. [Quick Reference](#-quick-reference)

---

## 📔 Development Journal System

### Initial Setup (Create on First Interaction)

Create the following structure in `docs/`:

#### 1. `docs/DEVELOPMENT_JOURNAL.md`
```markdown
# Development Journal

## Project Overview
- **Started**: [Current Date]
- **Tech Stack**: Python [Version], [Frameworks]
- **Purpose**: Track development decisions, problems, and solutions
- **Conventions**: PEP 8, Type Hints, Black formatting

---

## Entry Template

### 📅 [Date] - [Time] - Entry #[Number]

#### 📋 Task/Request
> Brief description of what was requested

#### 🎯 Approach
- Step-by-step approach taken
- Key decisions made
- Files modified: `[list files]`
- Design patterns used: [e.g., Factory, Singleton, Repository]

#### 🐛 Problems Encountered
1. **Problem**: [Description]
   
- **Error Message**: `[if applicable]`
   - **Root Cause**: [Analysis]
   - **Solution**: [How it was fixed]
   - **Prevention**: [How to avoid in future]
   - **Time to Resolve**: [Approximate]

#### ✅ Solution Implemented
```python
# Code snippet of the solution
```
#### 🔍 Code Review Notes
- **Complexity**: [Cyclomatic complexity if relevant]
- **Test Coverage**: [Percentage]
- **Performance Impact**: [If applicable]

#### 📝 Lessons Learned
- What worked well
- What to avoid next time
- Patterns to remember
- Dependencies added/removed

#### 🏷️ Tags
`#feature` `#bugfix` `#refactor` `#performance` `#security`

#### 🔗 Related Entries
- **Previous**: Entry #[X]
- **Next**: Entry #[Y]
- **Related**: Entry #[Z]
```

#### 2. `docs/COMMON_PROBLEMS.md`
```markdown
# Common Problems & Solutions

## Quick Reference Index
- [Database Issues](#database-issues)
- [Import Errors](#import-errors)
- [Type Errors](#type-errors)
- [Performance Problems](#performance-problems)
- [Security Vulnerabilities](#security-vulnerabilities)

## Database Issues

### Connection Pool Exhaustion
```python
# ❌ Problem Pattern
def get_data():
    conn = create_connection()  # Never closed
    return conn.execute(query)

# ✅ Solution Pattern
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = create_connection()
    try:
        yield conn
    finally:
        conn.close()
```
[Continue with patterns...]
```

#### 3. `docs/SUCCESS_PATTERNS.md`
```markdown
# Successful Implementation Patterns

## Design Patterns That Work

### Repository Pattern for Data Access
```python
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class Repository(ABC, Generic[T]):
    @abstractmethod
    async def get(self, id: int) -> Optional[T]:
        pass
    
    @abstractmethod
    async def get_all(self) -> List[T]:
        pass
    
    @abstractmethod
    async def add(self, entity: T) -> T:
        pass
    
    @abstractmethod
    async def update(self, entity: T) -> T:
        pass
    
    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass

class UserRepository(Repository[User]):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get(self, id: int) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.id == id)
        )
        return result.scalar_one_or_none()
```
[Continue with patterns...]
```

---

## 🎯 Code Quality Standards

### Clean Code Principles (Based on Robert C. Martin)

#### 1. Meaningful Names
```python
# ❌ BAD - Unclear variable names
def calc(x, y, z):
    return x * y * z / 100

# ✅ GOOD - Self-documenting names
def calculate_compound_interest(
    principal: float, 
    rate: float, 
    time_years: float
) -> float:
    """Calculate compound interest."""
    return principal * rate * time_years / 100
```

#### 2. Functions Should Do One Thing
```python
# ❌ BAD - Multiple responsibilities
def process_user_data(user_data):
    # Validate
    if not user_data.get('email'):
        raise ValueError("Email required")
  
    # Transform
    user_data['email'] = user_data['email'].lower()
    
    # Save to database
    db.save(user_data)
    
    # Send email
    send_welcome_email(user_data['email'])
    
    return user_data

# ✅ GOOD - Single responsibility
def validate_user_data(user_data: dict) -> None:
    """Validate user data."""
    if not user_data.get('email'):
        raise ValueError("Email required")

def normalize_user_data(user_data: dict) -> dict:
    """Normalize user data."""
    normalized = user_data.copy()
    normalized['email'] = normalized['email'].lower()
    return normalized

def save_user(user_data: dict) -> User:
    """Save user to database."""
    return db.save(user_data)

def notify_new_user(email: str) -> None:
    """Send welcome notification."""
    send_welcome_email(email)
```

#### 3. Don't Repeat Yourself (DRY)
```python
# ❌ BAD - Duplicated logic
def get_user_by_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_user_by_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# ✅ GOOD - Reusable abstraction
def execute_query(query: str, params: tuple = ()) -> Any:
    """Execute a database query with proper resource management."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

def get_user_by_email(email: str) -> Optional[User]:
    """Get user by email."""
    return execute_query(
        "SELECT * FROM users WHERE email = ?", 
        (email,)
    )

def get_user_by_id(user_id: int) -> Optional[User]:
    """Get user by ID."""
    return execute_query(
        "SELECT * FROM users WHERE id = ?", 
        (user_id,)
    )
```

## 🐍 Python Best Practices
### Project Structure
```
project/
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   └── dependencies.py
│   │   └── middleware.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── exceptions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── domain/         # Business entities
│   │   ├── schemas/        # Pydantic models
│   │   └── database/       # SQLAlchemy models
│   ├── services/           # Business logic
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── repositories/       # Data access layer
│   │   ├── __init__.py
│   │   └── user_repository.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
│   ├── DEVELOPMENT_JOURNAL.md
│   ├── COMMON_PROBLEMS.md
│   ├── SUCCESS_PATTERNS.md
│   └── API.md
├── scripts/               # Utility scripts
├── .env.example
├── .gitignore
├── pyproject.toml         # Modern Python packaging
├── requirements.txt       # Or use poetry.lock
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### Type Hints & Static Typing
```python
from typing import Optional, List, Dict, Union, TypeVar, Generic
from datetime import datetime
from pydantic import BaseModel, EmailStr, validator

# Use TypeVar for generic types
T = TypeVar('T')

class Response(BaseModel, Generic[T]):
    """Generic API response wrapper."""
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None
    timestamp: datetime = datetime.utcnow()

# Use Pydantic for data validation
class UserCreate(BaseModel):
    """User creation schema."""
    email: EmailStr
    username: str
    password: str
    
    @validator('username')
    def validate_username(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters')
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v.lower()
    
    @validator('password')
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v
```

### Dependency Management
```toml
# pyproject.toml
[tool.poetry]
name = "project-name"
version = "0.1.0"
description = "Project description"

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.104.0"
sqlalchemy = "^2.0.0"
pydantic = "^2.0.0"
alembic = "^1.12.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-cov = "^4.1.0"
black = "^23.9.0"
ruff = "^0.0.290"
mypy = "^1.5.0"
pre-commit = "^3.4.0"

[tool.black]
line-length = 88
target-version = ['py311']

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W", "UP", "B", "C4", "SIM", "RUF"]
ignore = ["E501"]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

## 🔒 Security Requirements
### Security Checklist
```python
# security_config.py
from typing import List
import secrets
from datetime import timedelta

class SecurityConfig:
    """Security configuration."""
    
    # ✅ REQUIRED Security Settings
    SECRET_KEY: str = secrets.token_urlsafe(32)  # Generate strong secret
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE: timedelta = timedelta(minutes=30)
    REFRESH_TOKEN_EXPIRE: timedelta = timedelta(days=7)
    
    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = [
        "https://yourdomain.com",
        # Never use "*" in production
    ]
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_PERIOD: int = 60  # seconds
    
    # Password Policy
    MIN_PASSWORD_LENGTH: int = 12
    REQUIRE_UPPERCASE: bool = True
    REQUIRE_LOWERCASE: bool = True
    REQUIRE_NUMBERS: bool = True
    REQUIRE_SPECIAL: bool = True
    
    # Session Security
    SESSION_COOKIE_SECURE: bool = True  # HTTPS only
    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SAMESITE: str = "strict"
```

### Input Validation & Sanitization
```python
import re
from typing import Any
import bleach
from pydantic import validator

class InputSanitizer:
    """Input sanitization utilities."""
    
    @staticmethod
    def sanitize_html(text: str) -> str:
        """Remove dangerous HTML."""
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'p', 'br']
        return bleach.clean(text, tags=allowed_tags)
    
    @staticmethod
    def sanitize_sql_identifier(identifier: str) -> str:
        """Sanitize SQL identifiers."""
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', identifier):
            raise ValueError(f"Invalid identifier: {identifier}")
        return identifier
    
    @staticmethod
    def validate_file_upload(file_content: bytes, allowed_types: List[str]) -> bool:
        """Validate file uploads."""
        import magic
        file_type = magic.from_buffer(file_content, mime=True)
        return file_type in allowed_types
```

### SQL Injection Prevention
```python
# ❌ NEVER DO THIS
def get_user_unsafe(user_id: str):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL Injection risk!
    return db.execute(query)

# ✅ ALWAYS USE PARAMETERIZED QUERIES
from sqlalchemy import text

def get_user_safe(user_id: int):
    query = text("SELECT * FROM users WHERE id = :user_id")
    return db.execute(query, {"user_id": user_id})

# ✅ OR USE ORM
from sqlalchemy.orm import Session

def get_user_orm(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
```

## 🧪 Testing & Validation
### Testing Strategy
```python
# tests/conftest.py
import pytest
from typing import Generator
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope="session")
def db_engine():
    """Create test database engine."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(db_engine):
    """Create test database session."""
    SessionLocal = sessionmaker(bind=db_engine)
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()

@pytest.fixture
def client(db_session) -> Generator:
    """Create test client."""
    def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
```

### Unit Test Example
```python
# tests/unit/test_user_service.py
import pytest
from unittest.mock import Mock, patch
from src.services.user_service import UserService

class TestUserService:
    """Test user service."""
    
    @pytest.fixture
    def user_service(self):
        """Create user service with mocked dependencies."""
        mock_repo = Mock()
        mock_email_service = Mock()
        return UserService(mock_repo, mock_email_service)
    
    def test_create_user_success(self, user_service):
        """Test successful user creation."""
        # Arrange
        user_data = {"email": "test@example.com", "username": "testuser"}
        user_service.repository.create.return_value = User(**user_data)
        
        # Act
        result = user_service.create_user(user_data)
        
        # Assert
        assert result.email == user_data["email"]
        user_service.repository.create.assert_called_once()
        user_service.email_service.send_welcome.assert_called_once()
    
    def test_create_user_duplicate_email(self, user_service):
        """Test user creation with duplicate email."""
        # Arrange
        user_service.repository.get_by_email.return_value = Mock()
        
        # Act & Assert
        with pytest.raises(ValueError, match="Email already exists"):
            user_service.create_user({"email": "existing@example.com"})
```

### Integration Test Example
```python
# tests/integration/test_api.py
def test_create_user_endpoint(client, db_session):
    """Test user creation endpoint."""
    # Arrange
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "SecurePass123!"
    }
    
    # Act
    response = client.post("/api/v1/users", json=user_data)
    
    # Assert
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == user_data["email"]
    assert "password" not in data  # Password should not be returned
    
    # Verify database
    user = db_session.query(User).filter_by(email=user_data["email"]).first()
    assert user is not None
    assert user.username == user_data["username"]
```

## ⚡ Performance Guidelines
### Performance Best Practices
```python
# 1. Use generators for large datasets
def process_large_file(file_path: str):
    """Process large file line by line."""
    with open(file_path, 'r') as file:
        for line in file:  # Generator, doesn't load entire file
            yield process_line(line)

# 2. Implement caching
from functools import lru_cache
import redis

# In-memory caching
@lru_cache(maxsize=128)
def expensive_calculation(param: int) -> int:
    """Cache expensive calculations."""
    return complex_operation(param)

# Redis caching
class CacheService:
    def __init__(self):
        self.redis = redis.Redis(decode_responses=True)
    
    def get_or_set(self, key: str, func, ttl: int = 3600):
        """Get from cache or compute and cache."""
        value = self.redis.get(key)
        if value is None:
            value = func()
            self.redis.setex(key, ttl, value)
        return value

# 3. Use database connection pooling
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600,
    pool_pre_ping=True
)

# 4. Avoid N+1 queries
from sqlalchemy.orm import joinedload

# ❌ BAD - N+1 query problem
users = session.query(User).all()
for user in users:
    print(user.posts)  # Each iteration queries database

# ✅ GOOD - Eager loading
users = session.query(User).options(
    joinedload(User.posts)
).all()
for user in users:
    print(user.posts)  # No additional queries

# 5. Use bulk operations
# ❌ BAD - Individual inserts
for item in items:
    session.add(Item(**item))
    session.commit()

# ✅ GOOD - Bulk insert
session.bulk_insert_mappings(Item, items)
session.commit()
```

### Async Best Practices
```python
import asyncio
from typing import List
import aiohttp
from concurrent.futures import ThreadPoolExecutor

# Use async for I/O operations
async def fetch_data(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetch data asynchronously."""
    async with session.get(url) as response:
        return await response.json()

async def fetch_multiple(urls: List[str]) -> List[dict]:
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Use thread pool for CPU-bound operations
executor = ThreadPoolExecutor(max_workers=4)

async def process_cpu_intensive(data):
    """Run CPU-intensive task in thread pool."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        executor, 
        cpu_intensive_function, 
        data
    )
```

## 📝 Documentation Standards
### Docstring Format (Google Style)
```python
def complex_function(
    param1: str,
    param2: int,
    optional_param: Optional[str] = None
) -> Dict[str, Any]:
    """
    Brief description of function purpose.

    Detailed explanation of what the function does, including any
    important algorithms or business logic.

    Args:
        param1: Description of param1
        param2: Description of param2
        optional_param: Description of optional parameter
    
    Returns:
        Dictionary containing:
            - key1: Description of key1
            - key2: Description of key2
    
    Raises:
        ValueError: When param1 is empty
        TypeError: When param2 is not an integer
    
    Example:
        >>> result = complex_function("test", 42)
        >>> print(result["key1"])
        "processed_test"
    
    Note:
        Any important notes about usage or limitations
    
    Journal:
        See Entry #123 for implementation details
    """
    pass
```

### API Documentation
```python
from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="API Title",
    description="API Description",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

class UserResponse(BaseModel):
    """User response schema."""
    id: int = Field(..., description="User ID")
    email: str = Field(..., description="User email address")
    created_at: datetime = Field(..., description="Account creation timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "email": "user@example.com",
                "created_at": "2024-01-01T00:00:00Z"
            }
        }

@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Create a new user account with email and password",
    response_description="The created user",
    tags=["users"]
)
async def create_user(user: UserCreate):
    """Create a new user."""
    pass
```

## 🚨 Error Handling
### Comprehensive Error Handling
```python
from enum import Enum
from typing import Optional, Dict, Any
import logging
import traceback

logger = logging.getLogger(__name__)

class ErrorCode(Enum):
    """Application error codes."""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    CONFLICT = "CONFLICT"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    EXTERNAL_SERVICE_ERROR = "EXTERNAL_SERVICE_ERROR"

class AppException(Exception):
    """Base application exception."""
    
    def __init__(
        self,
        message: str,
        code: ErrorCode,
        status_code: int,
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

class ValidationError(AppException):
    """Validation error."""
    
    def __init__(self, message: str, details: Dict[str, Any]):
        super().__init__(
            message=message,
            code=ErrorCode.VALIDATION_ERROR,
            status_code=400,
            details=details
        )

class NotFoundError(AppException):
    """Resource not found error."""
    
    def __init__(self, resource: str, identifier: Any):
        super().__init__(
            message=f"{resource} not found",
            code=ErrorCode.NOT_FOUND,
            status_code=404,
            details={"resource": resource, "identifier": str(identifier)}
        )

# Global exception handler
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    """Handle application exceptions."""
    logger.error(
        f"Application error: {exc.code.value}",
        extra={
            "message": exc.message,
            "details": exc.details,
            "path": request.url.path
        }
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code.value,
                "message": exc.message,
                "details": exc.details
            }
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    logger.exception(
        "Unexpected error",
        extra={
            "path": request.url.path,
            "traceback": traceback.format_exc()
        }
    )
    
    # Don't expose internal details in production
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": ErrorCode.INTERNAL_ERROR.value,
                "message": "An internal error occurred"
            }
        }
    )
```

## 📦 Package Research & Integration

**MANDATORY PROTOCOL: Before integrating any new third-party package, you MUST check the `research/` directory.**

This protocol is non-negotiable. Failure to check the `research/` directory before integrating a new package is a violation of the core development guidelines.

### Workflow
1.  **Identify Requirement**: A task requires a new package (e.g., `forallpeople`, `steelpy`).
2.  **Cease Implementation**: Stop all implementation work.
3.  **Consult Research Directory**: Navigate to the `research/` directory.
4.  **Locate and Read Documentation**:
    *   Open and thoroughly read `{package_name}_README_LLM.md`. This is your primary source of truth.
    *   Open and review `{package_name}_requirements_report.md` for dependency information.
5.  **Adhere to Research**: Your implementation MUST strictly follow the examples, patterns, and installation instructions provided in the research files.
6.  **Proceed with Implementation**: Only after completing the steps above may you proceed with the implementation.

### Rationale
The `research/` directory contains pre-analyzed, LLM-optimized documentation to ensure correct, secure, and consistent integration of third-party packages. Bypassing this step introduces significant risk of errors, security vulnerabilities, and inconsistencies.

---

## 🦨 Code Smells to Avoid
### 1. Long Methods (> 20 lines)
```python
# ❌ BAD - Method too long
def process_order(order_data):
    # ... (implementation with multiple responsibilities)

# ✅ GOOD - Broken into smaller methods
class OrderProcessor:
    def process_order(self, order_data: OrderData) -> Order:
        """Process an order."""
        self.validate_order(order_data)
        pricing = self.calculate_pricing(order_data)
        order = self.create_order(order_data, pricing)
        self.send_notifications(order)
        return order
    
    def validate_order(self, order_data: OrderData) -> None:
        """Validate order data."""
        # ... (validation logic)
    
    def calculate_pricing(self, order_data: OrderData) -> Pricing:
        """Calculate order pricing."""
        # ... (pricing logic)
```

### 2. Large Classes (> 200 lines)
```python
# ❌ BAD - God object
class UserManager:
    def create_user(self): pass
    def update_user(self): pass
    def delete_user(self): pass
    def authenticate_user(self): pass
    # ... 50 more methods

# ✅ GOOD - Single responsibility
class UserRepository:
    """Handle user data persistence."""
    # ... (persistence methods)

class AuthService:
    """Handle authentication."""
    # ... (authentication methods)
```

### 3. Feature Envy
```python
# ❌ BAD - Method uses another class's data excessively
class OrderCalculator:
    def calculate_total(self, customer: Customer) -> float:
        # ... (logic that should be in the Customer class)

# ✅ GOOD - Move logic to the appropriate class
class Customer:
    def calculate_order_total(self) -> float:
        """Calculate total for customer's order."""
        # ... (logic now lives in the Customer class)
```

### 4. Primitive Obsession
```python
# ❌ BAD - Using primitives for everything
def create_user(email: str, phone: str, age: int, country: str) -> dict:
    # ... (manual validation)

# ✅ GOOD - Use value objects
from pydantic import BaseModel, EmailStr

class UserData(BaseModel):
    email: EmailStr
    # ... (other value objects)
```

## 🔀 Git & Version Control
### Git Best Practices
```gitignore
# .gitignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.env.local
.env.*.local

# Testing
.coverage
htmlcov/
.pytest_cache/
.mypy_cache/

# Logs
*.log
logs/

# Database
*.db
*.sqlite3

# OS
.DS_Store
Thumbs.db
```

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```
**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Test additions or corrections
- `build`: Build system changes
- `ci`: CI configuration changes
- `chore`: Routine tasks, maintenance
- `security`: Security improvements

**Example**:
```
feat(auth): implement JWT refresh token rotation

- Add refresh token rotation for enhanced security
- Invalidate old refresh tokens after use
- Add configurable refresh token expiry

Closes #123
```

### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-json
      - id: check-merge-conflict
      - id: check-toml
      - id: debug-statements
      - id: mixed-line-ending

  - repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.290
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.1
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

## 📊 Monitoring & Logging
### Structured Logging
```python
import logging
import json
from datetime import datetime
from typing import Any, Dict
import structlog

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

class LoggingMiddleware:
    """Logging middleware for FastAPI."""
    
    async def __call__(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        
        # Log request
        logger.info(
            "request_started",
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            client_host=request.client.host
        )
        
        start_time = time.time()
        
        try:
            response = await call_next(request)
            
            # Log response
            logger.info(
                "request_completed",
                request_id=request_id,
                status_code=response.status_code,
                duration=time.time() - start_time
            )
            
            return response
        except Exception as e:
            logger.exception(
                "request_failed",
                request_id=request_id,
                error=str(e),
                duration=time.time() - start_time
            )
            raise
```

### Health Checks
```python
from enum import Enum
from typing import Dict, Any

class HealthStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"

@app.get("/health")
async def health_check() -> Dict[str, Any]:
    """Comprehensive health check."""
    checks = {
        "database": await check_database(),
        "redis": await check_redis(),
        "external_api": await check_external_api()
    }
    
    overall_status = HealthStatus.HEALTHY
    for check in checks.values():
        if check["status"] == HealthStatus.UNHEALTHY:
            overall_status = HealthStatus.UNHEALTHY
            break
        elif check["status"] == HealthStatus.DEGRADED:
            overall_status = HealthStatus.DEGRADED
    
    return {
        "status": overall_status.value,
        "timestamp": datetime.utcnow().isoformat(),
        "checks": checks
    }

async def check_database() -> Dict[str, Any]:
    """Check database connectivity."""
    try:
        async with get_db() as db:
            await db.execute("SELECT 1")
        return {"status": HealthStatus.HEALTHY.value}
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        return {
            "status": HealthStatus.UNHEALTHY.value,
            "error": str(e)
        }
```

## ✅ Code Review Checklist
### Before Submitting Code

#### Security
- [ ] No hardcoded secrets or credentials
- [ ] All user inputs are validated and sanitized
- [ ] SQL queries use parameterization
- [ ] Authentication and authorization properly implemented
- [ ] Sensitive data is encrypted
- [ ] Error messages don't leak sensitive information

#### Code Quality
- [ ] Functions are < 20 lines
- [ ] Classes follow single responsibility principle
- [ ] No duplicate code (DRY principle)
- [ ] Clear, descriptive variable and function names
- [ ] Complex logic has comments explaining why
- [ ] No commented-out code

#### Testing
- [ ] Unit tests for all new functions
- [ ] Integration tests for API endpoints
- [ ] Edge cases are tested
- [ ] Test coverage > 80%
- [ ] All tests pass

#### Documentation
- [ ] All functions have docstrings
- [ ] README updated if needed
- [ ] API documentation updated
- [ ] Journal entry created
- [ ] Complex algorithms explained

#### Performance
- [ ] No N+1 query problems
- [ ] Appropriate use of caching
- [ ] Large datasets use pagination
- [ ] Async used for I/O operations
- [ ] Database queries are optimized

#### Best Practices
- [ ] Type hints for all functions
- [ ] Error handling is comprehensive
- [ ] Logging added for important operations
- [ ] Code formatted with Black
- [ ] Linting passes (Ruff/Flake8)
- [ ] Type checking passes (mypy)

## 🎓 Continuous Learning
### Regular Reviews
- **Daily**: Review journal entries from today
- **Weekly**: Consolidate common problems
- **Monthly**: Update success patterns
- **Quarterly**: Refactor based on lessons learned

### Knowledge Base Maintenance
```python
# scripts/analyze_journal.py
"""Analyze development journal for insights."""

import re
from collections import Counter
from pathlib import Path

def analyze_journal():
    """Analyze journal for patterns."""
    journal_path = Path("docs/DEVELOPMENT_JOURNAL.md")
    content = journal_path.read_text()
    
    # Extract problems
    problems = re.findall(r'\*\*Problem\*\*: (.+)', content)
    problem_counts = Counter(problems)
    
    # Extract resolution times
    times = re.findall(r'\*\*Time to Resolve\*\*: (.+)', content)
    
    # Generate report
    print("## Journal Analysis Report")
    print(f"\nTotal Entries: {content.count('Entry #')}")
    print(f"\nTop 5 Problems:")
    for problem, count in problem_counts.most_common(5):
        print(f"  - {problem}: {count} occurrences")
    
    print(f"\nAverage Resolution Time: {calculate_average_time(times)}")

if __name__ == "__main__":
    analyze_journal()
```

## 🚀 Quick Reference
### Essential Commands
```bash
# Development setup
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
pre-commit install

# Code quality
black src/ tests/
ruff check src/ tests/ --fix
mypy src/

# Testing
pytest
pytest --cov=src --cov-report=html
pytest -v -s tests/unit/  # Verbose with print statements

# Database
alembic upgrade head  # Apply migrations
alembic revision --autogenerate -m "Description"  # Create migration

# Running
uvicorn src.main:app --reload --port 8000
```

## 🎯 Remember
- Write code for humans first, computers second
- Make it work, make it right, make it fast (in that order)
- When in doubt, choose readability over cleverness
- Document why, not what
- Test behavior, not implementation
- Fail fast, fail clearly
- Every line of code is a liability