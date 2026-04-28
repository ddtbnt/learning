# PMP_AI_SYSTEM

## Giới thiệu

**PMP_AI_SYSTEM** là hệ thống AI local dùng để xây dựng nền tảng học PMP chạy nội bộ.

Hệ thống sử dụng:

- Docker Desktop  
- Ollama  
- Qwen3.5  
- Prompt Engineering  
- Web Application  

Mục tiêu:

- chuẩn hóa nội dung khóa học PMP  
- loại bỏ nội dung trùng lặp  
- làm giàu kiến thức còn thiếu  
- sinh flashcards song ngữ  
- sinh câu hỏi luyện tập  
- sinh đề thi thử chuẩn PMI  
- xây chatbot học tập nội bộ  
- sẵn sàng triển khai nội bộ công ty sau này  

---

## Tư duy kiến trúc hệ thống

Hệ thống được tách thành **2 project độc lập**.

### 1. Project hệ thống AI

**PMP_AI_SYSTEM**

Chứa:

- source code hệ thống  
- docker  
- prompt chuẩn  
- backend API  
- frontend web app  
- deployment script  

👉 Đây là phần **Framework / Engine**

### 2. Project dữ liệu tri thức

**PMP Exam Prep Certification Training Specialization**

Chứa:

- nội dung khóa học gốc  
- kiến thức chuẩn hóa  
- flashcards  
- câu hỏi  
- mock exam  
- tài liệu revision  

👉 Đây là phần **Knowledge Base**

---

## Kiến trúc tổng thể

```text
    PMP_AI_SYSTEM  --->  AI Processing  --->  PMP Knowledge Base
```
---

## Mô hình hoạt động

```text
    PMP course files
            ↓
        Qwen3.5
            ↓
    Standardize content
            ↓
    Generate lessons
            ↓
    Generate questions
            ↓
    Save back into Knowledge Base
```
---

## Luồng xử lý người dùng

```text
    User
      ↓
    Web App
      ↓
    Backend API
      ↓
    Qwen3.5
      ↓
    Knowledge Base
      ↓
    Result
```
---

## Tại sao phải tách 2 project

### Code không lẫn dữ liệu

    code ≠ content

Điều này giúp:

- dễ bảo trì  
- dễ nâng cấp  
- dễ kiểm thử  
- dễ backup  

### Dễ mở rộng

Sau này có thể thay Knowledge Base thành:

- PMP  
- AWS  
- Scrum  
- TOGAF  
- Internal company training  

Mà không cần viết lại engine.

### Dễ triển khai nội bộ

Khi công ty cấp server:

- Linux server  
- Docker  
- RAM lớn  
- CPU mạnh  

Chỉ cần deploy:

**PMP_AI_SYSTEM**

và mount thư mục dữ liệu.

---

## Cấu trúc thư mục hệ thống

```diagram
    PMP_AI_SYSTEM/
    ├── 01_Setup/
    ├── 02_Content_Standardization/
    ├── 03_Question_Generation/
    ├── 04_Web_App/
    ├── 05_Deployment/
    ├── config/
    └── README.md
```
---

## Vai trò từng module

| Thư mục | Chức năng |
|--------|-----------|
| 01_Setup | Cài Docker + Ollama + model |
| 02_Content_Standardization | Chuẩn hóa nội dung học |
| 03_Question_Generation | Sinh câu hỏi và đề thi |
| 04_Web_App | Xây giao diện web |
| 05_Deployment | Triển khai nội bộ |
| config | Cấu hình đường dẫn hệ thống |

---

## Cấu trúc Knowledge Base

```diagram
    PMP Exam Prep Certification Training Specialization/
    ├── 0_MASTER_MINDMAP/
    ├── 1_COURSES/
    ├── 2_CONCEPTS_LIBRARY/
    ├── 3_PMI_MINDSET/
    ├── 4_EXAM_PRACTICE/
    └── 5_REVISION/
```
---

## Vai trò Knowledge Base

Knowledge Base lưu:

- markdown chuẩn hóa  
- flashcards  
- bài học song ngữ  
- câu hỏi luyện tập  
- đề thi thử  
- ghi chú sai  

Đây là nơi AI đọc và ghi dữ liệu liên tục.

---

## Kết nối giữa hai project

File cấu hình:

    PMP_AI_SYSTEM/config/system.json

Ví dụ nội dung:

```json
    {
      "knowledge_base_path": "D:/MyProjects/learning/PMP Exam Prep Certification Training Specialization"
    }
```
AI sẽ đọc dữ liệu từ đường dẫn này.

---

## Khi chạy bằng Docker

Ví dụ mount dữ liệu:

    docker run -v "D:/MyProjects/learning/PMP Exam Prep Certification Training Specialization:/data" pmp-ai

Ý nghĩa:

    Container AI  --->  đọc dữ liệu thật bên ngoài

Ưu điểm:

- Không mất dữ liệu  
- Dễ backup  
- Dễ deploy  
- Không sửa code khi đổi server  

---

## Lợi ích của kiến trúc này

Ưu điểm:

- dễ bảo trì  
- dễ mở rộng  
- dễ deploy  
- dễ backup  
- tái sử dụng cho nhiều khóa học khác  

---

## Mục tiêu cuối cùng

Hệ thống này có thể trở thành:

- PMP Learning Platform  
- PMP Exam Simulator  
- Internal AI Tutor  

---

## Bước tiếp theo

Tiếp tục tại:

    01_Setup/README.md

để bắt đầu:

- cài Docker Desktop  
- cài Ollama  
- pull Qwen3.5  
- mount Knowledge Base  
- chạy local AI system  

---

## Ghi chú

Tài liệu này được viết theo hướng:

- dễ đọc lâu dài  
- dễ đưa lên GitHub  
- dễ mở rộng về sau  
- phù hợp triển khai nội bộ