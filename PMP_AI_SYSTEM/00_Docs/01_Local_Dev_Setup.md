# 00_DOCS/01_Local_Dev_Setup.md
# PMP_AI_SYSTEM – Hướng dẫn chạy hệ thống local (Windows / Linux)

---

## 1. Mục tiêu của tài liệu

Tài liệu này hướng dẫn cách cài đặt và chạy toàn bộ hệ thống **PMP_AI_SYSTEM** trên máy local.

Sau khi hoàn thành, bạn sẽ có:

- Môi trường AI chạy offline
- Ollama + Qwen3.5 hoạt động local
- LangGraph AI Workflow Engine chạy được
- Pipeline xử lý PMP hoạt động end-to-end
- Knowledge Base được sinh tự động

---

## 2. Kiến trúc môi trường local

PMP_AI_SYSTEM chạy hoàn toàn local theo mô hình:

LOCAL MACHINE
│
├── Docker Engine
├── Python Runtime (LangGraph)
├── Ollama Server
│     └── Qwen3.5 Model
│
├── PMP_AI_SYSTEM Codebase
│     ├── 06_AI_WORKFLOW_ENGINE
│     ├── 02_Content_Standardization
│     ├── 03_Question_Generation
│     └── 04_Web_App
│
└── Knowledge Base Output
      ├── 2_CONCEPTS_LIBRARY
      ├── 3_PMI_MINDSET
      ├── 4_EXAM_PRACTICE
      └── 5_REVISION

---

## 3. Yêu cầu hệ thống

### 3.1 Phần cứng

- RAM: tối thiểu 16GB (khuyến nghị 32GB)
- CPU: 4 cores trở lên
- SSD: tối thiểu 20GB trống

---

### 3.2 Phần mềm bắt buộc

- Windows 10/11 hoặc Linux
- Docker Desktop
- Python 3.10+
- Git
- Ollama

---

## 4. Cài đặt môi trường

---

## 4.1 Cài Docker

Windows:
- Cài Docker Desktop
- Bật WSL2 backend

Kiểm tra:

docker --version

---

## 4.2 Cài Python

Khuyến nghị Python 3.10+

Kiểm tra:

python --version

---

## 4.3 Cài Ollama

Tải tại:
https://ollama.com/download

Kiểm tra:

ollama --version

---

## 4.4 Load model Qwen3.5

Tải model:

ollama pull qwen3.5

Kiểm tra:

ollama list

---

## 5. Cài đặt project PMP_AI_SYSTEM

Clone source code:

git clone <repo-url>
cd PMP_AI_SYSTEM

---

## 6. Cài dependencies Python

Cài thư viện:

pip install langgraph
pip install pyyaml
pip install requests
pip install tqdm

Hoặc:

pip install -r requirements.txt

---

## 7. Kiểm tra hệ thống (VERIFY ENV)

Chạy:

python 01_Setup/verify_env.py

Kết quả mong đợi:

- Python OK
- Ollama OK
- Qwen3.5 OK
- LangGraph OK

---

## 8. Cấu hình AI Engine

File:

06_AI_WORKFLOW_ENGINE/config/engine_config.yaml

Ví dụ:

llm:
  provider: ollama
  model: qwen3.5
  base_url: http://localhost:11434

---

## 9. Chạy AI Pipeline lần đầu

Vào module:

02_Content_Standardization/

Chạy:

python pipeline/run_pipeline.py

---

## 10. Luồng chạy hệ thống local

RAW PMP DATA
↓
Loader Node
↓
Analyzer Node
↓
Standardization Node (Qwen3.5)
↓
Enrichment Node (Qwen3.5)
↓
Mapping Node
↓
Validation Node
↓
Writer Node
↓
PMP_KNOWLEDGE_BASE

---

## 11. Output sau khi chạy thành công

PMP_KNOWLEDGE_BASE/
│
├── 2_CONCEPTS_LIBRARY/
├── 3_PMI_MINDSET/
├── 4_EXAM_PRACTICE/
└── 5_REVISION/

---

## 12. Kiểm tra kết quả

Concept:

ls PMP_KNOWLEDGE_BASE/2_CONCEPTS_LIBRARY/

Exam:

ls PMP_KNOWLEDGE_BASE/4_EXAM_PRACTICE/

---

## 13. Chạy AI Engine độc lập

python 06_AI_WORKFLOW_ENGINE/engine/graph_runtime.py

---

## 14. Chạy Web App (sau khi có dữ liệu)

Backend:

cd 04_Web_App
python backend/app.py

Frontend:

npm install
npm run dev

---

## 15. Debug hệ thống

Logs pipeline:

02_Content_Standardization/logs/

Logs engine:

06_AI_WORKFLOW_ENGINE/logs/

---

## 16. Lỗi thường gặp

### 16.1 Ollama không chạy

ollama serve

---

### 16.2 Chưa có model

ollama pull qwen3.5

---

### 16.3 Lỗi LangGraph

pip install --upgrade langgraph

---

## 17. Nguyên tắc chạy hệ thống

Thứ tự chuẩn:

1. Setup environment
2. Start Ollama
3. Load model
4. Run pipeline
5. Generate knowledge base
6. (Optional) Run Web App

---

## 18. Kết luận

Sau khi setup thành công:

✔ AI chạy local hoàn chỉnh  
✔ LangGraph pipeline hoạt động  
✔ Qwen3.5 xử lý PMP data  
✔ Knowledge Base tự động sinh  
✔ Sẵn sàng build Web App + Exam System  

---