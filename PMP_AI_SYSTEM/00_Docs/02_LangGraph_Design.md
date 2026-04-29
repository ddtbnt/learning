# 00_DOCS/02_LangGraph_Design.md
# PMP_AI_SYSTEM – Thiết kế LangGraph Workflow

---

## 1. Mục tiêu của tài liệu

Tài liệu này mô tả cách thiết kế **LangGraph Workflow Engine** trong hệ thống PMP_AI_SYSTEM.

Mục tiêu:

- Biến xử lý AI thành pipeline có trạng thái (stateful)
- Điều phối toàn bộ luồng xử lý PMP
- Kiểm soát từng bước xử lý bằng node
- Hỗ trợ retry / branch / validation
- Chuẩn hóa output thành Knowledge Base

---

## 2. Tư duy thiết kế LangGraph

### 2.1 Không dùng prompt đơn lẻ

Sai cách:

Prompt → AI → Output

Đúng cách:

STATE → NODE → STATE UPDATE → NEXT NODE → FINAL OUTPUT

---

### 2.2 AI theo dạng Graph

Thay vì xử lý tuần tự:

RAW → STEP 1 → STEP 2 → STEP 3

Hệ thống dùng graph:

RAW
│
├── Node A → Node B → Node C
│              ↓
│            Retry / Validate
└── Node D → Output

---

### 2.3 State-driven system

Toàn bộ hệ thống dựa trên STATE:

- Input không thay đổi
- Node chỉ update state
- State là nguồn sự thật duy nhất

---

## 3. Kiến trúc LangGraph trong hệ thống

PMP_AI_SYSTEM dùng 3 lớp chính:

### 3.1 Engine Layer

06_AI_WORKFLOW_ENGINE
- Runtime LangGraph
- State manager
- LLM client (Ollama)
- Retry handler

---

### 3.2 Pipeline Layer

02_Content_Standardization
03_Question_Generation

- Node definitions
- Workflow logic
- Business rules

---

### 3.3 Knowledge Layer

Output:

- Concept Library
- PMI Mindset
- Exam Practice

---

## 4. Tổng quan Workflow Graph

FLOW CHUẨN:

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
↓
KNOWLEDGE BASE

---

## 5. Thiết kế STATE (Core of System)

STATE là trung tâm của toàn bộ graph:

STATE = {
  file_path,
  raw_content,
  detected_type,
  extracted_concepts,
  analysis_result,
  standardized_content,
  enriched_content,
  mapped_concepts,
  validation_status,
  retry_count,
  output_path
}

---

## 6. Thiết kế Node System

Mỗi node là một đơn vị xử lý độc lập.

---

### 6.1 Loader Node

INPUT:
- file_path

OUTPUT:
- raw_content

CHỨC NĂNG:
- Đọc file markdown / json
- Load dữ liệu vào STATE

---

### 6.2 Analyzer Node

INPUT:
- raw_content

OUTPUT:
- analysis_result

CHỨC NĂNG:
- Phân tích cấu trúc dữ liệu
- Detect thiếu nội dung
- Detect duplicate concept

---

### 6.3 Standardization Node (LLM)

INPUT:
- raw_content

LLM:
- Qwen3.5 (Ollama)

OUTPUT:
- standardized_content

CHỨC NĂNG:
- Chuẩn hóa nội dung học
- Chuyển EN → EN/VI
- Format lại markdown

---

### 6.4 Enrichment Node (LLM)

INPUT:
- standardized_content

OUTPUT:
- enriched_content

CHỨC NĂNG:
- Bổ sung PMI knowledge
- Giải thích sâu concept
- Thêm ví dụ thực tế

---

### 6.5 Mapping Node

INPUT:
- enriched_content

OUTPUT:
- mapped_concepts

CHỨC NĂNG:
- Map Course → Concept Library
- Map Question → Concept
- Gắn PMI Domain

---

### 6.6 Validation Node

INPUT:
- mapped_concepts

OUTPUT:
- validation_status

CHỨC NĂNG:
- Kiểm tra format output
- Kiểm tra missing fields
- Quyết định retry hoặc pass

LOGIC:

if invalid → return previous node
if valid → continue

---

### 6.7 Writer Node

INPUT:
- validated content

OUTPUT:
- file system (Knowledge Base)

CHỨC NĂNG:
- Ghi markdown output
- Tạo folder structure
- Persist knowledge base

---

## 7. Retry & Loop Mechanism

LangGraph hỗ trợ vòng lặp:

VALIDATION FAIL
↓
Retry Node (increment counter)
↓
Quay lại Standardization hoặc Enrichment

RULE:

retry_count < MAX_RETRY = 3

---

## 8. Graph Execution Model

EXECUTION FLOW:

1. Load STATE
2. Execute Node
3. Update STATE
4. Validate
5. Decide next node
6. Repeat until complete

---

## 9. Điều phối LLM trong Graph

LLM (Qwen3.5) chỉ được gọi trong:

- Standardization Node
- Enrichment Node

Không dùng LLM ở:

- Loader
- Writer
- Validator

---

## 10. Tool System trong LangGraph

Tool được quản lý bởi:

06_AI_WORKFLOW_ENGINE/tool_registry.py

Tools:

- file_reader
- file_writer
- json_parser
- markdown_builder

---

## 11. Thiết kế mở rộng workflow

Hệ thống có thể mở rộng thêm node:

Ví dụ:

- Summarization Node
- Flashcard Generator Node
- Exam Difficulty Node
- AI Tutor Node

---

## 12. Nguyên tắc thiết kế graph

### 12.1 Deterministic Flow

Không để AI tự quyết định luồng chính

---

### 12.2 Node isolation

Mỗi node chỉ làm 1 việc

---

### 12.3 State as single source of truth

Không truyền dữ liệu ngoài STATE

---

### 12.4 Retry-safe system

Luôn có fallback khi LLM lỗi

---

## 13. Mapping sang hệ thống thực tế

LangGraph = “xương sống hệ thống”

Tương đương:

- Workflow engine (Airflow style)
- ETL pipeline
- AI orchestration layer

---

## 14. Kết nối với Web App

Output graph được dùng bởi:

04_Web_App

- Learning Module
- Exam Module

Không gọi LLM trực tiếp từ Web App

---

## 15. Kết luận

LangGraph trong PMP_AI_SYSTEM là:

Một **stateful AI orchestration engine**

giúp:

- Kiểm soát toàn bộ AI pipeline
- Biến raw data thành knowledge có cấu trúc
- Đảm bảo hệ thống chạy ổn định, có thể debug
- Sẵn sàng scale lên production system

---