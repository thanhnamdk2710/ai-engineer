# Hướng dẫn dịch tiếng Việt (vi) — Phase 00

Áp dụng cho mọi file `i18n/vi/phases/<phase>/<lesson>/docs/vi.md`. Nguồn chuẩn là `phases/<phase>/<lesson>/docs/en.md`.

## Quy tắc cấu trúc (bắt buộc)

1. **Giữ nguyên tuyệt đối:** mọi code block (```bash, ```python, ```mermaid, ```figure, ```text…) kể cả comment trong code; inline `code`; URL; đường dẫn; tên file; lệnh; công thức `$...$`; đích của link `[...](đích)`.
2. **Giữ nguyên khối metadata** ở đầu bài: các dòng `**Type:** …`, `**Languages:** …`, `**Prerequisites:** …`, `**Time:** …` — giữ y nguyên cả nhãn lẫn giá trị (site và pipeline parse các dòng này).
3. Giữ nguyên cấu trúc: số lượng và thứ tự heading, đoạn, bullet, bảng. Không thêm, không bớt, không gộp câu làm mất ý. Không thêm ghi chú của người dịch.
4. Dịch: heading, đoạn văn, bullet, ô bảng (trừ phần là code), text của link `[text](...)`, câu trích dẫn `>`.
5. Luôn có **khoảng trắng** giữa chữ tiếng Việt và inline code: `dùng `uv` để…`, không viết `dùng`uv`để`.
6. Giữ `**bold**` ở cùng vị trí ngữ nghĩa. Thuật ngữ in đậm lần đầu có thể ghi: **môi trường ảo (virtual environment)**.

## Giọng văn

- Xưng "bạn" với người đọc; tác giả xưng "chúng ta" (không dùng "chúng tôi").
- Văn ngắn, trực tiếp, kỹ thuật — giống bản gốc. Ưu tiên cách nói của dev Việt Nam, không dịch word-by-word.
- Thuật ngữ mà dev Việt thường để tiếng Anh thì GIỮ tiếng Anh (xem bảng). Không dịch tên sản phẩm/công cụ.

## Bảng thuật ngữ

| English | Dùng | KHÔNG dùng |
|---|---|---|
| AI engineering | AI engineering / kỹ thuật AI | |
| agent | agent | đại lý |
| API key | API key | khóa API (chấp nhận được nhưng ưu tiên API key) |
| request / response | request / response (hoặc yêu cầu / phản hồi) | |
| request body / response body | request body / response body | cơ quan yêu cầu, cơ thể phản ứng |
| raw HTTP | HTTP thô | HTTP nguyên liệu |
| rate limit | rate limit (giới hạn tần suất gọi) | giới hạn tỷ lệ |
| authentication | xác thực | |
| endpoint | endpoint | |
| environment | môi trường | |
| virtual environment | môi trường ảo (venv) | |
| package / package manager | package / trình quản lý package | |
| dependency | dependency (phụ thuộc) | |
| lockfile | lockfile | |
| runtime | runtime | thời gian chạy |
| stack (công nghệ) | stack / các tầng | gói |
| import error | lỗi import | lỗi nhập khẩu |
| broken (environment) | bị hỏng / lỗi | bị phá vỡ |
| driver | driver | trình điều khiển (chỉ khi cần) |
| tensor operation | phép toán tensor | hoạt động tensor |
| build (động từ) | build / xây dựng | |
| reproducible build | build tái lập được | |
| shell, terminal, prompt (shell) | shell, terminal, prompt | |
| alias | alias | bí danh |
| commit, branch, merge, pull request, rebase, clone, push | giữ nguyên | |
| repository / repo | repo | kho lưu trữ (chỉ lần đầu nếu cần) |
| container, image (Docker), volume, layer | container, image, volume, layer | thùng chứa, hình ảnh |
| notebook, cell, kernel | notebook, cell, kernel | |
| debug / debugger / breakpoint | debug / debugger / breakpoint | gỡ lỗi (chấp nhận cho "debugging" chung) |
| profiling / profiler | profiling / profiler | |
| bottleneck | nút thắt cổ chai / bottleneck | |
| logging | logging | |
| type hint | type hint | gợi ý kiểu |
| dataclass, decorator, generator, context manager | giữ nguyên | |
| async / await | async / await | |
| dataset | dataset / tập dữ liệu | |
| checkpoint | checkpoint | |
| fine-tune | fine-tune | |
| inference | inference (suy luận) | |
| token | token | mã thông báo |
| model | mô hình / model | |
| GPU, CUDA, MPS, VRAM | giữ nguyên | |
| cloud | cloud / đám mây | |
| permission | quyền | |
| process | tiến trình (process) | quá trình |
| Learning Objectives | Mục tiêu bài học | |
| The Problem | Vấn đề | |
| The Concept | Khái niệm | |
| Build It | Tự xây dựng | Hãy xây dựng nó |
| Use It | Ứng dụng | |
| Ship It | Đóng gói & sử dụng | |
| Exercises | Bài tập | |
| Key Terms | Thuật ngữ chính | |
| Further Reading | Đọc thêm | |

Bảng "Key Terms" thường có cột Term / What people say / What it actually means → dịch tiêu đề cột thành "Thuật ngữ / Người ta hay nói / Ý nghĩa thực sự"; giữ nguyên thuật ngữ tiếng Anh ở cột đầu.
