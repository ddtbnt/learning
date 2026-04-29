# PMP_AI_SYSTEM (LangGraph AI Learning Platform)

## 1. Problem Statement

Hiện tại hệ thống có dữ liệu thô PMP gồm:

```diagram
PMP/
├── 0_MASTER_MINDMAP/
│   └── PMP_MASTER_MINDMAP.md
│
├── 1_COURSES/
│   ├── Course_1_Principles.md
│   ├── Course_2_People.md
│   ├── Course_3_Process.md
│   └── Course_4_Business.md
│
├── question.txt (JSON question bank)
```

### Vấn đề hiện tại

Dữ liệu này:

- Không chuẩn hóa cấu trúc học tập
- Không có phân lớp kiến thức theo PMI domain
- Course dạng thô, chưa tách concept
- Question bank chưa gắn mapping vào knowledge
- Chưa có format phục vụ Web App học + thi thử
- Không thể dùng trực tiếp cho AI tutor

---

## 2. Goal of the System

Chuyển toàn bộ dữ liệu thô thành AI-ready knowledge system để phục vụ:

### Web App 2 modules:

1. Learning Module
- Học PMP song ngữ EN / VI
- Theo concept-based structure
- Theo PMI domains

2. Exam Module
- Sinh đề thi ngẫu nhiên
- Mô phỏng format PMP exam
- Phân tích lỗi + pattern sai

---

## 3. Target Knowledge Architecture (OUTPUT)

Sau khi xử lý bằng AI pipeline, hệ thống tạo ra:

```diagram
PMP_KNOWLEDGE_BASE/
├── 2_CONCEPTS_LIBRARY/
│   ├── 01_Fundamentals/
│   ├── 02_People/
│   ├── 03_Process/
│   ├── 04_Agile_Hybrid/
│   └── 05_Business/
│
├── 3_PMI_MINDSET/
│   ├── PMI_CORE_RULES.md
│   └── DECISION_FRAMEWORK.md
│
├── 4_EXAM_PRACTICE/
│   ├── Situations.md
│   ├── Mistakes_Log.md
│   ├── Patterns.md
│   └── Mock_Analysis.md
│
└── 5_REVISION/
    ├── Cheat_Sheet.md
    ├── Flashcards.md
    └── Last_Week_Review.md
```
---

## 4. Core Architecture

### High-level system design

PMP_RAW_DATA
        ↓
LangGraph AI Pipeline
        ↓
Qwen3.5 (LLM Processing Layer)
        ↓
Stateful Workflow Engine
        ↓
Knowledge Transformation Layer
        ↓
PMP_KNOWLEDGE_BASE
        ↓
Web App (Learning + Exam System)

---

## 5. AI Processing Engine (LangGraph)

Hệ thống KHÔNG dùng prompt đơn lẻ.

Thay vào đó dùng:

STATEFUL GRAPH PIPELINE

### Pipeline Flow

```diagram
Loader Node
    ↓
Analyzer Node
    ↓
Standardization Node (Qwen3.5)
    ↓
Enrichment Node (Qwen3.5)
    ↓
Mapping Node (Course → Concept Library)
    ↓
Question Mapping Node (question.txt → knowledge)
    ↓
Validation Node
    ↓
Writer Node
```
---

## 6. Input Data Sources

### 1. Course Data

- Course_1_Principles.md
- Course_2_People.md
- Course_3_Process.md
- Course_4_Business.md

### 2. Mindmap

- PMP_MASTER_MINDMAP.md

### 3. Question Bank

- question.txt (JSON format)

---

## 7. Output Transformation Rules

### Courses → Concepts

- 1 Course KHÔNG còn là file học
- Chuyển thành Concept-based structure

Ví dụ:

Course 3_Process →
- Risk Management
- Schedule Management
- Quality Management
- Procurement Management

---

### Questions → Knowledge-linked data

Mỗi question sẽ:

- map vào concept
- map vào PMI domain
- gắn difficulty level
- gắn explanation EN + VI

---

## 8. LangGraph Execution Model

### State Model

