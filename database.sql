CREATE DATABASE enterprise_assistant;

\c enterprise_assistant;


CREATE TABLE conversation_memory (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    role VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);