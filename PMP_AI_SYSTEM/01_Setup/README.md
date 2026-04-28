# 01_Setup

## Mục tiêu

Module này dùng để chuẩn bị môi trường local cho hệ thống:

- cài Docker Desktop
- cài Ollama
- tải model Qwen3.5
- kết nối Knowledge Base
- kiểm tra hệ thống hoạt động

Sau bước này máy local sẽ sẵn sàng để:

- chuẩn hóa tài liệu PMP
- sinh câu hỏi
- chạy web app nội bộ

---

## Thành phần cần cài

Hệ thống cần:

- Docker Desktop
- Ollama
- Node.js
- npm
- Qwen3.5 model

---

## Kiến trúc local

```diagram
    Windows
       ↓
    Docker Desktop
       ↓
    Ollama
       ↓
    Qwen3.5
       ↓
    PMP Knowledge Base
```

---

## Bước 1 — Cài Docker Desktop

Tải Docker Desktop:

    https://www.docker.com/products/docker-desktop

Sau khi cài:

Mở terminal kiểm tra:

    docker --version

Kết quả ví dụ:

    Docker version 27.x.x

Nếu thấy version:

✅ Docker đã cài thành công

---

## Bước 2 — Cài Ollama

Tải Ollama:

    https://ollama.com

Kiểm tra:

    ollama --version

Ví dụ:

    ollama version 0.xx.x

Nếu thấy version:

✅ Ollama hoạt động

---

## Bước 3 — Kiểm tra Node.js

OpenCode cần Node.js.

Kiểm tra:

    node --version

Ví dụ:

    v20.x.x

Kiểm tra npm:

    npm --version

Ví dụ:

    10.x.x

Nếu chưa có:

Tải Node.js:

    https://nodejs.org

---

## Bước 4 — Cài OpenCode

OpenCode là coding agent giúp:

- đọc folder
- phân tích markdown
- hỗ trợ generate nội dung
- hỗ trợ phát triển web app

Cài:

    npm install -g opencode-ai

Kiểm tra:

    opencode --version

Nếu thấy version:

✅ OpenCode sẵn sàng

---

## Bước 5 — Tải model Qwen3.5

Khuyến nghị cho máy 16GB RAM:

    ollama pull qwen3.5:9b

Máy yếu hơn:

    ollama pull qwen3.5:4b

Kiểm tra:

    ollama list

Ví dụ:

    NAME          SIZE
    qwen3.5:9b    6.6 GB

---

## Bước 6 — Chạy test model

Chạy:

    ollama run qwen3.5:9b

Test prompt:

    Explain the purpose of PMP knowledge management.

Nếu model trả lời:

✅ Model hoạt động

---

## Bước 7 — Dừng model

Thoát chat:

    Ctrl + D

Hoặc:

    /bye

Sau đó dừng:

    ollama stop qwen3.5:9b

Kiểm tra:

    ollama ps

Nếu hiện:

    No models loaded

=> model đã giải phóng RAM

---

## Bước 8 — Cấu hình đường dẫn Knowledge Base

Tạo file:

    PMP_AI_SYSTEM/config/system.json

Nội dung:

    {
      "knowledge_base_path": "D:/MyProjects/learning/PMP Exam Prep Certification Training Specialization"
    }

Ý nghĩa:

Hệ thống sẽ đọc dữ liệu từ project tri thức.

---

## Bước 9 — Mount dữ liệu bằng Docker

Ví dụ chạy container:

    docker run -it ^
    -v "D:/MyProjects/learning/PMP Exam Prep Certification Training Specialization:/data" ^
    pmp-ai

Ý nghĩa:

    local folder  --->  container /data

Ưu điểm:

- dữ liệu không mất
- dễ backup
- dễ deploy

---

## Bước 10 — Kiểm tra toàn bộ

Kiểm tra từng phần:

Docker:

    docker --version

Ollama:

    ollama --version

Model:

    ollama list

Agent:

    opencode --version

Nếu tất cả OK:

✅ môi trường local hoàn chỉnh

---

## Khuyến nghị cấu hình máy

### Tối thiểu

- RAM 16GB
- CPU 6 cores
- SSD 50GB trống

### Khuyến nghị

- RAM 32GB
- CPU 8 cores+
- SSD NVMe

---

## Cấu trúc sau khi setup

```diagram
    PMP_AI_SYSTEM/
    ├── 01_Setup/
    ├── config/
    └── docker/
```

---

## Kết quả sau module này

Sau khi hoàn thành:

Bạn sẽ có:

- local AI chạy được
- model hoạt động
- đọc được knowledge base
- sẵn sàng chuẩn hóa dữ liệu

---

## Bước tiếp theo

Tiếp tục:

    ../02_Content_Standardization/README.md

để bắt đầu:

- cho AI đọc dữ liệu khóa học
- chuẩn hóa nội dung
- làm giàu tri thức

---

## Ghi chú

Luôn nhớ:

Khi không dùng:

    ollama stop qwen3.5:9b

Điều này giúp:

- giải phóng RAM
- giảm CPU
- tránh model chạy nền