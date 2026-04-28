# 01_Setup (PMP_AI_SYSTEM + LangGraph Runtime Bootstrap - Windows 11)

## Mục tiêu

Khởi tạo môi trường AI local trên Windows 11 sử dụng:

- Docker Desktop (WSL2 backend)
- Ollama (local LLM runtime)
- Qwen3.5
- Python LangGraph AI Engine
- PMP Knowledge Base (file system)

Sau khi hoàn thành:

SYSTEM = FULLY READY FOR AI WORKFLOW EXECUTION

---

## 1. Kiến trúc hệ thống (Windows 11 + Docker Desktop)

Windows 11 Host
        ↓
WSL2 Backend (Docker Desktop)
        ↓
Ollama Container / Service
        ↓
Qwen3.5 Model Runtime
        ↓
Python LangGraph Engine (Host or WSL2)
        ↓
AI Workflow Nodes
        ↓
PMP Knowledge Base (Local Disk)

---

## 2. Yêu cầu hệ thống (Windows 11)

### Bắt buộc

- Windows 11 64-bit
- Virtualization enabled (BIOS)
- WSL2 installed
- Docker Desktop enabled WSL2 backend

### Khuyến nghị

- RAM: 16GB+
- CPU: 6 cores+
- SSD NVMe

---

## 3. Bước 1 — Cài WSL2 (QUAN TRỌNG)

Run PowerShell (Admin):

wsl --install

Check:

wsl -l -v

Expected:

VERSION = 2

---

## 4. Bước 2 — Cài Docker Desktop (Windows 11)

Download:

https://www.docker.com/products/docker-desktop/

Settings bắt buộc:

- Enable WSL2 backend
- Enable integration with Ubuntu (WSL)

Check:

docker --version

---

## 5. Bước 3 — Cài Ollama (Windows)

Download:

https://ollama.com

Check:

ollama --version

Pull model:

ollama pull qwen3.5:9b

Test:

ollama run qwen3.5:9b

---

## 6. Bước 4 — Cài Python AI Engine (Host hoặc WSL2)

Check:

python --version

Install:

pip install langgraph fastapi pydantic

---

## 7. Bước 5 — LangGraph Workflow Engine

Pipeline:

Loader Node → Analyzer Node → Standardization Node → Enrichment Node → Validation Node → File Writer Node

---

## STATE MODEL

STATE = {
  file_path,
  raw_content,
  analysis_result,
  generated_content,
  validation_status,
  output_path,
  retry_count
}

---

## 8. Bước 6 — Knowledge Base Config

PMP_AI_SYSTEM/config/system.json

{
  "knowledge_base_path": "D:/MyProjects/learning/PMP Exam Prep Certification Training Specialization"
}

---

## 9. Bước 7 — Docker Mount (Windows 11 chuẩn)

PowerShell / CMD:

docker run -it `
  -v "D:\MyProjects\learning\PMP Exam Prep Certification Training Specialization:/data" `
  pmp-ai

NOTE:
- dùng \ (Windows)
- hoặc / trong WSL2

---

## 10. Bước 8 — System Verification

docker --version
ollama --version
ollama list
python --version
python -c "import langgraph"

---

## SYSTEM STATUS CHECK

Docker Desktop = READY
WSL2 = READY
Ollama = READY
Qwen3.5 = READY
Python Engine = READY
LangGraph = READY
Knowledge Base = READY

SYSTEM STATUS = FULLY OPERATIONAL

---

## Runtime Architecture

Qwen3.5 (Ollama)
        ↓
LangGraph Workflow Engine
        ↓
State Management Layer
        ↓
File Tool Layer (Read/Write)
        ↓
PMP Knowledge Base

---

## Kết quả sau setup

- AI local chạy trên Windows 11
- Docker Desktop backend ổn định
- LLM runtime ready
- LangGraph workflow engine active
- file-based knowledge system connected

---

## Bước tiếp theo

02_Content_Standardization/

- run LangGraph pipeline
- process PMP markdown files
- build concept library
- generate exam questions

---

## Ghi chú quan trọng

Hệ thống này yêu cầu:

- WSL2 backend (bắt buộc)
- Docker Desktop integration
- Python LangGraph runtime

Nếu thiếu WSL2 → Docker + AI pipeline sẽ không hoạt động đúng