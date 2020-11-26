# Flow:

- BTC cung cấp file <b>test_set.zip</b>.
- Hệ thống sẽ giải nén <b>test_set.zip</b> thành thư mục <b>test_set</b>.
- Gọi file <b>pre_proc.py</b> để lọc thư mục test_set thành 3 thư mục con:
    + <b>test_set_none</b>.
    + <b>test_set_square</b>.
    + <b>test_set_cropped</b>.
- Tiếp đến gọi hàm <b>predict.py</b> với đầu vào là đường dẫn đến thư mục <b>test_set_cropped</b>.
- Hàm <b>predict.py</b> sẽ trả về đường dẫn đến 1 tệp tin <b>submission_raw.txt</b>.
- Đưa đường dẫn này vào file <b>post_proc.py</b> để hậu xử lý và trả về đường dẫn tới file <b>submission.txt</b> mới, kèm theo đường dẫn đến 1 file <b>submission_viz.txt</b>.
- Sử dụng file <b>submission_viz.txt</b> để hiển thị lên giao diện interactive.
- Sau khi interactive hoàn tất, tiến hành submit kết quả.
- Nếu xảy ra trục trặc gì trong quá trình interactive, có thể nộp tạm file submission đã qua post_proc.