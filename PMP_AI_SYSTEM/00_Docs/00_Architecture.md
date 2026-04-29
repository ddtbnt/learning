# 00_DOCS/00_Architecture.md  
# PMP_AI_SYSTEM – Kiến trúc hệ thống AI LangGraph (Enterprise Design)

---

## 1. Tổng quan hệ thống

PMP_AI_SYSTEM là một **AI Learning Platform Engine chạy local**, được thiết kế theo tư duy hệ thống doanh nghiệp (enterprise workflow system).

Mục tiêu chính:

- Biến dữ liệu PMP thô → hệ thống kiến thức có cấu trúc
- Tạo nền tảng học PMP song ngữ Anh / Việt
- Sinh hệ thống luyện thi mô phỏng PMP exam
- Chạy hoàn toàn local (không phụ thuộc cloud)

---

## 2. Kiến trúc thư mục hệ thống (System Layout)

PMP_AI_SYSTEM được chia thành 6 lớp rõ ràng + 1 core engine:

PMP_AI_SYSTEM/
│
├── 00_DOCS/                      # DESIGN LAYER (CHỈ THIẾT KẾ – KHÔNG RUN CODE)
│   ├── 00_Architecture.md        # kiến trúc tổng thể hệ thống
│   ├── 01_Local_Dev_Setup.md     # hướng dẫn chạy local
│   ├── 02_LangGraph_Design.md    # thiết kế workflow graph
│   ├── 03_Data_Flow.md           # luồng dữ liệu end-to-end
│   ├── 04_Deployment_Windows.md  # deploy Windows local
│   └── 05_Production_Scaling.md  # chiến lược scale hệ thống
│
├── 01_Setup/                     # ENVIRONMENT BOOTSTRAP
│   ├── install_docker.md
│   ├── install_ollama.md
│   ├── load_qwen3_5.sh
│   ├── verify_env.py             # kiểm tra hệ thống ready
│   └── README.md
│
├── 02_Content_Standardization/   # PIPELINE 1: RAW → KNOWLEDGE
│   ├── pipeline/
│   │   ├── run_pipeline.py       # entry point LangGraph
│   │   ├── state.py              # định nghĩa STATE schema
│   │   ├── graph_builder.py      # build workflow graph
│   │   └── nodes/
│   │       ├── loader_node.py
│   │       ├── analyzer_node.py
│   │       ├── standard_node.py
│   │       ├── enrich_node.py
│   │       ├── mapping_node.py
│   │       ├── validate_node.py
│   │       └── writer_node.py
│   │
│   ├── prompts/
│   │   ├── standardize_prompt.md
│   │   ├── enrich_prompt.md
│   │   └── mapping_prompt.md
│   │
│   ├── config.yaml
│   └── logs/
│
├── 03_Question_Generation/       # PIPELINE 2: KNOWLEDGE → EXAM
│   ├── pipeline/
│   │   ├── generate_exam.py
│   │   ├── question_mapper.py
│   │   ├── exam_builder.py
│   │   ├── difficulty_classifier.py
│   │   └── explanation_generator.py
│   │
│   ├── templates/
│   │   └── pmp_exam_format.json
│   │
│   └── logs/
│
├── 04_Web_App/                   # APPLICATION LAYER (USER + ADMIN)
│   ├── backend/
│   ├── frontend/
│   └── api/
│
├── 05_Deployment/                # PRODUCTION LAYER
│   ├── docker-compose.yml
│   ├── nginx/
│   └── deploy.sh
│
├── 06_AI_WORKFLOW_ENGINE/        # CORE ENGINE (LANGGRAPH HEART)
│   │
│   ├── engine/                   # RUNTIME LAYER (EXECUTION CORE)
│   │   ├── graph_runtime.py      # LangGraph entrypoint
│   │   ├── state_manager.py      # STATE management xuyên pipeline
│   │   ├── llm_client.py         # Ollama / Qwen3.5 wrapper
│   │   ├── tool_registry.py      # file/json/io tools
│   │   ├── retry_policy.py       # retry + fallback logic
│   │   └── event_bus.py          # event-driven coordination
│   │
│   ├── nodes_core/               # NODE FRAMEWORK LAYER
│   │   ├── base_node.py          # abstract node class
│   │   ├── async_executor.py     # async / parallel execution
│   │   ├── node_registry.py      # register all nodes
│   │   ├── node_context.py       # context sharing
│   │   └── node_types.py         # LLM / IO / LOGIC types
│   │
│   ├── nodes/                    # BUSINESS LOGIC NODES (ABSTRACTED)
│   │   ├── content_nodes/        # RAW → KNOWLEDGE nodes group
│   │   ├── exam_nodes/           # KNOWLEDGE → EXAM nodes group
│   │   └── shared_nodes/         # reusable nodes
│   │
│   ├── workflows/                # LANGGRAPH PIPELINE DEFINITIONS
│   │   ├── content_pipeline.py   # RAW → KNOWLEDGE graph
│   │   ├── exam_pipeline.py      # KNOWLEDGE → EXAM graph
│   │   └── admin_pipeline.py     # ADMIN AI enrichment flow
│   │
│   ├── prompts/                  # AI PROMPT LAYER
│   │   ├── standardize_prompt.md
│   │   ├── enrich_prompt.md
│   │   ├── mapping_prompt.md
│   │   └── exam_prompt.md
│   │
│   ├── config/                  # SYSTEM CONFIGURATION
│   │   ├── engine_config.yaml
│   │   ├── node_config.yaml
│   │   └── workflow_config.yaml
│   │
│   ├── runtime_logs/            # EXECUTION OBSERVABILITY
│   │   ├── engine.log
│   │   ├── node_trace.log
│   │   └── error.log
│   │
│   └── tests/                   # TESTING LAYER
│       ├── test_graph.py
│       ├── test_nodes.py
│       └── test_llm_client.py

