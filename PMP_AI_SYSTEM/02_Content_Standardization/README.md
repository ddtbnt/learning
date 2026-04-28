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

## Bước 3 — Cho AI hiểu cấu trúc dữ liệu

Prompt:

```prompt

	You are a PMP knowledge architect.

	Review this PMP learning folder.

	Analyze only the existing files.

	Identify:
	- duplicate topics
	- missing concepts
	- weak explanations
	- inconsistent structure
	- files that should be standardized first

	Important:
	- use only the current course files
	- preserve PMI terminology
	- do not rewrite content yet
	- do not create new content yet

	Return:
	1. File name
	2. Issue found
	3. Why it matters
	4. Priority (High / Medium / Low)
```

Mục tiêu:

AI xác định:

- file trùng
- file thiếu
- file yếu
- thứ tự xử lý

---

## Bước 4 — Chuẩn hóa từng file

Ví dụ file:

    1_COURSES/Course_1_Principles.md

Prompt:

    Rewrite this file into a cleaner PMP study format.

    Requirements:
    - remove duplicate ideas
    - simplify English
    - add Vietnamese explanation
    - preserve PMI terminology
    - improve readability

    Output:
    1. Concept
    2. Simple explanation
    3. Vietnamese meaning
    4. Key takeaway

---

## Bước 5 — Lưu file chuẩn hóa

Ví dụ lưu:

    2_CONCEPTS_LIBRARY/01_Fundamentals/project_lifecycle.md

Mỗi concept:

- 1 file riêng
- dễ tái sử dụng
- dễ tìm kiếm

---

## Cấu trúc file chuẩn

Mẫu:

    # Project Lifecycle

    ## Definition
    English explanation

    ## Giải thích
    Vietnamese explanation

    ## PMI mindset
    Important exam logic

    ## Key takeaway
    Important note

---

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