STATE = {
  file_path,
  raw_content,
  extracted_concepts,
  standardized_markdown,
  enriched_markdown,
  question_mapping,
  validation_status,
  output_path
}

---

## 9. Node Responsibilities

### Loader Node
Load raw markdown + JSON

### Analyzer Node
Detect:
- duplicate content
- missing concepts
- weak structure

### Standardization Node (Qwen3.5)
- Clean content
- Normalize structure
- Convert EN → EN + VI

### Enrichment Node (Qwen3.5)
- Add PMI explanations
- Add missing concepts

### Mapping Node
- Map Course → Concept Library
- Map Questions → Concepts

### Validation Node
- Check structure correctness
- Ensure PMI alignment

### Writer Node
- Write to Knowledge Base
- Auto create folder structure

---

## 10. Local Development (Windows Test Mode)

### Flow

1. Run Ollama
2. Load Qwen3.5
3. Run LangGraph pipeline
4. Process local files
5. Output markdown into Knowledge Base

### Result

- No cloud required
- Fully local AI pipeline
- File-based processing system

---

## 11. Web App Target Architecture

### Module 1: Learning System

- Read 2_CONCEPTS_LIBRARY
- Show EN + VI explanation
- Navigate by PMI domain

### Module 2: Exam System

- Random question generator
- Pull from mapped question bank
- Simulate PMP exam format
- Score + analysis

---

## 12. System Philosophy

This system is NOT:

- prompt-based chatbot
- static markdown generator
- manual content processing

This system IS:

STATEFUL AI LEARNING ENGINE

Powered by:

- LangGraph (workflow orchestration)
- Qwen3.5 (local LLM)
- Knowledge graph structure (concept mapping)
- File-based memory system

---

## 13. Deployment Strategy

### Phase 1 (Local Windows)
- Docker + Ollama + LangGraph
- Process data locally

### Phase 2 (Internal Server)
- Deploy API backend
- Add Web App UI

### Phase 3 (Production Scale)
- Multi-course expansion
- Adaptive exam system
- AI tutor engine

---

## 14. Final Goal

Transform:

RAW PMP FILES

INTO:

AI POWERED PMP LEARNING PLATFORM

with:

- structured knowledge base
- exam engine
- AI tutoring system
- scalable workflow architecture

---

END OF SYSTEM

# 15. Project Execution Overview (How to Use This System)

PMP_AI_SYSTEM được thiết kế như một **AI Learning Platform Engine (Enterprise Workflow System)**, không phải một ứng dụng học thông thường.

Hệ thống mô phỏng cách một AI platform thực tế được xây dựng trong doanh nghiệp:

- Tách rõ DESIGN / ENGINE / PIPELINE / APPLICATION / DEPLOYMENT
- Có AI Workflow Engine (LangGraph) làm lõi xử lý
- Có Knowledge Base làm dữ liệu học
- Có Web App làm lớp người dùng
- Có cơ chế ADMIN để mở rộng dữ liệu bằng AI

---

## 15.1 Kiến trúc hệ thống và lý do tổ chức

### Cấu trúc tổng thể dự án

PMP_AI_SYSTEM  
│  
├── 00_DOCS/ → SYSTEM DESIGN (CHỈ THIẾT KẾ – KHÔNG RUN CODE)  
├── 01_Setup/ → ENVIRONMENT BOOTSTRAP (cài đặt hệ thống)  
├── 02_Content_Standardization/ → AI PIPELINE 1 (RAW → KNOWLEDGE)  
├── 03_Question_Generation/ → AI PIPELINE 2 (KNOWLEDGE → EXAM SYSTEM)  
├── 04_Web_App/ → USER APPLICATION LAYER (HỌC + THI)  
├── 05_Deployment/ → PRODUCTION DEPLOYMENT LAYER  
├── 06_AI_WORKFLOW_ENGINE/ → CORE ENGINE (LangGraph HEART SYSTEM)  

---

### Mục tiêu của kiến trúc này

Hệ thống được tách thành nhiều lớp để đảm bảo:

