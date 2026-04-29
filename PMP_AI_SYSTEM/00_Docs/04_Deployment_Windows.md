# 00_DOCS/04_Deployment_Windows.md
# PMP_AI_SYSTEM – Triển khai hệ thống local trên Windows

---

## 1. Mục tiêu của tài liệu

Tài liệu này hướng dẫn cách deploy toàn bộ PMP_AI_SYSTEM trên Windows local, bao gồm:

- AI Workflow Engine (LangGraph)
- Ollama + Qwen3.5
- Pipeline xử lý dữ liệu PMP
- Web App (backend + frontend)
- Knowledge Base runtime

---

## 2. Kiến trúc deploy trên Windows

Hệ thống chạy theo mô hình local full-stack:

WINDOWS MACHINE
│
├── Docker Desktop
├── Ollama Server (Qwen3.5)
├── Python (LangGraph Engine)
├── NodeJS (Web Frontend)
│
├── PMP_AI_SYSTEM
│   ├── 06_AI_WORKFLOW_ENGINE
│   ├── 02_Content_Standardization
│   ├── 03_Question_Generation
│   ├── 04_Web_App
│   └── 05_Deployment
│
└── PMP_KNOWLEDGE_BASE

---

## 3. Nguyên tắc deploy hệ thống

### 3.1 Local-first architecture

- Không cần cloud
- Không cần Kubernetes
- Không cần server ngoài

---

### 3.2 AI chạy tách biệt Web

- AI chạy trong pipeline (LangGraph)
- Web App chỉ đọc dữ liệu
- Không gọi LLM trực tiếp từ UI

---

### 3.3 Deployment = kết nối các layer

Deploy không phải upload server  
mà là:

- chạy AI engine
- chạy web app
- kết nối data flow

---

## 4. Chuẩn bị trước khi deploy

### 4.1 Cài bắt buộc

- Docker Desktop
- Python 3.10+
- NodeJS 18+
- Ollama

---

### 4.2 Load AI model

ollama pull qwen3.5

Kiểm tra:

ollama list

---

## 5. Deploy AI Workflow Engine

### 5.1 Start Ollama service

ollama serve

---

### 5.2 Run LangGraph Engine

Vào thư mục:

06_AI_WORKFLOW_ENGINE/

Chạy:

python engine/graph_runtime.py

---

### 5.3 Kiểm tra engine hoạt động

Output mong đợi:

- Node execution log
- STATE update
- No error in pipeline

---

## 6. Deploy Content Pipeline (ADMIN MODE)

### 6.1 Chạy chuẩn hóa dữ liệu

02_Content_Standardization/pipeline/run_pipeline.py

Chức năng:

- Convert RAW → Knowledge Base
- Generate Concept Library
- Enrich PMI content

---

### 6.2 Sinh hệ thống câu hỏi

03_Question_Generation/pipeline/generate_exam.py

Output:

- Exam questions
- Answer explanation
- Difficulty classification

---

## 7. Deploy Web App (Windows local)

### 7.1 Backend

Vào:

04_Web_App/backend

Chạy:

python app.py

Backend sẽ:

- đọc Knowledge Base
- expose API cho frontend

---

### 7.2 Frontend

Vào:

04_Web_App/frontend

Cài dependencies:

npm install

Chạy:

npm run dev

---

## 8. Kết nối hệ thống

Luồng kết nối:

Web App
↓
Backend API
↓
Knowledge Base (file system)
↓
AI Engine (only for admin pipeline)

---

## 9. Deploy Knowledge Base

PMP_KNOWLEDGE_BASE/
│
├── 2_CONCEPTS_LIBRARY/
├── 3_PMI_MINDSET/
├── 4_EXAM_PRACTICE/
└── 5_REVISION/

Web App sẽ đọc trực tiếp thư mục này

---

## 10. Run full system

Step 1:
ollama serve

Step 2:
python 06_AI_WORKFLOW_ENGINE/engine/graph_runtime.py

Step 3:
02_Content_Standardization/pipeline/run_pipeline.py

Step 4:
04_Web_App/backend/app.py

Step 5:
04_Web_App/frontend
npm run dev

---

## 11. Monitoring hệ thống

06_AI_WORKFLOW_ENGINE/logs/
02_Content_Standardization/logs/
03_Question_Generation/logs/

---

## 12. Troubleshooting

Ollama:
ollama serve

Model:
ollama pull qwen3.5

LangGraph:
pip install --upgrade langgraph

---

## 13. Kiến trúc deploy

RAW DATA
↓
AI ENGINE (LangGraph + Qwen3.5)
↓
KNOWLEDGE BASE
↓
WEB BACKEND
↓
WEB FRONTEND
↓
USER

---

## 14. Nguyên tắc deploy

- Không cloud dependency
- AI tách khỏi UI
- Data-first system

---

## 15. Mở rộng

- Docker hóa system
- Deploy VPS / Cloud
- Multi-course system
- AI Tutor realtime

---

## 16. Kết luận

✔ chạy 100% local  
✔ không phụ thuộc cloud  
✔ AI pipeline tách biệt UI  
✔ Knowledge Base là trung tâm  
✔ dễ nâng cấp production