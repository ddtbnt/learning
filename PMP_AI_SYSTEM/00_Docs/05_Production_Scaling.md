# 00_DOCS/05_Production_Scaling.md
# PMP_AI_SYSTEM – Chiến lược scale hệ thống (Production Scaling)

---

## 1. Mục tiêu của tài liệu

Tài liệu này mô tả cách mở rộng PMP_AI_SYSTEM từ **local AI system** thành một **AI Learning Platform có khả năng scale production**, bao gồm:

- Scale AI Workflow Engine (LangGraph)
- Scale Knowledge Base
- Scale Web App traffic
- Tối ưu chi phí AI inference
- Hỗ trợ multi-course (PMP → AWS → Scrum → TOGAF)

---

## 2. Nguyên tắc scale hệ thống

### 2.1 Giữ kiến trúc 3 lớp cốt lõi

Hệ thống luôn giữ nguyên 3 lớp:

AI LAYER (LangGraph + LLM)
↓
DATA LAYER (Knowledge Base file system)
↓
APPLICATION LAYER (Web App)

---

### 2.2 Không scale UI trước, scale AI trước

Sai hướng:
- scale frontend trước ❌

Đúng hướng:
- scale AI pipeline trước ✔
- scale data structure trước ✔

---

### 2.3 Stateless Web App

Web App:
- không chứa AI logic
- không giữ state quan trọng
- chỉ đọc Knowledge Base + gọi API

---

## 3. Kiến trúc scale tổng thể

Giai đoạn production:

CLIENT
↓
LOAD BALANCER
↓
WEB BACKEND (API CLUSTER)
↓
AI WORKFLOW ENGINE CLUSTER
↓
LLM SERVING LAYER (Ollama / vLLM / GPU server)
↓
KNOWLEDGE BASE STORAGE LAYER

---

## 4. Scale AI Workflow Engine (LangGraph)

### 4.1 Giai đoạn 1 – Single Node (Local)

- 1 máy chạy toàn bộ pipeline
- Ollama chạy local
- LangGraph single instance

---

### 4.2 Giai đoạn 2 – Multi Worker AI Engine

Tách engine thành:

- Node Runner Service
- State Manager Service
- LLM Client Service

Mô hình:

REQUEST
↓
QUEUE
↓
WORKER 1 / 2 / 3
↓
STATE STORE

---

### 4.3 Giai đoạn 3 – Distributed AI Pipeline

LangGraph execution:

- chia node theo service
- mỗi node chạy độc lập
- giao tiếp qua message queue

Ví dụ:

Loader Service
Analyzer Service
Enrichment Service
Mapping Service
Writer Service

---

## 5. Scale Knowledge Base

### 5.1 Giai đoạn file-based (hiện tại)

PMP_KNOWLEDGE_BASE/
├── markdown files
├── json mapping

✔ dễ debug
✔ dễ phát triển

---

### 5.2 Giai đoạn hybrid storage

Kết hợp:

- File system (source of truth)
- Vector DB (search layer)

Ví dụ:

- ChromaDB
- FAISS
- Weaviate

---

### 5.3 Giai đoạn production knowledge graph

Chuyển sang:

- Concept Graph
- Relation Graph
- Question Graph

Mỗi node:

- Concept
- Skill
- Question
- Explanation

---

## 6. Scale Web App

### 6.1 Giai đoạn local

- NodeJS frontend
- Python backend
- đọc file trực tiếp

---

### 6.2 Giai đoạn API-based

Web App không đọc file trực tiếp nữa

Thay vào:

Frontend
↓
Backend API
↓
Knowledge Service

---

### 6.3 Giai đoạn microservices UI

Tách Web App:

- Learning Service
- Exam Service
- Admin Service

---

## 7. Scale LLM Layer

### 7.1 Local Ollama (giai đoạn đầu)

- Qwen3.5 local
- CPU inference

---

### 7.2 GPU inference server

Chuyển sang:

- vLLM server
- GPU cluster
- batching request

---

### 7.3 Multi-model system

Dùng nhiều model:

- Qwen (reasoning)
- LLaMA (general)
- Mistral (fast tasks)

Routing:

LLM Router
→ chọn model theo task

---

## 8. Scale dữ liệu (Data Growth Strategy)

### 8.1 Input scale

- thêm course mới
- thêm question bank
- thêm domain mới

---

### 8.2 Output scale

- Concept Library mở rộng
- Exam bank tăng dần
- PMI Mindset versioning

---

### 8.3 Versioning system

PMP_KNOWLEDGE_BASE/
├── v1/
├── v2/
├── v3/

---

## 9. Performance Optimization

### 9.1 AI caching

- cache node output
- cache LLM response
- reuse enrichment result

---

### 9.2 Incremental processing

Không chạy full pipeline:

Chỉ chạy:
- changed course
- new question set
- updated concept

---

### 9.3 Batch processing

- process theo batch file
- tránh real-time overload

---

## 10. Scaling strategy theo giai đoạn

### Phase 1 – Local System

- 1 machine
- Ollama local
- LangGraph single instance

---

### Phase 2 – Internal Service

- API backend
- separate AI engine
- multi user support

---

### Phase 3 – Production System

- distributed AI engine
- microservice backend
- vector database
- GPU inference cluster

---

## 11. Bottleneck chính cần scale

### 11.1 AI inference

Giải pháp:
- GPU server
- batching
- model routing

---

### 11.2 State management

Giải pháp:
- Redis state store
- event-driven workflow

---

### 11.3 Knowledge base I/O

Giải pháp:
- cache layer
- index layer
- vector DB

---

## 12. Monitoring hệ thống production

Theo dõi:

- node execution time
- LLM latency
- pipeline success rate
- memory usage per node

Tools:

- Prometheus
- Grafana
- Log aggregation system

---

## 13. Kiến trúc mục tiêu cuối cùng

PMP_AI_SYSTEM khi scale hoàn chỉnh sẽ trở thành:

AI LEARNING PLATFORM ENGINE

bao gồm:

- Distributed LangGraph Engine
- Multi-model LLM system
- Knowledge Graph system
- Exam generation engine
- Web learning platform
- Admin AI pipeline system

---

## 14. Kết luận

Chiến lược scale của hệ thống dựa trên nguyên tắc:

- Scale AI trước UI
- Scale data trước feature
- Scale workflow trước application

Hệ thống không scale theo kiểu truyền thống web app

Mà scale theo mô hình:

STATEFUL AI WORKFLOW PLATFORM