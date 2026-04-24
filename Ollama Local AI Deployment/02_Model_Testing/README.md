# 02 Model Testing

## Mục tiêu

Kiểm tra model có phù hợp với máy hiện tại hay không:

- tốc độ phản hồi
- mức dùng RAM
- mức dùng CPU
- khả năng hiểu source code
- độ ổn định khi chạy lâu
- cách tắt model đúng cách khi không dùng

---

# Tổng quan cách test

Quy trình đúng:

```text
Chạy model
→ Gửi prompt test
→ Quan sát RAM / CPU
→ Dừng model
→ Kiểm tra đã giải phóng RAM chưa
```

---

# 1. Kiểm tra trước khi chạy

Mở CMD:

```bash
ollama ps
```

Nếu thấy:

```text
No models loaded
```

=> hiện chưa có model nào chạy.

Nếu thấy:

```text
NAME         ID           SIZE    PROCESSOR
qwen3.5:9b   xxxxxxxx     6.6 GB  CPU
```

=> model đang chạy và đang giữ RAM.

---

# 2. Chạy model để test

Gõ:

```bash
ollama run qwen3.5:9b
```

Sau đó terminal chuyển sang:

```text
>>>
```

Dấu này nghĩa là:
👉 bạn đang chat trực tiếp với model.

---

# 3. Test phản hồi đơn giản

Nhập prompt:

```text
Explain React hooks simply.
```

Mục đích:
- đo tốc độ phản hồi
- xem model trả lời mượt không

---

# 4. Test khả năng đọc code

Nhập prompt:

```text
Explain what this Angular component does.
```

Mục đích:
- xem model hiểu code không
- xem giải thích có đúng không

---

# 5. Test prompt dài

Nhập:

```text
Explain the architecture of a medium Angular enterprise project.
```

Mục đích:
- kiểm tra context
- kiểm tra tốc độ xử lý prompt dài

---

# 6. Kiểm tra RAM / CPU

Mở Task Manager:

```text
Ctrl + Shift + Esc
```

Quan sát:

| Mục | Ý nghĩa |
|-----|--------|
| Memory | RAM model đang dùng |
| CPU | tải CPU |
| Disk | swap nếu thiếu RAM |

---

# 7. Kiểm tra model có còn chạy không

Mở thêm 1 cửa sổ CMD mới.

Gõ:

```bash
ollama ps
```

Nếu thấy model:
=> model vẫn đang chiếm RAM

---

# 8. Cách thoát khỏi màn hình chat

Khi đang thấy:

```text
>>>
```

Bạn có thể thoát chat bằng:

```text
Ctrl + D
```

hoặc:

```text
/bye
```

hoặc:

```text
/exit
```

Sau đó terminal trở về:

```bash
C:\Users\...
```

Lúc này bạn đã thoát khỏi chế độ chat.

---

# 9. Cách dừng model đúng cách

## Quan trọng

Khi đang ở màn hình:

```text
>>>
```

Bạn KHÔNG gõ:

```bash
ollama stop qwen3.5:9b
```

vì model sẽ hiểu đó là câu chat.

---

## Cách đúng

### Cách 1 (khuyên dùng)
Mở CMD thứ 2 rồi gõ:

```bash
ollama stop qwen3.5:9b
```

---

### Cách 2
Thoát chat trước rồi gõ:

```bash
ollama stop qwen3.5:9b
```

---

# 10. Kiểm tra model đã tắt chưa

Gõ:

```bash
ollama ps
```

Nếu thấy:

```text
No models loaded
```

=> model đã tắt hoàn toàn

RAM đã được giải phóng.

---

# 11. Đóng terminal

Sau khi xong:

```bash
exit
```

Mục đích:
- đóng CMD
- kết thúc phiên test

---

# 12. Ghi kết quả benchmark

| Kiểm tra | Kết quả |
|----------|---------|
| Startup time | |
| First response | |
| RAM usage | |
| CPU usage | |
| Long prompt | |
| Stability | |

---

# 13. Đánh giá model

## Nếu RAM ổn

Nếu RAM dưới ~12GB:
có thể tiếp tục dùng:

```text
qwen3.5:9b
```

---

## Nếu RAM cao

Nên dùng model nhẹ hơn:

```bash
ollama pull qwen3.5:4b
```

---

# 14. Quy trình đúng sau mỗi lần test

```text
1. ollama run
2. gửi prompt
3. xem Task Manager
4. Ctrl + D
5. ollama stop
6. ollama ps
7. exit
```

---

# 15. 3 lệnh quan trọng nhất

## Kiểm tra model đang chạy

```bash
ollama ps
```

---

## Dừng model

```bash
ollama stop qwen3.5:9b
```

---

## Đóng terminal

```bash
exit
```

---

# 16. Kết luận

Khi không dùng nữa luôn làm:

```bash
ollama stop qwen3.5:9b
```

sau đó:

```bash
exit
```

Đây là cách:
- gọn nhẹ
- giải phóng RAM
- tránh model chạy ngầm
- tránh máy chậm