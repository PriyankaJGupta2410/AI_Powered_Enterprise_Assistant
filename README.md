# AI-Powered Enterprise Assistant

A simple AI-powered enterprise assistant built using **FastAPI**,
**Ollama (Llama3)** and **PostgreSQL Conversation Memory**. The
assistant processes natural language queries, performs business actions
through tool calling, and maintains conversational context across
requests.

------------------------------------------------------------------------

# Features

-   FastAPI REST API
-   Natural language understanding using Ollama (Llama3)
-   Tool calling architecture
-   Ticket creation workflow
-   Conversation memory using PostgreSQL
-   Request validation
-   Error handling and fallback logic
-   JSON response parsing
-   Global exception handling
-   Logging support
-   Unit tests
-   Modular code structure
-   Mock data support

------------------------------------------------------------------------

# Tech Stack

-   Python 3.11+
-   FastAPI
-   Ollama (Llama3)
-   PostgreSQL
-   psycopg2
-   Pydantic
-   Requests
-   Uvicorn
-   Pytest

------------------------------------------------------------------------

# Architecture

``` text
                          User
                            │
                            ▼
                      POST /ask
                            │
                            ▼
                    Request Validation
                            │
                            ▼
             Load Conversation History (PostgreSQL)
                            │
                            ▼
                  Build Context + Prompt
                            │
                            ▼
                  Tool Router Service
                            │
                            ▼
                     Ollama (Llama3)
                            │
          ┌─────────────────┴─────────────────┐
          ▼                                   ▼
   create_ticket                       general_query
          │                                   │
          ▼                                   ▼
    Ticket Service                    Generate Answer
          │                                   │
          └─────────────────┬─────────────────┘
                            ▼
              Save Conversation Memory
                            │
                            ▼
                     JSON Response
```

------------------------------------------------------------------------

# Request Flow

``` text
User Question
      │
      ▼
POST /ask
      │
      ▼
Validate Request
      │
      ▼
Load Conversation History
      │
      ▼
Build Prompt
      │
      ▼
Ollama (Llama3)
      │
      ▼
Intent Detection
      │
      ├──────────── create_ticket
      │                   │
      │                   ▼
      │          create_ticket_tool()
      │                   │
      │                   ▼
      │           ticket_service()
      │
      └──────────── general_query
                          │
                          ▼
                  Generate Answer
                          │
                          ▼
            Save Conversation History
                          │
                          ▼
                  Return Response
```

------------------------------------------------------------------------

# Business Action

## Create Ticket

**Request**

``` json
{
  "question": "Create a ticket for printer issue"
}
```

**Response**

``` json
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

------------------------------------------------------------------------

# Engineering Improvements

## 1. Tool Calling

The LLM returns structured JSON with an intent (`create_ticket` or
`general_query`). The router invokes the correct business tool based on
that intent instead of relying on keyword matching.

## 2. Conversation Memory

Conversation history is stored in PostgreSQL.

Flow:

``` text
User Question
      │
      ▼
Load Previous Messages
      │
      ▼
Build Context
      │
      ▼
LLM
      │
      ▼
Generate Response
      │
      ▼
Save User Message
      │
      ▼
Save Assistant Response
```

Benefits:

-   Supports follow-up questions
-   Maintains context
-   Improves user experience

## 3. Error Handling

Implemented:

-   Empty request validation
-   Missing issue validation
-   Timeout handling
-   JSON parsing fallback
-   Global exception handling
-   Logging

------------------------------------------------------------------------

# Project Structure

``` text
enterprise_assistant/
│
├── venv/
│
├── app/
│   ├── main.py
│   │
│   ├── constants/
|   |     └── constants.py
|   |
│   ├── database/
│   │     └── db.py
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
│   │     ├── memory_service.py
│   │     ├── ticket_service.py
│   │     └── tool_router_service.py
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
# AI-Powered Enterprise Assistant

A simple AI-powered enterprise assistant built using **FastAPI**,
**Ollama (Llama3)** and **PostgreSQL Conversation Memory**. The
assistant processes natural language queries, performs business actions
through tool calling, and maintains conversational context across
requests.

------------------------------------------------------------------------

# Features

-   FastAPI REST API
-   Natural language understanding using Ollama (Llama3)
-   Tool calling architecture
-   Ticket creation workflow
-   Conversation memory using PostgreSQL
-   Request validation
-   Error handling and fallback logic
-   JSON response parsing
-   Global exception handling
-   Logging support
-   Unit tests
-   Modular code structure
-   Mock data support

