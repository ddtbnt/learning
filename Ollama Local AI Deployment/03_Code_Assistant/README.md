# 03 Code Assistant

Module này hướng dẫn cách dùng AI để:

- đọc source code Angular
- hiểu cấu trúc dự án
- xác định business logic
- tìm file quan trọng
- chuẩn bị cho bước migrate sau này

Project hiện tại:

```text
YOUR_LOCAL_DIRECTORY_CODE
D:\MyProjects\ConvertCode\web-admin
```

---

# Mục tiêu của bước này

Ở bước này model cần:

- hiểu cấu trúc project
- hiểu folder
- hiểu service
- hiểu routing
- hiểu module
- chưa viết code ngay

Mục tiêu chính:
```text
Cho AI học project trước khi ra lệnh sửa code
```

---

# Bước 1 — Mở terminal tại thư mục dự án

Mở CMD hoặc PowerShell:

```bash
cd /d YOUR_LOCAL_DIRECTORY_CODE
cd /d D:\MyProjects\ConvertCode\web-admin
```

Kiểm tra thư mục:

```bash
dir
```

Bạn cần thấy:

```text
src
package.json
angular.json
tsconfig.json
```

---

# Bước 2 — Khởi chạy coding agent

Khuyến nghị:

```bash
ollama launch opencode
```

Hoặc:

```bash
ollama launch codex
```

Mục đích:
- cho AI truy cập source
- hiểu project
- phân tích file

Sau khi chạy lệnh, coding agent sẽ được khởi động và hiển thị như sau:

![Qwen Coding Assistant](./qwen3.5-9b.png)

# Bước 3 — Yêu cầu AI học project trước

Prompt đầu tiên:

```text
You are a senior Angular architect.

First:
- analyze this Angular project
- understand folder structure
- understand coding style
- understand services
- understand routing
- understand shared modules

Do not generate code yet.
Explain the project architecture first.
```

Sau khi chạy lệnh, kết quả hiển thị như sau:
![Step 3 - AI Study Project](./step3-study-project-summary.png)

# Bước 4 — Yêu cầu AI liệt kê module quan trọng

Prompt:

```text
List the important modules in this project.
Explain:
- authentication
- shared components
- API services
- routing
- guards
- business modules
```

Mục tiêu:
AI xác định:
- file quan trọng
- logic chính
- module chính

Sau khi chạy lệnh, kết quả hiển thị như sau:

![Step 4 - AI List Important Modules](./step4-ai-list-important-modules.png)

# Bước 5 — Tìm nơi xử lý API

Prompt:

```text
Which files handle API communication in this project?
```

Hoặc:

```text
Show me where HTTP requests are implemented.
```

Mục tiêu:
xác định:
- service layer
- interceptor
- token handling

Sau khi chạy lệnh, kết quả hiển thị như sau:

![Step 5 - API Communication Analysis](./step5-api-communication-analysis.png)

# Bước 6 — Tìm luồng đăng nhập

Prompt:

```text
Explain the login flow in this Angular project step by step.
```

AI sẽ giúp bạn hiểu:
- login component
- auth service
- token storage
- route guard

Sau khi chạy lệnh, kết quả hiển thị như sau:

![Step 6 - Login Flow Analysis](./step6-login-flow-analysis.png)


# Bước 7 — Tìm component nên chuyển trước

Prompt:

```text
Which component should be migrated first with the lowest risk?
```

AI thường chọn:
- component nhỏ
- ít dependency
- dễ test

Ví dụ:
- login
- form nhỏ
- table nhỏ

Sau khi chạy lệnh, kết quả hiển thị như sau:

![Step 7 - First Component Migration Suggestion](./step7-first-migration-component.png)

# Bước 8 — Cho AI học một component cụ thể

## Ví dụ với màn hình đăng nhập

```text
src/app/auth/login/login.component.ts
src/app/auth/login/login.component.html
src/app/auth/login/login.component.scss
```

Prompt:

