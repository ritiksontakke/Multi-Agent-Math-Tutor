# 🧮 Multi-Agent Math Tutor

A Multi-Agent Math Tutor built with **FastAPI**, **LangChain**, and **LLM-powered agents**. This project demonstrates the **Supervisor–Subagent Architecture**, where multiple AI agents collaborate to solve mathematical problems.

---

## 🚀 Features

* Multi-Agent Architecture
* Supervisor Agent Orchestration
* Reasoning Agent
* Calculator Agent
* Reviewer Agent
* FastAPI REST API
* Structured JSON Responses
* LangChain Integration
* Easy to Extend

---

## 🏗️ Architecture

```text
User
 │
 ▼
Main Agent (Supervisor)
 │
 ├── Reasoning Agent
 │
 ├── Calculator Agent
 │
 └── Reviewer Agent
 │
 ▼
Final Response
```

### Agent Responsibilities

#### Reasoning Agent

* Understands the math problem
* Extracts values
* Identifies the operation

#### Calculator Agent

* Performs calculations
* Returns numerical results

#### Reviewer Agent

* Verifies calculations
* Validates final answers

#### Main Agent (Supervisor)

* Coordinates all agents
* Controls workflow
* Combines outputs

---

## 📂 Project Structure

```text
Multi-Agent-Math-Tutor/
│
├── src/
│   ├── agents/
│   │   ├── main_agent.py
│   │   ├── reasoning_agent.py
│   │   ├── calculator_agent.py
│   │   └── reviewer_agent.py
│   │
│   ├── tools/
│   │   └── subagent_tools.py
│   │
│   ├── config/
│   │   └── llm.py
│   │
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Multi-Agent-Math-Tutor.git

cd Multi-Agent-Math-Tutor
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Linux / Mac

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Application

```bash
python -m uvicorn src.main:app --reload
```

Application runs at:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST /solve

#### Request

```json
{
  "question": "Calculate compound interest on ₹10000 for 3 years at 8%"
}
```

#### Response

```json
{
  "reasoning_agent": {
    "operation": "compound_interest",
    "principal": 10000,
    "rate": 8,
    "time": 3
  },
  "calculator_agent": {
    "amount": 12597.12,
    "compound_interest": 2597.12
  },
  "reviewer_agent": {
    "status": "verified",
    "final_answer": 12597.12
  }
}
```

---

## 🧠 Workflow

```text
Question
   │
   ▼
Reasoning Agent
   │
   ▼
Calculator Agent
   │
   ▼
Reviewer Agent
   │
   ▼
Final Verified Answer
```

---

## 📚 Learning Objectives

This project demonstrates:

* Multi-Agent Systems
* LangChain Agents
* Supervisor Pattern
* Agent Orchestration
* Context Isolation
* FastAPI Integration
* Structured AI Workflows

---

## 🔮 Future Improvements

* Support additional math operations
* LangGraph integration
* Agent
