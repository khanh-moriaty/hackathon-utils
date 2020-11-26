# Flow:

- BTC cung cấp file test_set.zip.
- Hệ thống sẽ giải nén test_set.zip thành thư mục test_set.
- Gọi file pre_proc.py để lọc thư mục test_set thành 3 thư mục con:
    + test_set_none.
    + test_set_square.
    + test_set_cropped.
- Tiếp đến gọi hàm predict.py với đầu vào là đường dẫn đến thư mục test_set_cropped.
- Hàm predict.py sẽ trả về đường dẫn đến 1 tệp tin submission_raw.txt.
- Đưa đường dẫn này vào file post_proc.py để hậu xử lý và trả về đường dẫn tới file submission.txt mới, kèm theo đường dẫn đến 1 file submission_viz.txt.
- Sử dụng file submission_viz.txt để hiển thị lên giao diện interactive.
- Sau khi interactive hoàn tất, tiến hành submit kết quả.