- Tách biệt rõ giữa thiết kế và vận hành thực tế
- AI pipeline có thể debug từng bước (step-by-step)
- Dễ mở rộng thêm course (PMP → AWS → Scrum…)
- Kiểm soát luồng dữ liệu AI có cấu trúc
- Có khả năng chuyển sang production system thực tế

---

## 15.2 Tư duy hệ thống (System Thinking)

Hệ thống không hoạt động theo kiểu “chatbot” hay “prompt generator”.

Mà theo mô hình:

PMP RAW DATA  
↓  
LANGGRAPH AI ENGINE (STATEFUL WORKFLOW)  
↓  
STRUCTURED KNOWLEDGE BASE  
↓  
WEB APPLICATION (LEARNING + EXAM)

---

### Ý nghĩa quan trọng

- Không học từ file thô  
- Không dùng prompt đơn lẻ  
- Không xử lý rời rạc từng file  

👉 Tất cả phải đi qua AI Workflow Engine

---

## 15.3 Mô hình vận hành USER vs ADMIN

### USER (Người học)

USER chỉ làm 1 việc:

→ Học từ Knowledge Base đã được AI xử lý sẵn

Dữ liệu USER sử dụng:

- 2_CONCEPTS_LIBRARY/
- 3_PMI_MINDSET/
- 4_EXAM_PRACTICE/
- 5_REVISION/

👉 USER KHÔNG chạy AI  
👉 USER KHÔNG gọi LLM  
👉 USER chỉ học + làm bài + luyện đề

---

### ADMIN (Người quản trị)

ADMIN có quyền:

- Import dữ liệu mới (Course, Question, Mindmap)
- Làm giàu nội dung học
- Chạy AI pipeline để update Knowledge Base
- Sinh lại câu hỏi / concept / explanation

ADMIN sử dụng AI trong 2 pipeline:

- 02_Content_Standardization
- 03_Question_Generation

👉 Đây là OFFLINE AI PROCESSING (không chạy realtime cho user)

---

## 15.4 Cách sử dụng hệ thống từ đầu đến cuối

### Bước 1 — Cài môi trường

01_Setup/

- Docker
- Ollama
- Qwen3.5
- Python runtime

👉 mục tiêu: tạo local AI environment

---

### Bước 2 — Hiểu kiến trúc hệ thống

00_DOCS/00_Architecture.md

File này giải thích:

- Toàn bộ kiến trúc system
- Luồng dữ liệu end-to-end
- Vai trò từng module
- Cách LangGraph vận hành
- Cách dữ liệu đi từ RAW → KNOWLEDGE → WEB

👉 BẮT BUỘC đọc trước khi chạy system

---

### Bước 3 — Khởi tạo AI Engine (CORE)

06_AI_WORKFLOW_ENGINE/

Đây là “bộ não hệ thống”

Chức năng:

- Điều phối LangGraph
- Quản lý STATE
- Gọi LLM (Qwen3.5 qua Ollama)
- Quản lý node execution
- Retry / failure handling
- Tool system (file read/write)

---

### Bước 4 — Xử lý dữ liệu học (ADMIN PIPELINE – HYBRID MODE)

02_Content_Standardization/

Đây là giai đoạn quan trọng nhất của hệ thống, vì nó biến dữ liệu thô thành Knowledge Base có cấu trúc phục vụ Web App + Exam System.

Hệ thống hỗ trợ 2 chế độ vận hành theo vòng đời phát triển:

---

#### 4.1 Giai đoạn 1 — OFFLINE AI PIPELINE (KHỞI TẠO HỆ THỐNG)

👉 Dùng khi hệ thống mới build, chưa có Web Admin

Input:

- Course files
- Mindmap
- question.txt

Cách vận hành:

ADMIN chạy pipeline thủ công bằng local system:

- run_pipeline.py (LangGraph execution)
- Qwen3.5 (qua Ollama local)
- Xử lý theo từng node:
  Loader → Analyzer → Standardization → Enrichment → Mapping → Writer

Output:

PMP_KNOWLEDGE_BASE/  
├── 2_CONCEPTS_LIBRARY/  
├── 3_PMI_MINDSET/  
├── 4_EXAM_PRACTICE/  
├── 5_REVISION/  

