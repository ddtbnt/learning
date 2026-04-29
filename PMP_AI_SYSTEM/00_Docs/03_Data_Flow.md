# 00_DOCS/03_Data_Flow.md
# PMP_AI_SYSTEM – Luồng dữ liệu end-to-end

---

## 1. Mục tiêu của tài liệu

Tài liệu này mô tả toàn bộ **luồng dữ liệu (Data Flow)** trong hệ thống PMP_AI_SYSTEM từ lúc nhập dữ liệu thô → xử lý bằng AI → tạo Knowledge Base → phục vụ Web App.

Mục tiêu chính:

- Hiểu dữ liệu đi như thế nào trong hệ thống
- Biết điểm nào có AI, điểm nào không có AI
- Kiểm soát toàn bộ pipeline từ đầu đến cuối
- Đảm bảo hệ thống chạy đúng kiến trúc enterprise

---

## 2. Nguyên tắc thiết kế dữ liệu

### 2.1 Dữ liệu luôn đi một chiều

Không có vòng lặp dữ liệu tự do ngoài kiểm soát.

RAW → PROCESS → KNOWLEDGE → APPLICATION

---

### 2.2 Không có xử lý rời rạc

Tất cả xử lý đều phải đi qua:

06_AI_WORKFLOW_ENGINE (LangGraph)

---

### 2.3 STATE là trung tâm dữ liệu

Mọi dữ liệu đều được chứa trong STATE:

- Không truyền file lung tung giữa modules
- Không xử lý ngoài pipeline
- Không bypass engine

---

## 3. Tổng luồng dữ liệu hệ thống

PMP_AI_SYSTEM xử lý theo 4 tầng:

RAW DATA
↓
AI PROCESSING LAYER
↓
KNOWLEDGE BASE
↓
APPLICATION LAYER

---

## 4. Luồng dữ liệu chi tiết end-to-end

### 4.1 Giai đoạn 1 – INPUT DATA (RAW LAYER)

Nguồn dữ liệu:

PMP/
├── 0_MASTER_MINDMAP/
├── 1_COURSES/
└── question.txt

---

Dữ liệu gồm:

- Course content (markdown)
- Mindmap logic (PMP structure)
- Question bank (JSON / text)

---

## 4.2 Giai đoạn 2 – AI PROCESSING (LangGraph Engine)

ENTRY POINT:

02_Content_Standardization/run_pipeline.py

---

### LUỒNG XỬ LÝ:

RAW DATA
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

---

## 4.3 Vai trò dữ liệu trong từng node

### Loader Node

INPUT:
- file_path

OUTPUT:
- raw_content

---

### Analyzer Node

INPUT:
- raw_content

OUTPUT:
- analysis_result

Chức năng:
- Detect structure
- Detect missing knowledge
- Detect duplicate content

---

### Standardization Node (AI)

INPUT:
- raw_content

OUTPUT:
- standardized_content

AI xử lý:

- format lại markdown
- chuẩn hóa kiến thức
- chuyển EN → EN/VI

---

### Enrichment Node (AI)

INPUT:
- standardized_content

OUTPUT:
- enriched_content

AI xử lý:

- bổ sung PMI knowledge
- giải thích sâu concept
- thêm ví dụ thực tế

---

### Mapping Node

INPUT:
- enriched_content

OUTPUT:
- mapped_concepts

Chức năng:

- Course → Concept Library
- Question → Knowledge mapping
- PMI domain tagging

---

### Validation Node

INPUT:
- mapped_concepts

OUTPUT:
- validation_status

Logic:

- PASS → sang Writer
- FAIL → quay lại node trước

---

### Writer Node

INPUT:
- validated data

OUTPUT:
- Knowledge Base (file system)

---

## 4.4 Giai đoạn 3 – KNOWLEDGE BASE LAYER

OUTPUT SYSTEM:

PMP_KNOWLEDGE_BASE/

├── 2_CONCEPTS_LIBRARY/
├── 3_PMI_MINDSET/
├── 4_EXAM_PRACTICE/
└── 5_REVISION/

---

Đặc điểm:

- dữ liệu đã chuẩn hóa
- không còn raw content
- có structure học rõ ràng
- có thể dùng trực tiếp cho Web App

---

## 4.5 Giai đoạn 4 – QUESTION ENGINE FLOW

03_Question_Generation/

INPUT:
- 2_CONCEPTS_LIBRARY
- question.txt mapping result

PROCESS:

Question Mapper
↓
Difficulty Classifier
↓
Exam Builder
↓
Explanation Generator (EN/VI)

OUTPUT:

- Mock Exam
- Practice Questions
- Answer Explanation

---

## 4.6 Giai đoạn 5 – WEB APPLICATION FLOW

04_Web_App/

### Learning Module

INPUT:
- 2_CONCEPTS_LIBRARY
- 3_PMI_MINDSET

FLOW:

User Request
↓
API Backend
↓
Read Knowledge Base
↓
Render UI

---

### Exam Module

INPUT:
- 4_EXAM_PRACTICE

FLOW:

User Start Exam
↓
Random Question Picker
↓
Load from Knowledge Base
↓
User Answer
↓
Score + Analysis

---

## 4.7 Giai đoạn 6 – ADMIN AI FLOW

ADMIN PIPELINE:

02_Content_Standardization
03_Question_Generation

2 MODE:

### MODE 1 – OFFLINE BATCH
- chạy full pipeline
- generate toàn bộ knowledge

### MODE 2 – INCREMENTAL UPDATE
- update từng course
- enrich lại concept
- regenerate question

---

## 5. Tổng sơ đồ dữ liệu hệ thống

PMP RAW DATA
│
├── Course Files
├── Mindmap
├── Question Bank
│
↓
06_AI_WORKFLOW_ENGINE (LangGraph)
│
├── Loader
├── Analyzer
├── Standardization (AI)
├── Enrichment (AI)
├── Mapping
├── Validation
├── Writer
│
↓
PMP_KNOWLEDGE_BASE
│
├── Concept Library
├── PMI Mindset
├── Exam Practice
└── Revision
│
↓
04_Web_App
│
├── Learning Module
└── Exam Module

---

## 6. Quy tắc luồng dữ liệu

### 6.1 Không có data đi ngược

Knowledge Base không quay lại RAW.

---

### 6.2 AI chỉ dùng trong pipeline

AI chỉ xuất hiện tại:

- Standardization Node
- Enrichment Node
- Question Generator

---

### 6.3 Web App không chạy AI nặng

Web App chỉ:

- đọc dữ liệu
- hiển thị dữ liệu
- không xử lý AI nặng

---

### 6.4 Admin là người kích hoạt AI

AI không tự chạy.

Admin trigger pipeline.

---

## 7. Tư duy hệ thống dữ liệu

Hệ thống không phải:

- chatbot
- generator text
- prompt system

Mà là:

STATEFUL DATA PIPELINE SYSTEM

---

## 8. Kết luận

Luồng dữ liệu PMP_AI_SYSTEM được thiết kế theo chuẩn:

RAW → AI ENGINE → KNOWLEDGE → APPLICATION

Với các đặc điểm:

- Có kiểm soát (controlled flow)
- Có trạng thái (stateful)
- Có phân tầng rõ ràng
- Có thể mở rộng production system

---