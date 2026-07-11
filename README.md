# Streamlit Simple Chatbot

A lightweight conversational AI application built with **Streamlit**, **LangChain**, and **Groq's Llama 3.1** language model. The project demonstrates how to build a simple chat interface that communicates with a Large Language Model (LLM) while maintaining conversation history during a user session.

> **Note:** This project is intended as a learning module to explore the fundamentals of integrating Large Language Models into a web-based chat application using Streamlit.

---

# Overview

This project provides a minimal implementation of an AI-powered chatbot using Streamlit's chat components and LangChain's Groq integration.

The application allows users to interact with the Llama 3.1 model through a clean web interface. Conversation history is maintained within the current Streamlit session, enabling context-aware interactions throughout the chat.

The project serves as a practical introduction to building conversational AI applications with modern LLM frameworks.

---

# Features

* Interactive chat interface built with Streamlit.
* Integration with Groq's hosted Llama 3.1 language model.
* Conversation history maintained using Streamlit session state.
* System prompt configuration for assistant behavior.
* Deterministic responses using a fixed temperature setting.
* Environment-based API key configuration.

---

# Application Workflow

```text id="qw83nh"
User Message
      │
      ▼
Streamlit Chat Interface
      │
      ▼
Store Conversation History
      │
      ▼
LangChain ChatGroq
      │
      ▼
Groq Llama 3.1 Model
      │
      ▼
AI Response
      │
      ▼
Display in Chat Interface
```

---

# Project Structure

```text id="p7j2mf"
streamlit-simple-chatbot-main/
│
├── chatbot.py           # Main Streamlit application
├── requirements.txt     # Project dependencies
└── env_template.txt     # Environment variable template
```

---

# Technology Stack

| Category               | Technology                  |
| ---------------------- | --------------------------- |
| Programming Language   | Python                      |
| User Interface         | Streamlit                   |
| LLM Framework          | LangChain                   |
| Language Model         | Groq (Llama 3.1 8B Instant) |
| Environment Management | python-dotenv               |

---

# Core Components

## Streamlit Interface

The application uses Streamlit's built-in chat components to create a conversational user experience.

The interface includes:

* Chat message display
* User input field
* Conversation history
* AI response rendering

The application entry point is:

```text id="4dc2ve"
chatbot.py
```

---

## Conversation Management

Conversation history is maintained using Streamlit's session state.

Each user message and assistant response is stored during the active session, allowing previous messages to be included as context for subsequent interactions.

---

## Language Model Integration

The chatbot uses LangChain's **ChatGroq** integration to communicate with Groq's hosted language model.

Configured model:

* **Llama 3.1 8B Instant**

A system prompt initializes the assistant with the role of a helpful AI assistant before processing user messages.

---

## Response Generation

For every user query, the application:

1. Receives the user's message.
2. Appends it to the conversation history.
3. Sends the complete conversation context to the language model.
4. Receives the generated response.
5. Displays the response in the chat interface.
6. Stores the assistant response for future context.

---

# Environment Configuration

The application requires a Groq API key.

Configure the API key using the provided environment template.

```
GROQ_API_KEY=YourAPIKey
```

The application reads this key before communicating with the language model.

---

# Running the Application

Start the Streamlit application.


Once the application launches:

1. Open the Streamlit interface.
2. Enter a message in the chat input.
3. Receive an AI-generated response.
4. Continue the conversation with maintained session history.

---

# Learning Objectives

This project demonstrates the implementation of several foundational Generative AI concepts, including:

* Large Language Model (LLM) integration
* Prompt-based interaction
* Conversational AI
* Streamlit chat interfaces
* LangChain model wrappers
* Session state management
* API-based model inference

It serves as a compact example for understanding how modern chatbot applications are built using hosted language models.

---

# Dependencies

The project depends on the following Python libraries:

* streamlit
* python-dotenv
* langchain-community
* langchain-groq

---

[Insert license information]
```
