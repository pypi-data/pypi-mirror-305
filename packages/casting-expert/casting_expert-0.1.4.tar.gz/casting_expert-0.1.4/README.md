# Casting Expert

A comprehensive Python package for type casting, string-to-dictionary conversion, and data validation with advanced features like type inference, serialization, and schema validation.

## 🌟 Features

- **String to Dictionary Conversion**
  - Multiple format support (JSON, Query String, Key-Value, YAML-like)
  - Auto-format detection
  - Nested structure support

- **Type Inference**
  - Automatic type detection and conversion
  - Support for common data types (int, float, bool, datetime)
  - List parsing (comma-separated values)
  - Nested type inference

- **Data Serialization**
  - Convert dictionaries to various string formats
  - Pretty printing options
  - Customizable delimiters and formatting

- **Advanced Validation**
  - Nested schema validation
  - Custom error messages
  - Type checking
  - Pattern matching
  - Range validation
  - Length constraints
  - Custom validators
  - Field transformations
  - Conditional validation

## 📦 Installation

```bash
pip install casting-expert
```

## 🚀 Quick Start

### Basic Usage

```python
from casting_expert import parse_string_to_dict

# Auto-detect format and convert
data = parse_string_to_dict('{"name": "John", "age": 30}')
```

### Type Inference

```python
from casting_expert import TypeInference

# Infer types for single values
value1 = TypeInference.infer_type("123")         # Returns int(123)
value2 = TypeInference.infer_type("true")        # Returns bool(True)
value3 = TypeInference.infer_type("2024-01-01")  # Returns datetime object
value4 = TypeInference.infer_type("1.23")        # Returns float(1.23)
value5 = TypeInference.infer_type("a,b,c")       # Returns ["a", "b", "c"]

# Infer types for entire dictionary
data = {
    "id": "123",
    "active": "true",
    "score": "98.6",
    "tags": "python,coding,dev"
}

typed_data = TypeInference.infer_types_in_dict(data)
# Result:
# {
#     "id": 123,
#     "active": True,
#     "score": 98.6,
#     "tags": ["python", "coding", "dev"]
# }
```

### Serialization

```python
from casting_expert import DictSerializer

data = {
    "name": "John",
    "age": 30,
    "scores": [95, 87, 91]
}

# Convert to different formats
json_str = DictSerializer.to_json(data, pretty=True)
# {
#     "name": "John",
#     "age": 30,
#     "scores": [95, 87, 91]
# }

query_str = DictSerializer.to_query_string(data, prefix='?')
# ?name=John&age=30&scores=[95,87,91]

kv_str = DictSerializer.to_key_value(data, delimiter=': ')
# name: John
# age: 30
# scores: [95, 87, 91]

yaml_str = DictSerializer.to_yaml_like(data)
# name: John
# age: 30
# scores: 
#   - 95
#   - 87
#   - 91
```

### Validation

#### Basic Validation

```python
from casting_expert import DictValidator

# Create validation schema
schema = {
    "name": DictValidator.create_field(
        str,
        required=True,
        min_length=2,
        pattern=r'^[A-Za-z\s]+$',
        error_messages={
            "pattern": "Name should contain only letters and spaces",
            "required": "Name is required"
        }
    ),
    "age": DictValidator.create_field(
        int,
        min_value=0,
        max_value=150,
        error_messages={
            "min_value": "Age cannot be negative",
            "max_value": "Age cannot be greater than 150"
        }
    ),
    "email": DictValidator.create_field(
        str,
        required=True,
        pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$',
        error_messages={"pattern": "Invalid email format"}
    )
}

# Validate data
data = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com"
}

result = DictValidator.validate(data, schema)
if result.is_valid:
    print("Validation passed!")
else:
    for issue in result.issues:
        print(f"{issue.severity}: {issue.field} - {issue.message}")
```

#### Nested Validation

```python
# Create nested schema
address_schema = {
    "street": DictValidator.create_field(
        str,
        required=True,
        min_length=5,
        error_messages={"min_length": "Street name is too short"}
    ),
    "city": DictValidator.create_field(
        str,
        required=True,
        choices=["New York", "Los Angeles", "Chicago"]
    ),
    "zip_code": DictValidator.create_field(
        str,
        pattern=r'^\d{5}(-\d{4})?$',
        error_messages={"pattern": "Invalid ZIP code format"}
    )
}

# Main schema with nested address
schema = {
    "name": DictValidator.create_field(str, required=True),
    "address": DictValidator.create_field(
        dict,
        required=True,
        schema=address_schema
    )
}

# Validate nested data
data = {
    "name": "John Doe",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip_code": "12345"
    }
}

result = DictValidator.validate(data, schema)
```

#### Custom Validators and Transformations

```python
# Custom validator
def validate_domain(email: str) -> bool:
    return not email.endswith(('.temp', '.test'))

email_field = DictValidator.create_field(
    str,
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
).add_validator(
    validate_domain,
    "Temporary email domains are not allowed"
)

# Transform before validation
username_field = DictValidator.create_field(
    str
).add_transform(
    lambda x: x.lower().strip()
)

# Combined schema
schema = {
    "email": email_field,
    "username": username_field
}
```

## 🧪 Testing

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## 📝 Common Use Cases

### 1. Form Data Processing

```python
from casting_expert import parse_string_to_dict, TypeInference, DictValidator

# Process form data
form_data = "name=John+Doe&age=30&email=john@example.com"
data = parse_string_to_dict(form_data, format='query')
typed_data = TypeInference.infer_types_in_dict(data)

# Validate
schema = {
    "name": DictValidator.create_field(str, required=True),
    "age": DictValidator.create_field(int, min_value=0),
    "email": DictValidator.create_field(str, pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
}

result = DictValidator.validate(typed_data, schema)
```

### 2. Configuration File Processing

```python
# Process YAML-like config
config_str = """
database:
  host: localhost
  port: 5432
  username: admin
settings:
  debug: true
  max_connections: 100
"""

config = parse_string_to_dict(config_str, format='yaml_like')
typed_config = TypeInference.infer_types_in_dict(config)
```

### 3. API Response Validation

```python
# Define API response schema
response_schema = {
    "status": DictValidator.create_field(
        str,
        choices=["success", "error"]
    ),
    "data": DictValidator.create_field(
        dict,
        nullable=True,
        schema={
            "id": DictValidator.create_field(int, required=True),
            "name": DictValidator.create_field(str, required=True)
        }
    ),
    "message": DictValidator.create_field(str, required=True)
}

# Validate API response
response_data = {
    "status": "success",
    "data": {
        "id": 123,
        "name": "John"
    },
    "message": "Data retrieved successfully"
}

result = DictValidator.validate(response_data, response_schema)
```

## 📄 License

MIT License - feel free to use this package in your projects.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📬 Contact

- Issue Tracker: [GitHub Issues](https://github.com/ahmednizami/casting-expert/issues)
- Source Code: [GitHub](https://github.com/ahmednizami/casting-expert)