------------------------------------------------------------------------

# Tech Stack

-   Python 3.11+
-   FastAPI
-   Ollama (Llama3)
-   PostgreSQL
-   psycopg2
-   Pydantic
-   Requests
-   Uvicorn
-   Pytest

------------------------------------------------------------------------

# Architecture

``` text
                          User
                            │
                            ▼
                      POST /ask
                            │
                            ▼
                    Request Validation
                            │
                            ▼
             Load Conversation History (PostgreSQL)
                            │
                            ▼
                  Build Context + Prompt
                            │
                            ▼
                  Tool Router Service
                            │
                            ▼
                     Ollama (Llama3)
                            │
          ┌─────────────────┴─────────────────┐
          ▼                                   ▼
   create_ticket                       general_query
          │                                   │
          ▼                                   ▼
    Ticket Service                    Generate Answer
          │                                   │
          └─────────────────┬─────────────────┘
                            ▼
              Save Conversation Memory
                            │
                            ▼
                     JSON Response
```

------------------------------------------------------------------------

# Request Flow

``` text
User Question
      │
      ▼
POST /ask
      │
      ▼
Validate Request
      │
      ▼
Load Conversation History
      │
      ▼
Build Prompt
      │
      ▼
Ollama (Llama3)
      │
      ▼
Intent Detection
      │
      ├──────────── create_ticket
      │                   │
      │                   ▼
      │          create_ticket_tool()
      │                   │
      │                   ▼
      │           ticket_service()
      │
      └──────────── general_query
                          │
                          ▼
                  Generate Answer
                          │
                          ▼
            Save Conversation History
                          │
                          ▼
                  Return Response
```

------------------------------------------------------------------------

# Business Action

## Create Ticket

**Request**

``` json
{
  "question": "Create a ticket for printer issue"
}
```

**Response**

``` json
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

------------------------------------------------------------------------

# Engineering Improvements

## 1. Tool Calling

The LLM returns structured JSON with an intent (`create_ticket` or
`general_query`). The router invokes the correct business tool based on
that intent instead of relying on keyword matching.

## 2. Conversation Memory

Conversation history is stored in PostgreSQL.

Flow:

``` text
User Question
      │
      ▼
Load Previous Messages
      │
      ▼
Build Context
      │
      ▼
LLM
      │
      ▼
Generate Response
      │
      ▼
Save User Message
      │
      ▼
Save Assistant Response
```

Benefits:

-   Supports follow-up questions
-   Maintains context
-   Improves user experience

## 3. Error Handling

Implemented:

-   Empty request validation
-   Missing issue validation
-   Timeout handling
-   JSON parsing fallback
-   Global exception handling
-   Logging

------------------------------------------------------------------------

# Project Structure

``` text
enterprise_assistant/
│
├── venv/
│
├── app/
│   ├── main.py
│   │
│   ├── constants/
|   |     └── constants.py
|   |
│   ├── database/
│   │     └── db.py
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
│   │     ├── memory_service.py
│   │     ├── ticket_service.py
│   │     └── tool_router_service.py
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
------------------------------------------------------------------------

# Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=enterprise_assistant
DB_USER=postgres
DB_PASSWORD=your_password
------------------------------------------------------------------------

# PostgreSQL Setup

Create the database.

```sql
CREATE DATABASE enterprise_assistant;
```

Connect to the database.

```sql
\c enterprise_assistant;
```

Create the conversation memory table.

```sql
CREATE TABLE conversation_memory (
    id SERIAL PRIMARY KEY,
    role VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


------------------------------------------------------------------------

# Setup

## Clone Repository


```bash
git clone https://github.com/PriyankaJGupta2410/AI_Powered_Enterprise_Assistant.git
```

```bash
cd AI_Powered_Enterprise_Assistant
```

## Create Virtual Environment

``` bash
python -m venv venv
```

Windows

``` bash
venv\Scripts\activate
```

Install dependencies

``` bash
pip install -r requirements.txt
```

Run PostgreSQL and create the conversation_memory table.

##Install Ollama:

``` bash
ollama pull llama3
```

Start Ollama

```bash
ollama serve
```

Run API:

``` bash
uvicorn app.main:app --reload
```

Swagger:

`http://localhost:8000/docs`

------------------------------------------------------------------------

# API

## POST /ask

``` json
{
  "question":"Create a ticket for email issue"
}
```

------------------------------------------------------------------------

