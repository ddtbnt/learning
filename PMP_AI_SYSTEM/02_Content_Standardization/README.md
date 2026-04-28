# 02_Content_Standardization

## Mục tiêu

Module này dùng để:

- Đọc toàn bộ nội dung khóa học PMP
- Loại bỏ nội dung trùng lặp
- Chuẩn hóa cấu trúc markdown
- Bổ sung phần còn thiếu
- Chuyển nội dung sang song ngữ
- Tạo nền dữ liệu sạch cho hệ thống học và thi

Sau bước này:

Knowledge Base sẽ trở thành:

- dễ đọc
- dễ tìm kiếm
- dễ mở rộng
- dễ dùng cho AI

---

## Vì sao cần chuẩn hóa

Tài liệu gốc thường có:

- nhiều ý trùng nhau
- tiếng Anh khó hiểu
- format không đồng nhất
- thiếu liên kết giữa các chủ đề
- thiếu giải thích theo mindset PMI

Nếu không chuẩn hóa:

AI sẽ:

- trả lời thiếu ổn định
- sinh câu hỏi kém chất lượng
- tạo nội dung bị lặp

---

## Luồng xử lý

```diagram
    Raw course files
          ↓
    Qwen3.5 analyze
          ↓
    Remove duplicates
          ↓
    Enrich missing content
          ↓
    Convert bilingual
          ↓
    Save clean files
```
---

## Dữ liệu đầu vào

Nguồn dữ liệu chính:

```diagram
    PMP Exam Prep Certification Training Specialization/
    ├── 0_MASTER_MINDMAP/
    └── 1_COURSES/
```

Đây là dữ liệu:

- khóa học gốc
- ghi chú gốc
- sơ đồ tổng hợp

---

## Dữ liệu đầu ra

Sau khi chuẩn hóa sẽ ghi vào:

```diagram
    PMP Exam Prep Certification Training Specialization/
    ├── 2_CONCEPTS_LIBRARY/
    ├── 3_PMI_MINDSET/
    └── 5_REVISION/
```
---

## Bước 1 — Mở terminal

Di chuyển vào thư mục:

    cd /d "D:\MyProjects\learning\PMP Exam Prep Certification Training Specialization"

---

## Bước 2 — Chạy model

Chạy:

    ollama run qwen3.5:9b

---

## Bước 3 — Cho AI hiểu cấu trúc dữ liệu trước

### Mục tiêu của bước này

Bước này giúp AI:

- Hiểu cách tổ chức của Knowledge Base
- Xác định thư mục nào là nguồn dữ liệu gốc
- Xác định thứ tự chuẩn hóa phù hợp
- Phát hiện phần có thể bị trùng
- Xác định phần còn thiếu ở mức cấu trúc

---

### Lưu ý quan trọng

Qwen3.5 chạy bằng:

    ollama run qwen3.5:9b

sẽ không tự đọc ổ đĩa, vì vậy bạn cần:

- Copy cây thư mục
- Dán vào prompt
- Để AI phân tích

---

### Prompt dùng cho bước 3

```prompt

    You are a PMP knowledge architect.

    Review the PMP folder structure below.

    Understand:
    - purpose of each folder
    - possible duplicate sections
    - missing learning sections
    - weak organization
    - recommended processing order

    Important:
    - analyze structure only
    - do not analyze file content yet
    - preserve PMI terminology
    - do not rewrite anything

    Return:
    1. Folder or file group
    2. Issue found
    3. Why it matters
    4. Priority (High / Medium / Low)

    Folder structure:
    PMP/
    ├── 0_MASTER_MINDMAP/
    ├── 1_COURSES/
    ├── 2_CONCEPTS_LIBRARY/
    ├── 3_PMI_MINDSET/
    ├── 4_EXAM_PRACTICE/
    └── 5_REVISION/
```
---

### Kết quả mong muốn

AI sẽ xác định:

- Thư mục nào là nguồn dữ liệu gốc
- Thư mục nào đang trùng vai trò
- Thư mục nào còn thiếu
- Nên chuẩn hóa từ đâu trước

Ví dụ thường là:

- Bắt đầu từ `1_COURSES`
- Sau đó ghi vào `2_CONCEPTS_LIBRARY`

---

## Bước 4 — Chuẩn hóa từng file riêng lẻ

Sau khi AI hiểu cấu trúc,
bạn mới bắt đầu chuẩn hóa từng file.

Ví dụ file đầu tiên:

    1_COURSES/Course_1_Principles.md

---

### Lưu ý quan trọng

Bạn cần:

- Mở file
- Copy nội dung
- Dán vào prompt

vì model không tự mở file

---