---

## 3. Tư duy thiết kế hệ thống

### 3.1 Stateful AI System (AI có trạng thái)

Hệ thống KHÔNG dùng kiểu:

Prompt → Output → Done

Mà dùng:

STATE → NODE → UPDATE STATE → NEXT NODE → LOOP

---

### 3.2 Graph-based Execution (LangGraph)

Luồng xử lý không tuyến tính mà là graph:

RAW DATA
→ Node A
→ Node B
→ Node C
↘ retry / branch / loop / fallback

---

### 3.3 Layer Separation (Tách lớp rõ ràng)

- 00_DOCS → thiết kế hệ thống (không chạy code)
- 01_Setup → môi trường runtime
- 02–03 → AI processing pipelines
- 04 → ứng dụng Web (USER + ADMIN)
- 05 → deployment production
- 06 → core AI engine (LangGraph runtime)

---

### 3.4 Controlled AI Execution

AI không được tự do sinh output.

Mọi xử lý phải:

- đi qua node rõ ràng
- có state rõ ràng
- có validation rõ ràng
- có retry/fallback logic

---

### 3.5 File-based Knowledge System

Hệ thống sử dụng:

- Markdown (.md)
- JSON (.json)

Không phụ thuộc database phức tạp.

---

## 4. Luồng dữ liệu tổng thể

PMP RAW DATA  
↓  
06_AI_WORKFLOW_ENGINE (LangGraph Runtime)  
↓  
02_Content_Standardization (Knowledge Generation)  
↓  
03_Question_Generation (Exam System)  
↓  
04_Web_App (User Experience)  
↓  
User Learning System

---

## 5. Vai trò từng tầng hệ thống

### 5.1 00_DOCS – DESIGN LAYER

- Chỉ thiết kế hệ thống
- Không chạy code
- Mô tả kiến trúc, flow, deployment

---

### 5.2 01_Setup – ENVIRONMENT LAYER

- Cài Docker
- Cài Ollama
- Load Qwen3.5
- Verify system ready

→ Output: môi trường AI local sẵn sàng

---

### 5.3 02_Content_Standardization – PIPELINE 1

Chức năng:

- RAW PMP → Concept Library
- Chuẩn hóa nội dung EN/VI
- Tách concept theo PMI domain
- Enrich kiến thức học

→ Output:
Knowledge Base chuẩn hóa

---

### 5.4 03_Question_Generation – PIPELINE 2

Chức năng:

