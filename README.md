# AI-Powered Enterprise Assistant

A simple AI-powered enterprise assistant built using **FastAPI** and **Ollama (Llama3)**. The assistant processes natural language queries and performs business actions through tool calling. Currently, it supports ticket creation with request validation and robust error handling.

---

# Features

- FastAPI REST API
- Natural language understanding using Ollama (Llama3)
- Tool calling architecture
- Ticket creation workflow
- Request validation
- Error handling and fallback logic
- JSON response parsing
- Global exception handling
- Logging support
- Unit tests
- Modular code structure
- Mock data support

---

# Tech Stack

- Python 3.11+
- FastAPI
- Ollama (Llama3)
- Pydantic
- Requests
- Uvicorn
- Pytest

---

# Architecture

The application follows a layered architecture. User requests are validated and routed through a tool router service. The LLM determines the intent and either invokes a business tool or returns a general answer.

```text
                       User
                         │
                         ▼
                  POST /ask Endpoint
                         │
                         ▼
                 FastAPI Application
                         │
                         ▼
                 Request Validation
                         │
                         ▼
                  Tool Router Service
                         │
                         ▼
                    Ollama (Llama3)
                         │
                         ▼
               Structured JSON Response
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
     create_ticket                general_query
          │                             │
          ▼                             ▼
  create_ticket_tool()            Generate Answer
          │                             │
          ▼                             ▼
     ticket_service()              JSON Response
          │
          ▼
      JSON Response
```

---

# Request Flow

```text
User Question
      │
      ▼
POST /ask
      │
      ▼
Request Validation
      │
      ▼
Tool Router Service
      │
      ▼
Ollama (Llama3)
      │
      ▼
JSON Output
      │
      ├──────────── Ticket Intent
      │                    │
      │                    ▼
      │            create_ticket_tool()
      │                    │
      │                    ▼
      │              ticket_service()
      │
      └──────────── General Query
                           │
                           ▼
                     Generate Answer
                           │
                           ▼
                      Return JSON
```

---

# Business Action

## Create Ticket

The assistant creates support tickets based on user requests.

### Example

### Request

```json
{
  "question": "Create a ticket for printer issue"
}
```

### Response

```json
{
  "status": true,
  "message": "Ticket created successfully.",
  "data": {
    "ticket_id": "TKT1001",
    "issue": "printer issue",
    "status": "OPEN"
  }
}
```

---

# Engineering Improvements

## 1. Tool Calling

Instead of relying on hardcoded keyword matching, the application uses Ollama to determine the user's intent and invoke the appropriate business tool.

### Flow

```text
Question
   │
   ▼
Ollama
   │
   ▼
Structured JSON
{
    "intent": "create_ticket",
    "issue": "printer issue"
}
   │
   ▼
create_ticket_tool()
   │
   ▼
ticket_service()
   │
   ▼
Generate Ticket ID
   │
   ▼
Return JSON Response
```

---

## 2. Error Handling and Fallback Logic

Implemented:

- Empty request validation
- Missing issue validation
- Timeout handling
- JSON parsing fallback
- Global exception handling
- Standard response format
- Logging support

---

# Project Structure

```text
enterprise_assistant/
│
├── venv/
│
├── app/
│   ├── main.py
│   │
│   ├── constants/
│   │     └── constants.py
│   │
│   ├── exceptions/
│   │     └── global_exception_handler.py
│   │
│   ├── models/
│   │     ├── request_model.py
│   │     └── response_model.py
│   │
│   ├── routes/
│   │     └── ask_route.py
│   │
│   ├── services/
│   │     ├── llm_service.py
│   │     ├── tool_router_service.py
│   │     └── ticket_service.py
│   │
│   ├── tools/
│   │     └── create_ticket_tool.py
│   │
│   ├── utils/
│   │     ├── validators.py
│   │     ├── error_handler.py
│   │     ├── json_parser.py
│   │     └── logger.py
│   │
│   └── tests/
│         ├── test_ask_api.py
│         ├── test_ticket_service.py
│         └── test_tool_router.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>
cd enterprise_assistant
```

---

# Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Verify installation:

```bash
ollama --version
```

Pull model:

```bash
ollama pull llama3
```

Start Ollama server:

```bash
ollama serve
```

Verify models:

```bash
ollama list
```

---

# Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server URL:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# API Endpoint

## POST /ask

### Request

```json
{
  "question": "Create a ticket for email issue"
}
```

### Response

```json
{
  "status": true,
  "message": "Ticket created successfully.",
  "data": {
    "ticket_id": "TKT1001",
    "issue": "email issue",
    "status": "OPEN"
  }
}
```

---

# Test Cases

## Test Case 1: Normal Business Query

### Request

```json
{
  "question": "Create a ticket for printer not working"
}
```

### Response

```json
{
  "status": true,
  "message": "Ticket created successfully.",
  "data": {
    "ticket_id": "TKT1001"
  }
}
```

---

## Test Case 2: Challenging Query

### Request

```json
{
  "question": "Create ticket"
}
```

### Response

```json
{
  "status": false,
  "message": "Please provide issue details.",
  "data": null
}
```

---

# Error Handling Examples

## Empty Input

### Request

```json
{
  "question": ""
}
```

### Response

```json
{
  "status": false,
  "message": "Question cannot be empty",
  "data": null
}
```

---

## Unsupported Query

### Request

```json
{
  "question": "Increase my salary"
}
```

### Response

```json
{
  "status": false,
  "message": "Unable to process the request.",
  "data": null
}
```

---

# Unit Tests

Run:

```bash
pytest -v
```

Test files:

```text
test_ticket_service.py
test_tool_router.py
test_ask_api.py
```

Expected Output:

```text
============================= test session starts =============================

app/tests/test_ticket_service.py::test_create_ticket PASSED
app/tests/test_tool_router.py::test_process_question PASSED
app/tests/test_ask_api.py::test_ask_endpoint PASSED

============================= 3 passed =============================
```

---

# Future Enhancements

- Conversation Memory
- Retrieval Augmented Generation (RAG)
- Database Integration
- Docker Support
- LangChain Integration
- LangGraph Integration
- Authentication and Authorization
- Multiple Business Workflows

---

# Evaluation Criteria Covered

- ✅ Functionality
- ✅ Code Quality
- ✅ Problem Solving Approach
- ✅ AI Workflow Design
- ✅ API Design
- ✅ Tool Calling
- ✅ Error Handling and Fallback Logic
- ✅ Unit Testing
- ✅ End-to-End Working Demo

---

# Author

**Priyanka Gupta**

Python Developer | AI Enthusiast | FastAPI | Ollama | REST APIs