### Prompt chuẩn hóa file

    You are a PMP knowledge architect.

    Standardize the PMP lesson below into a cleaner study format.

    Requirements:
    - remove duplicate ideas
    - simplify difficult English
    - add Vietnamese explanation
    - preserve PMI terminology
    - preserve original meaning
    - improve readability
    - do not invent new concepts
    - do not change PMI intent

    Output format:
    1. Concept
    2. Simple explanation
    3. Vietnamese meaning
    4. PMI exam note
    5. Key takeaway

    Lesson content:
    [PASTE FILE CONTENT HERE]

---

### Mục tiêu bước 4

AI sẽ:

- Làm nội dung dễ hiểu hơn
- Giữ đúng thuật ngữ PMI
- Song ngữ hóa
- Bỏ nội dung lặp
- Giữ nguyên ý nghĩa gốc

---

## Bước 5 — Lưu file chuẩn hóa

Sau khi AI trả kết quả,
lưu thành file mới trong:

    2_CONCEPTS_LIBRARY/

Ví dụ:

    2_CONCEPTS_LIBRARY/01_Fundamentals/project_lifecycle.md

---

### Nguyên tắc lưu file

- Mỗi concept = 1 file
- Dễ bảo trì
- Dễ tra cứu
- Dễ tái sử dụng
- Dễ sinh câu hỏi sau này

---

### Ví dụ luồng đúng

    Folder structure
        ↓
    Analyze structure
        ↓
    Select source file
        ↓
    Standardize content
        ↓
    Save into concept library

---

### Vì sao phải tách riêng

#### Bước 3

AI hiểu:

    cấu trúc hệ thống

#### Bước 4

AI hiểu:

    nội dung chi tiết

Tách như vậy giúp:

- Chính xác hơn
- Ít mất context
- Ít lỗi hơn
- Phù hợp với Qwen3.5:9b hơn

## Bước 6 — Tìm phần còn thiếu

Prompt:

    Based on the current concept library,
    identify missing PMP concepts.

    Return:
    - missing topic
    - correct folder
    - why needed

AI có thể phát hiện:

- servant leadership
- conflict management
- procurement
- stakeholder engagement

---

## Bước 7 — Tạo file bổ sung

Prompt:

    Create a new PMP concept file for:

    Risk Response Strategies

    Include:
    - definition
    - bilingual explanation
    - exam tip
    - common mistake

Lưu vào:

    2_CONCEPTS_LIBRARY/

---

## Bước 8 — Chuẩn hóa mindset PMI

Ghi vào:

    3_PMI_MINDSET/

Prompt:

    Extract PMI mindset rules from this lesson.

    Output:
    - what PMI prefers
    - what PMI avoids
    - decision logic

---

## Bước 9 — Tạo flashcards

Prompt:

    Create bilingual flashcards from this concept.

    Format:
    Front:
    Back:
    English:
    Vietnamese:

Lưu:

    5_REVISION/Flashcards.md

---

## Bước 10 — Tạo cheat sheet

Prompt:

    Summarize this topic into a one-minute review sheet.

Lưu:

    5_REVISION/Cheat_Sheet.md

---

## Quy tắc quan trọng

Luôn:

- xử lý 1 file mỗi lần
- review trước khi lưu
- không xử lý toàn bộ cùng lúc

Không nên:

    Rewrite the whole folder now.

Vì:

- model dễ mất context
- dễ sinh nội dung sai
- RAM tăng mạnh

---

## Quy trình đúng

```diagram
    Analyze
      ↓
    Clean
      ↓
    Enrich
      ↓
    Review
      ↓
    Save
```
---

## Prompt tổng hợp

Có thể dùng:

    Use existing files as the source of truth.

    Tasks:
    1. standardize content
    2. remove duplicates
    3. enrich missing concepts
    4. simplify English
    5. add Vietnamese explanation

    Important:
    - preserve PMI meaning
    - avoid duplication
    - keep clean structure

---

## Kết quả sau module này

Sau khi hoàn thành:

Bạn sẽ có:

- concept library sạch
- nội dung song ngữ
- mindset PMI rõ ràng
- dữ liệu sẵn sàng sinh câu hỏi

---

## Thư mục sau chuẩn hóa

```diagram
    PMP Exam Prep Certification Training Specialization/
    ├── 2_CONCEPTS_LIBRARY/
    ├── 3_PMI_MINDSET/
    └── 5_REVISION/
```
---

## Bước tiếp theo

Tiếp tục:

```diagram
    ../03_Question_Generation/README.md
```

để:

- học pattern đề PMP
- sinh câu hỏi mới
- tạo mock exam

---

## Ghi chú

Sau mỗi phiên:

    ollama stop qwen3.5:9b

để:

- giải phóng RAM
- giảm CPU
- tránh model chạy nền