- Map câu hỏi vào concept
- Chuẩn hóa format PMP exam
- Sinh mock exam
- Phân loại độ khó
- Tạo explanation EN/VI

→ Output:
Exam System hoàn chỉnh

---

### 5.5 04_Web_App – APPLICATION LAYER

#### Module 1: Learning System
- Học theo concept
- Hiển thị EN/VI
- Navigation theo PMI domain

#### Module 2: Exam System
- Random question engine
- Mock PMP exam
- Score + review sai

👉 Web App chỉ đọc Knowledge Base (KHÔNG gọi AI realtime)

---

### 5.6 05_Deployment – PRODUCTION LAYER

- Deploy backend API
- Kết nối LangGraph engine
- Serve hệ thống nội bộ / production

---

### 5.7 06_AI_WORKFLOW_ENGINE – CORE SYSTEM

Đây là “BỘ NÃO HỆ THỐNG”

Chức năng:

- Điều phối LangGraph execution
- Quản lý STATE toàn hệ thống
- Kết nối LLM (Qwen3.5 via Ollama)
- Node execution engine
- Retry / fallback / recovery
- Tool system (file IO, JSON processing)

---

## 6. LangGraph Execution Model

### 6.1 STATE Schema

STATE = {
  file_path,
  raw_content,
  extracted_concepts,
  analysis_result,
  standardized_output,
  enriched_output,
  mapping_result,
  validation_status,
  output_path
}

---

### 6.2 Node Flow Execution

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

## 7. Vai trò từng Node

### Loader Node
- Load file input
- Inject vào STATE

### Analyzer Node
- Phân tích nội dung
- Detect thiếu / trùng / lỗi logic

### Standardization Node
- Chuẩn hóa nội dung
- Chuyển EN → EN/VI
- Làm sạch format

### Enrichment Node
- Bổ sung kiến thức PMI
- Mở rộng nội dung học

### Mapping Node
- Map Course → Concept
- Map Question → Concept

### Validation Node
- Kiểm tra output
- Fail → rollback node trước

### Writer Node
- Ghi markdown output
- Tạo Knowledge Base structure

---

## 8. Kiến trúc dữ liệu

### INPUT

PMP/
├── 0_MASTER_MINDMAP/
├── 1_COURSES/
├── question.txt

---

### PROCESS

LangGraph AI Engine xử lý toàn bộ dữ liệu

---

### OUTPUT

PMP_KNOWLEDGE_BASE/
├── 2_CONCEPTS_LIBRARY/
├── 3_PMI_MINDSET/
├── 4_EXAM_PRACTICE/
├── 5_REVISION/

---

## 9. Luồng hệ thống USER

User  
→ Web App  
→ Backend API  
→ LangGraph Engine  
→ Qwen3.5  
→ Knowledge Base  
→ Response

---

## 10. Chạy hệ thống local

Công cụ:

- Docker
- Ollama
- Qwen3.5
- Python + LangGraph

Quy trình:

1. Start Ollama
2. Load model AI
3. Run pipeline
4. Generate Knowledge Base

→ 100% local execution

---

## 11. Khả năng mở rộng

- PMP → AWS → Scrum → TOGAF
- Thêm node mới
- Thêm workflow mới
- Thêm model AI mới

---

## 12. Error Handling System

- Retry node khi fail
- Loop validation
- State recovery
- Re-execution pipeline

---

## 13. Vì sao dùng LangGraph

Truyền thống:

Prompt → Output ❌

Kiến trúc mới:

State → Graph → Validate → Loop → Output ✔

Ưu điểm:

- Debug dễ
- Kiểm soát AI tốt
- Production-ready
- Mở rộng dễ

---

## 14. Tư duy hệ thống đầu ra

Hệ thống KHÔNG tạo:

- chatbot
- text generator
- prompt response

Mà tạo:

AI Learning System + Exam Engine + Knowledge Base

---

## 15. Tổng kết

PMP_AI_SYSTEM là:

AI Workflow Platform cấp enterprise

bao gồm:

- LangGraph AI Engine
- Knowledge Base System
- Exam Generation Engine
- Web Learning Platform
- Admin AI Pipeline
- Production Deployment System