```text
Please analyze this Angular login component:

src/app/auth/login/login.component.ts
src/app/auth/login/login.component.html
src/app/auth/login/login.component.scss

Explain:
- component logic
- form validation
- API call
- UI rendering
- authentication flow
```

Sau khi chạy lệnh, kết quả hiển thị như sau:

![Step 8 - Component Analysis](./step8-component-analysis.png)

# Bước 9 — Học coding style của project

## Mục tiêu
Cho AI hiểu coding style hiện tại để sinh code đồng nhất với source.

## File mẫu nên đọc

```text
src/app/core/
src/app/shared/
src/app/auth/
src/app/modules/
```

Prompt:

```text
Study the coding style of this Angular project.

Analyze these areas:
- naming convention
- folder structure
- service implementation
- component structure
- RxJS usage
- API handling
- state management
- HTML template style
- SCSS organization

Important:
- infer existing patterns only
- do not suggest refactoring
- do not rewrite code
- remember this style for future generated code

When generating new code later:
- keep same naming
- keep same import order
- keep same dependency injection style
- keep same observable pattern
- keep same HTML structure
```

Mục tiêu:
để model viết code giống dự án hiện tại

Sau khi chạy lệnh, kết quả hiển thị như sau:

![Step 9 - Coding Style Learning](./step9-coding-style-learning.png)

# Bước 10 — Kiểm tra model đã hiểu project chưa

## Mục tiêu
Xác nhận AI đã nắm được:
- kiến trúc project
- module chính
- service layer
- authentication flow
- coding style

## Prompt tối ưu cho Qwen 3.5 9B

```text
Summarize your understanding of this Angular project.

Please explain:

1. Project architecture
2. Main modules
3. Shared components
4. Core services
5. Authentication flow
6. API communication flow
7. State/data handling
8. Coding style patterns

Important:
- use only information from the source code
- do not guess missing parts
- do not recommend improvements
- keep summary concise and technical
```

Sau khi chạy lệnh, kết quả hiển thị như sau:

![Step 10 - Project Understanding Check](./step10-project-understanding-check.png)

# Bước 11 — Lưu context trước khi bắt đầu code

## Mục tiêu
Giữ cho AI:
- nhớ architecture
- nhớ coding style
- nhớ naming convention
- không tự ý sinh code sớm
- chuẩn bị cho bước generate code tiếp theo

## Prompt tối ưu cho Qwen 3.5 9B

```text
Remember the current project architecture and coding style.

Keep in memory:
- folder structure
- naming convention
- component pattern
- service pattern
- API handling
- authentication flow
- RxJS usage
- HTML structure
- SCSS organization

Important:
- do not generate code yet
- do not suggest improvements
- do not refactor existing code
- wait for the next instruction

For future code:
- follow the same project style exactly
- keep consistency with existing source code
```

Sau khi chạy lệnh, kết quả hiển thị như sau:

![Step 11 - Save Context Before Coding](./step11-save-context-before-coding.png)

# Những điều không nên làm

Không nên:

```text
Convert the whole project now.
```

Vì:
- project quá lớn
- model mất context
- dễ sai logic

---

# Cách đúng

Nên:

```text
Learn first.
Convert later.
One component at a time.
```

---

# Prompt tốt nhất để học project

```text
You are a senior frontend engineer.

First understand this Angular project.

Analyze:
- architecture
- modules
- routing
- services
- coding style

Do not generate code.
Explain your understanding only.
```

---

# Kết quả mong muốn

Sau bước này AI sẽ hiểu:

- project structure
- business flow
- coding convention
- migration order

Từ đó bước sau mới:
```text
Convert to React safely.
```

---

# Quy trình đúng

```text
Open project
→ Launch AI
→ Analyze project
→ Learn architecture
→ Learn component
→ Confirm understanding
→ Then convert
```

---

# Kết luận

Tại bước này chỉ làm:

```text
Cho AI học code dự án
```

Chưa nên:

```text
Chuyển React ngay
```

để tránh sai kiến trúc.