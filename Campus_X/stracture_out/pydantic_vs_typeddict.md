# Pydantic vs. TypedDict Guide

When handling structured data in Python—especially when extracting structured outputs from LLMs with **LangChain**—you will frequently choose between **`TypedDict`** and **Pydantic (`BaseModel`)**.

This document breaks down why they exist, how they work under the hood, and when to use each.

---

## 1. The Core Problem: Why Not Just Plain `dict`?

A standard Python dictionary offers zero schema enforcement:

```python
student = {"name": "Muneeb", "age": "twenty", "corse": "AI"}
```

- **Typos in Keys:** `"corse"` instead of `"course"` fails silently until accessed.
- **No Type Safety:** `"age": "twenty"` is accepted even though you expect an integer.
- **No IDE Autocomplete:** Your editor cannot suggest available keys or types.
- **Missing Fields:** A dictionary can be missing required keys without raising any immediate error.

---

## 2. What is `TypedDict`?

`TypedDict` is built into Python's standard library (`typing` module) starting in Python 3.8.

### Example

```python
from typing import TypedDict

class StudentDict(TypedDict):
    name: str
    age: int
    course: str

# Creating an instance:
student: StudentDict = {
    "name": "Muneeb",
    "age": 19,
    "course": "AI"
}

print(type(student))  # Output: <class 'dict'>
```

### Key Characteristics

- **Design-Time Type Hints:** Primarily intended for static type checkers (mypy, Pyright) and editor autocomplete.
- **Zero Runtime Validation:** At runtime, `student` is **just a standard Python `dict`**.
- **No Type Coercion:** If you pass `"age": "19"` or `"age": "invalid"`, Python will not convert it, check it, or throw a runtime error.
- **Zero Overhead:** Because it is just a dictionary, it adds almost no runtime performance cost.

---

## 3. What is Pydantic (`BaseModel`)?

Pydantic is a data validation and parsing library built on Python type annotations.

### Example

```python
from pydantic import BaseModel, ValidationError, field_validator

class Student(BaseModel):
    name: str
    age: int
    course: str

    @field_validator("age")
    @classmethod
    def validate_age(cls, value: int) -> int:
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        return value

# 1. Automatic Type Coercion (string "19" -> int 19)
student = Student(name="Muneeb", age="19", course="AI")
print(student.age)        # 19 (an integer!)
print(type(student))      # <class '__main__.Student'>

# 2. Dot-notation Access
print(student.name)       # "Muneeb"

# 3. Strict Runtime Validation
try:
    invalid_student = Student(name="Muneeb", age="nineteen", course="AI")
except ValidationError as e:
    print("Caught validation error at runtime:\n", e)
```

### Key Capabilities

1. **Runtime Validation:** Enforces types and constraints when the code runs.
2. **Data Coercion / Parsing:** Intelligently casts compatible inputs (e.g., string `"19"` or `"true"` to `19` and `True`).
3. **Custom Validators:** Powerful `@field_validator` and `@model_validator` methods to enforce complex domain logic.
4. **Object-Oriented Access:** Dot notation (`student.name`) instead of dictionary keys (`student["name"]`).
5. **Serialization:** Built-in export helpers such as `.model_dump()` (to dict) and `.model_dump_json()` (to JSON string).

---

## 4. Head-to-Head Comparison

| Feature | `TypedDict` | Pydantic (`BaseModel`) |
| :--- | :--- | :--- |
| **Origin** | Built-in standard library (`typing`) | Third-party library (`pydantic`) |
| **Runtime Type** | Standard Python `dict` (`<class 'dict'>`) | Custom instance (`<class '...'>`) |
| **Runtime Validation** | ❌ No | ✅ Yes (raises `ValidationError`) |
| **Type Coercion** | ❌ No | ✅ Yes (converts compatible types) |
| **Access Syntax** | `student["name"]` | `student.name` |
| **Custom Validation Logic** | ❌ None | ✅ `@field_validator`, regex, constraints |
| **Nested Models** | TypedDict within TypedDict (static only) | Fully validated recursive models |
| **Performance** | Extremely fast (raw dict) | Slight overhead for validation parsing |

---

## 5. Usage in LangChain (Structured Outputs)

In LangChain, LLMs can return guaranteed schema formats via `.with_structured_output()`:

### Option A: Using `TypedDict` (Lightweight)

```python
from typing import TypedDict
from langchain_openai import ChatOpenAI

class AnswerSchema(TypedDict):
    summary: str
    confidence_score: float

llm = ChatOpenAI(model="gpt-4o-mini")
structured_llm = llm.with_structured_output(AnswerSchema)

response = structured_llm.invoke("Explain black holes in one sentence.")
# response is a standard dict: {"summary": "...", "confidence_score": 0.95}
```

### Option B: Using Pydantic (Strict & Robust)

```python
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class AnswerSchema(BaseModel):
    summary: str = Field(description="One-sentence summary of the topic")
    confidence_score: float = Field(ge=0.0, le=1.0, description="Score between 0 and 1")

llm = ChatOpenAI(model="gpt-4o-mini")
structured_llm = llm.with_structured_output(AnswerSchema)

response = structured_llm.invoke("Explain black holes in one sentence.")
# response is an AnswerSchema object: response.summary, response.confidence_score
```

---

## 6. Decision Rule of Thumb

- **Pick `TypedDict` when:**
  - You only want simple dictionaries for internal processing.
  - You do not need runtime validation or custom error handling.
  - You want zero external dependencies and maximum speed.

- **Pick `Pydantic` when:**
  - You parse data coming from untrusted or unpredictable sources (like **LLM outputs**, API requests, or user inputs).
  - You need automatic data conversion (e.g. strings into integers or datetimes).
  - You need business rules enforced via validators (e.g., regex, numerical ranges).
  - You want clean dot-notation access and easy JSON export.