👉 Đây là SYSTEM BOOTSTRAP PHASE

---

#### 4.2 Giai đoạn 2 — ADMIN AI TOOL (WEB-BASED ENRICHMENT)

👉 Sau khi hệ thống ổn định và có Web App

ADMIN không còn chạy script thủ công nữa.

Thay vào đó dùng Web Admin để điều khiển AI pipeline.

Chức năng:

- Upload Course / Question / Mindmap
- Standardize nội dung
- Enrich kiến thức PMI
- Mapping concept + question
- Regenerate nội dung
- Preview trước khi publish
- Publish vào Knowledge Base

Backend:

- Gọi 06_AI_WORKFLOW_ENGINE
- LangGraph runtime execution
- Qwen3.5 inference (Ollama on-demand)
- Update Knowledge Base realtime

---

#### 4.3 Output hệ thống (GIỮ NGUYÊN)

Dù chạy offline hay web admin, output luôn chuẩn hóa:

PMP_KNOWLEDGE_BASE/

- 2_CONCEPTS_LIBRARY/ → kiến thức học chính
- 3_PMI_MINDSET/ → tư duy PMP
- 4_EXAM_PRACTICE/ → case + pattern + sai lầm
- 5_REVISION/ → học nhanh + ôn tập

---

### 4.4 Tư duy cốt lõi

Hệ thống không phụ thuộc vào cách chạy AI.

Mà theo nguyên tắc:

RAW DATA  
→ AI WORKFLOW ENGINE  
→ KNOWLEDGE BASE  
→ WEB APPLICATION  

---

### 4.5 Kết luận bước 4

Pipeline này được thiết kế để:

- Khởi tạo hệ thống bằng offline AI pipeline
- Sau đó chuyển sang web admin để mở rộng dữ liệu
- Giữ một logic AI duy nhất (LangGraph core)

👉 Nghĩa là:

1 AI Engine  
1 Knowledge Base  
2 chế độ vận hành:
- Offline batch (bootstrap)
- Web admin (production enrichment)

---

## 15.5 Luồng dữ liệu hệ thống

00_DOCS → DESIGN ONLY  
01_Setup → ENVIRONMENT  
06_ENGINE → AI ORCHESTRATION  
02_PIPELINE → KNOWLEDGE GENERATION  
03_EXAM → QUESTION SYSTEM  
04_WEB_APP → USER INTERFACE  
05_DEPLOY → PRODUCTION SYSTEM  

---

## 15.6 Tư duy vận hành hệ thống

Hệ thống hoạt động theo nguyên tắc:

“Tất cả dữ liệu học phải được chuẩn hóa qua AI Workflow Engine trước khi đến người dùng”

Không có:

- xử lý thủ công trong Web App
- prompt trực tiếp từ user
- logic rời rạc từng file

Thay vào đó:

STATEFUL AI PIPELINE (LangGraph-based system)

---

## 15.7 Vai trò kiến trúc tổng thể

Hệ thống gồm 3 lớp:

### 1. Design Layer
→ 00_DOCS  
→ chỉ thiết kế hệ thống  

### 2. AI Processing Layer
→ 02 + 03 + 06  
→ biến dữ liệu thành knowledge  

### 3. Application Layer
→ 04 + 05  
→ phục vụ người dùng học và thi  

---

## 15.8 Tài liệu kiến trúc chi tiết

👉 00_DOCS/00_Architecture.md

File này mô tả:

- LangGraph design chi tiết
- Node system architecture
- STATE schema chuẩn
- Data flow production
- Strategy mở rộng multi-course system

---

## 15.9 Kết luận

PMP_AI_SYSTEM không phải:

- chatbot
- tool tạo câu hỏi
- markdown generator

Mà là:

AI Learning Platform Engine có kiến trúc enterprise hoàn chỉnh

bao gồm:

- Workflow AI (LangGraph)
- Knowledge Base system
- Exam engine
- Web learning platform
- Admin AI pipeline
- Production deployment architecture