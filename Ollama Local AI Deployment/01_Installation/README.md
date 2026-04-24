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
| `ollama launch` | Chạy AI agent | Coding |
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
ollama rm qwen3-vl:8b
```

---

# Quy trình sử dụng cơ bản

## Bước 1 — kiểm tra
```bash
ollama --version
```

## Bước 2 — tải model
```bash
ollama pull qwen3.5:9b
```

## Bước 3 — chạy model
```bash
ollama run qwen3.5:9b
```

## Bước 4 — dừng khi xong
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

Ví dụ:
```bash
ollama launch opencode
```

---

# Khuyến nghị cho máy 16GB RAM

Nên dùng:
```bash
ollama pull qwen3.5:9b
```

Nếu máy yếu:
```bash
ollama pull qwen3.5:4b
```