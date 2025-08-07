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

## Import Errors
### Circular Imports
```python
# ❌ Problem Pattern
# a.py
from b import b_func
def a_func():
    b_func()

# b.py
from a import a_func
def b_func():
    a_func()

# ✅ Solution Pattern
# Refactor dependencies, use local imports, or use dependency injection.
# a.py
import b
def a_func():
    b.b_func()

# b.py
# No import from a needed if logic is restructured.
def b_func():
    # ...
    pass
```

## Type Errors
### NoneType Errors
```python
# ❌ Problem Pattern
def get_user(user_id):
    user = db.find(user_id) # Might return None
    return user.name # Raises AttributeError if user is None

# ✅ Solution Pattern
def get_user(user_id):
    user = db.find(user_id)
    if user is None:
        raise ValueError("User not found")
    return user.name