# Test Cases

### Business Action

``` json
{
  "question":"Create a ticket for printer not working"
}
```

Expected: Ticket created.

### Conversation Memory

Request 1

``` json
{
  "question":"What is FastAPI?"
}
```

Request 2

``` json
{
  "question":"Can you summarize my previous question?"
}
```

Expected: Assistant summarizes the previous question using stored
conversation.

### Business Memory

Request 1

``` json
{
  "question":"Create a ticket for printer not working"
}
```

Request 2

``` json
{
  "question":"What issue did I report?"
}
```

Expected: Assistant answers using conversation history without creating
another ticket.

### Validation

``` json
{
  "question":""
}
```

Expected: Question cannot be empty.

------------------------------------------------------------------------

# Unit Tests

``` bash
pytest -v
```

------------------------------------------------------------------------

# Future Enhancements

- Retrieval Augmented Generation (RAG)
- Docker Support
- LangChain Integration
- LangGraph Workflows
- Authentication & Authorization
- Multi-user Conversation Sessions
- Redis Memory Cache
- Memory Summarization
- Additional Business Actions (Employee Lookup, Report Generation)
------------------------------------------------------------------------

# Evaluation Criteria Covered

-   ✅ Functionality
-   ✅ Code Quality
-   ✅ Problem Solving
-   ✅ AI Workflow Design
-   ✅ API Design
-   ✅ Tool Calling
-   ✅ Conversation Memory
-   ✅ Error Handling
-   ✅ Unit Testing
-   ✅ End-to-End Working Demo

------------------------------------------------------------------------

# Author

**Priyanka Gupta**

Python Developer \| AI Enthusiast \| FastAPI \| Ollama \| REST APIs
------------------------------------------------------------------------

PostgreSQL Setup

Create the database.

CREATE DATABASE enterprise_assistant;

Connect to the database.

\c enterprise_assistant;

Create the conversation memory table.

CREATE TABLE conversation_memory (
    id SERIAL PRIMARY KEY,
    role VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


------------------------------------------------------------------------

# Setup

## Clone Repository

```bash
git clone https://github.com/PriyankaJGupta2410/AI_Powered_Enterprise_Assistant.git

cd enterprise_assistant

``` bash
python -m venv venv
```

Windows

``` bash
venv\Scripts\activate
```

Install dependencies

``` bash
pip install -r requirements.txt
```

Run PostgreSQL and create the conversation_memory table.

Install Ollama:

``` bash
ollama pull llama3
ollama serve
```

Run API:

``` bash
uvicorn app.main:app --reload
```

Swagger:

`http://localhost:8000/docs`

------------------------------------------------------------------------

# API

## POST /ask

``` json
{
  "question":"Create a ticket for email issue"
}
```

------------------------------------------------------------------------

# Test Cases

### Business Action

``` json
{
  "question":"Create a ticket for printer not working"
}
```

Expected: Ticket created.

### Conversation Memory

Request 1

``` json
{
  "question":"What is FastAPI?"
}
```

Request 2

``` json
{
  "question":"Can you summarize my previous question?"
}
```

Expected: Assistant summarizes the previous question using stored
conversation.

### Business Memory

Request 1

``` json
{
  "question":"Create a ticket for printer not working"
}
```

Request 2

``` json
{
  "question":"What issue did I report?"
}
```

Expected: Assistant answers using conversation history without creating
another ticket.

### Validation

``` json
{
  "question":""
}
```

Expected: Question cannot be empty.

------------------------------------------------------------------------

# Unit Tests

``` bash
pytest -v
```

------------------------------------------------------------------------

# Future Enhancements

- Retrieval Augmented Generation (RAG)
- Docker Support
- LangChain Integration
- LangGraph Workflows
- Authentication & Authorization
- Multi-user Conversation Sessions
- Redis Memory Cache
- Memory Summarization
- Additional Business Actions (Employee Lookup, Report Generation)
------------------------------------------------------------------------

# Evaluation Criteria Covered

-   ✅ Functionality
-   ✅ Code Quality
-   ✅ Problem Solving
-   ✅ AI Workflow Design
-   ✅ API Design
-   ✅ Tool Calling
-   ✅ Conversation Memory
-   ✅ Error Handling
-   ✅ Unit Testing
-   ✅ End-to-End Working Demo

------------------------------------------------------------------------

# Author

**Priyanka Gupta**

Python Developer \| AI Enthusiast \| FastAPI \| Ollama \| REST APIs