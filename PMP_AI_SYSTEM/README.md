# PMP_AI_SYSTEM (LangGraph Architecture)

## Giới thiệu

PMP_AI_SYSTEM là hệ thống AI local dùng để xây dựng nền tảng học PMP chạy nội bộ theo kiến trúc workflow-based AI system.

Hệ thống chuyển từ mô hình “prompt pipeline đơn giản” sang kiến trúc:

AI Workflow Engine + Multi-Agent Processing + State Management

## Công nghệ sử dụng

- Docker Desktop
- Ollama
- Qwen3.5
- Python Backend
- Web Application
- LangGraph Workflow Engine

## Mục tiêu hệ thống

Hệ thống hướng tới xây dựng một nền tảng AI học PMP toàn diện:

- Chuẩn hóa nội dung khóa học PMP
- Loại bỏ nội dung trùng lặp
- Làm giàu kiến thức còn thiếu
- Chuẩn hóa thành markdown học tập
- Sinh flashcards song ngữ
- Sinh câu hỏi luyện tập
- Sinh đề thi thử chuẩn PMI
- Xây dựng AI tutor nội bộ
- Sẵn sàng mở rộng thành hệ thống đào tạo doanh nghiệp

## Kiến trúc tổng thể hệ thống

### Kiến trúc mới (LangGraph-based)

```diagram
PMP_AI_SYSTEM
        ↓
LangGraph Orchestrator
        ↓
┌──────────────────────────────────────────┐
│          AI Workflow Engine              │
│                                          │
│  1. Loader Node                          │
│  2. Analyzer Node                        │
│  3. Standardization Node (Qwen3.5)       │
│  4. Enrichment Node (Qwen3.5)            │
│  5. Validation Node                      │
│  6. File Writer Tool                     │
└──────────────────────────────────────────┘
        ↓
PMP Knowledge Base
```

## Kiến trúc hệ thống tổng thể

### 1. AI System Layer

PMP_AI_SYSTEM đóng vai trò là AI Engine / Workflow System

Chứa:
- LangGraph workflow engine
- Backend API
- Prompt templates
- Tool system (file, folder, validation)
- Docker deployment
- Web interface

👉 Đây là phần “bộ não điều phối”

### 2. Knowledge Base Layer

PMP Exam Prep Certification Training Specialization là dữ liệu tri thức

Chứa:
- Course gốc
- Concept library
- PMI mindset
- Exam practice
- Revision system
- Flashcards

👉 Đây là phần “bộ nhớ dài hạn”

### 3. Kết nối hệ thống

```diagram
AI Engine (LangGraph)
        ↓
Processes files
        ↓
Writes structured markdown
        ↓
Knowledge Base
```

## Kiến trúc LangGraph Workflow Engine

### Vai trò của LangGraph

LangGraph là trung tâm điều phối toàn bộ AI pipeline.

Không còn xử lý tuyến tính, thay vào đó là:

- Graph-based execution
- Stateful processing
- Multi-agent system
- Conditional routing
- Retry logic
- Tool execution layer

## State Management

STATE = {
  file_path,
  raw_content,
  analysis_result,
  markdown_output,
  validation_status,
  output_path
}

## AI Workflow Nodes

### 1. Loader Node
Đọc file markdown từ Knowledge Base
Gắn vào state

Input:
file path

Output:
raw content

### 2. Analyzer Node
Phân tích cấu trúc nội dung
Phát hiện:
- trùng lặp
- thiếu concept
- cấu trúc yếu

Output:
JSON analysis report

### 3. Standardization Node (Qwen3.5)
Chuẩn hóa nội dung học
- Làm sạch text
- Song ngữ hóa (English + Vietnamese)
- Giữ nguyên PMI terminology

Output:
markdown chuẩn học tập

### 4. Enrichment Node (Qwen3.5)
Bổ sung nội dung còn thiếu
- Làm rõ concept PMI
- Thêm ví dụ nếu cần

Output:
markdown nâng cấp

### 5. Validation Node
Kiểm tra output markdown
- Kiểm tra format chuẩn
- Kiểm tra đủ section

Nếu fail:
→ quay lại Standardization Node

### 6. File Writer Tool
Ghi file vào Knowledge Base
- Tự động tạo folder nếu chưa tồn tại
- Chuẩn hóa tên file

Output:
file markdown hoàn chỉnh

## Luồng xử lý hệ thống

```diagram
Input File
    ↓
LangGraph Execution
    ↓
Loader Node
    ↓
Analyzer Node
    ↓
Standardization Node (Qwen3.5)
    ↓
Enrichment Node (Qwen3.5)
    ↓
Validation Node
    ↓
File Writer Tool
    ↓
Knowledge Base Output
```

## Luồng người dùng

```
User
  ↓
Web Application
  ↓
Backend API
  ↓
LangGraph Engine
  ↓
Qwen3.5 Nodes
  ↓
Knowledge Base
  ↓
Result
```

## Tại sao cần LangGraph

### Vấn đề kiến trúc cũ

- Prompt pipeline tuyến tính
- Không kiểm soát trạng thái
- Không retry khi AI sai
- Không validate output
- Không mở rộng multi-agent

### Giải pháp LangGraph

- Workflow dạng graph
- State tracking
- Retry logic
- Branching
- Tool execution layer
- Multi-agent system

## Cấu trúc project hệ thống

PMP_AI_SYSTEM/

├── 01_Setup/  
├── 02_Content_Standardization/  
├── 03_Question_Generation/  
├── 04_Web_App/  
├── 05_Deployment/  
├── 06_AI_WORKFLOW_ENGINE/  
├── config/  
└── README.md  

## Module mới

06_AI_WORKFLOW_ENGINE

Chứa:
- LangGraph workflow definitions
- Node definitions
- State management
- Tool execution layer
- Retry & validation logic

## Knowledge Base Structure

PMP Knowledge Base/

├── 0_MASTER_MINDMAP/  
├── 1_COURSES/  
├── 2_CONCEPTS_LIBRARY/  
├── 3_PMI_MINDSET/  
├── 4_EXAM_PRACTICE/  
└── 5_REVISION/  

## Vai trò từng module

Setup → Cài Docker + Ollama  
Content Standardization → LangGraph pipeline xử lý nội dung  
Question Generation → Sinh câu hỏi + đề thi  
Web App → Giao diện người dùng  
Deployment → Deploy nội bộ  
AI Workflow Engine → Điều phối toàn bộ AI system  

## Mô hình mở rộng tương lai

- PMP
- AWS
- Scrum
- TOGAF
- mock exam
- adaptive test
- question bank
- Angular generator
- backend generator
- template builder

## Lợi ích kiến trúc mới

### Kỹ thuật
- state management
- workflow rõ ràng
- retry logic
- multi-agent system

### Business
- dễ mở rộng course
- dễ triển khai SaaS nội bộ
- dễ scale platform

### AI
- giảm hallucination
- tăng chất lượng output
- kiểm soát logic tốt hơn

## Mục tiêu cuối cùng

PMP_AI_SYSTEM không còn là script AI đơn giản.

Nó trở thành:

AI Learning Platform Engine dựa trên Workflow Graph Architecture

## Kết luận

Việc tích hợp LangGraph biến hệ thống từ:

prompt-based pipeline

thành:

AI workflow engine có kiến trúc sản phẩm thật sự