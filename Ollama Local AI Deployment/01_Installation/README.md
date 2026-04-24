# 01 Installation

## Ollama là gì?

Ollama là công cụ giúp chạy mô hình AI trực tiếp trên:

- máy cá nhân
- máy nội bộ công ty
- server riêng

Mục đích:

- hỗ trợ lập trình
- xử lý tài liệu
- chatbot nội bộ
- migrate source code
- bảo mật dữ liệu tốt hơn cloud

---

# OpenCode là gì?

OpenCode là công cụ coding assistant chạy trong terminal.

Nó giúp:

- đọc source code
- hiểu cấu trúc project
- sửa file
- tạo file mới
- refactor code
- migrate Angular sang React

OpenCode **không phải model AI**.

OpenCode chỉ là:

```text
giao diện làm việc với model AI
```

---

# Codex là gì?

Codex là một coding agent khác tương tự OpenCode.

Mục đích:

- phân tích source code
- hỗ trợ viết code
- review code
- tạo file

Có thể dùng thay thế OpenCode.

---

# Mối quan hệ giữa các thành phần

```text
Người dùng
   ↓
OpenCode / Codex
   ↓
Ollama
   ↓
Qwen3.5 Model
```

---

# Ý nghĩa từng thành phần

| Thành phần | Vai trò |
|-----------|--------|
| Ollama | chạy model local |
| Model | xử lý AI |
| OpenCode | giao diện coding |
| Codex | coding agent khác |

---

# Lưu ý quan trọng

Lệnh:

```bash
ollama launch opencode
```

chỉ hoạt động nếu:

```text
OpenCode đã được cài trong máy
```

Nếu chưa cài sẽ báo:

```text
opencode is not installed
```

---
# Cài OpenCode trên Windows

OpenCode được cài thông qua:

```text
npm
```

---

## npm là gì?

`npm` là công cụ quản lý package đi kèm với:

```text
Node.js
```

Nó dùng để cài:

- OpenCode
- Codex
- các CLI hỗ trợ lập trình

---

## 1. Kiểm tra Node.js đã cài chưa

Mở CMD:

```bash
node --version
```

Ví dụ:

```text
v22.15.0
```

---

## 2. Kiểm tra npm đã có chưa

```bash
npm --version
```

Ví dụ:

```text
10.9.2
```

Nếu có phiên bản:
=> npm đã sẵn sàng.

---

## 3. Nếu chưa có Node.js

Tải và cài:

:contentReference[oaicite:0]{index=0}

Sau khi cài xong mở lại CMD rồi kiểm tra:

```bash
node --version
npm --version
```

---

## 4. Cài OpenCode

Khi npm đã sẵn sàng:

```bash
npm install -g opencode-ai
```

Giải thích:

| Tham số | Ý nghĩa |
|--------|--------|
| `install` | cài package |
| `-g` | cài toàn hệ thống |
| `opencode-ai` | tên package |

---

## 5. Kiểm tra OpenCode đã cài

```bash
opencode --version
```

Ví dụ:

```text
1.2.0
```

=> cài thành công.

---

## 6. Kiểm tra vị trí cài

```bash
where opencode
```

Ví dụ:

```text
C:\Users\YourUser\AppData\Roaming\npm\opencode.cmd
```

---

## 7. Chạy OpenCode với Ollama

```bash
ollama launch opencode
```

hoặc:

```bash
opencode --provider ollama --model qwen3.5:9b
```

---

## Kết luận

Thứ tự đúng:

```text
Cài Node.js
→ kiểm tra npm
→ cài OpenCode
→ kiểm tra OpenCode
→ dùng với Ollama
```

# Các lệnh cơ bản cần nhớ

| Lệnh | Mục đích | Khi dùng |
|------|----------|----------|
| `ollama --version` | Kiểm tra Ollama đã cài chưa | Lần đầu cài |
| `ollama list` | Xem model trong máy | Kiểm tra model |
| `ollama pull` | Tải model mới | Khi cần model |
| `ollama run` | Chạy model | Chat trực tiếp |
| `ollama ps` | Xem model đang chạy | Kiểm tra RAM |
| `ollama stop` | Dừng model | Giải phóng RAM |
| `ollama rm` | Xóa model | Giải phóng ổ cứng |
| `ollama show` | Xem thông tin model | Kiểm tra chi tiết |
| `ollama launch` | Chạy coding agent | Coding |
| `ollama create` | Tạo model tùy chỉnh | Nâng cao |

---

# Chi tiết từng lệnh

---

## 1. Kiểm tra phiên bản Ollama

### Mục đích
Kiểm tra máy đã cài Ollama chưa.

```bash
ollama --version
```

---

## 2. Xem danh sách model trong máy

### Mục đích
Hiển thị model đã tải.

```bash
ollama list
```

---

## 3. Tải model mới

### Mục đích
Tải model từ server về máy.

```bash
ollama pull qwen3.5:9b
```

---

## 4. Chạy model

### Mục đích
Mở model để chat.

```bash
ollama run qwen3.5:9b
```

---

## 5. Kiểm tra model đang chạy

### Mục đích
Xem model nào đang dùng RAM.

```bash
ollama ps
```

---

## 6. Dừng model

### Mục đích
Giải phóng RAM.

```bash
ollama stop qwen3.5:9b
```

---

## 7. Xóa model

### Mục đích
Giải phóng dung lượng ổ cứng.

```bash
ollama rm qwen3-vl:8b
```

---

## 8. Xem thông tin model

### Mục đích
Kiểm tra thông số model.

```bash
ollama show qwen3.5:9b
```

---

## 9. Chạy coding agent

### Mục đích
Dùng AI hỗ trợ code.

```bash
ollama launch opencode
```

Hoặc:

```bash
ollama launch codex
```

---

## 10. Tạo model riêng

### Mục đích
Tạo model tùy chỉnh.

```bash
ollama create mymodel -f Modelfile
```

---

# 5 lệnh quan trọng nhất cần nhớ

```bash
ollama list
ollama pull qwen3.5:9b
ollama run qwen3.5:9b
ollama ps
ollama stop qwen3.5:9b
```

---

# Quy trình sử dụng cơ bản

## Bước 1 — kiểm tra

```bash
ollama --version
```

---

## Bước 2 — tải model

```bash
ollama pull qwen3.5:9b
```

---

## Bước 3 — chạy model

```bash
ollama run qwen3.5:9b
```

---

## Bước 4 — dừng model khi xong

```bash
ollama stop qwen3.5:9b
```

---

# Khi nào dùng launch?

Dùng khi muốn AI:

- đọc project
- sửa code
- migrate Angular sang React
- refactor source
- sinh file mới

Ví dụ:

```bash
ollama launch opencode
```

---

# Quy trình coding đầy đủ

```text
Cài Ollama
→ Pull model
→ Cài OpenCode
→ Launch agent
→ AI đọc project
→ AI hỗ trợ coding
```

---

# Khuyến nghị cho máy 16GB RAM

Nên dùng:

```bash
ollama pull qwen3.5:9b
```

Nếu máy yếu hơn:

```bash
ollama pull qwen3.5:4b
```

---

# Kết luận

Với máy cá nhân:

```text
Ollama + qwen3.5:9b
```

là đủ để:

- học project
- hỗ trợ code
- migrate source
- thử nghiệm AI nội bộ