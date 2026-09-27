# Knowledge Base — Quản lý chi phí đầu tư xây dựng

Thư mục quy định pháp lý **duy nhất và bắt buộc** làm căn cứ cho skill `kiem-tra-du-toan`.

## Quy tắc vàng
1. **Không tự bịa.** Mọi con số định mức, tỷ lệ %, đơn giá, điều khoản pháp lý xuất hiện trong kết quả thẩm tra ĐỀU phải trỏ được đến 1 file + 1 điều/khoản cụ thể trong thư mục này (hoặc trỏ đến URL nguồn nếu là số liệu cập nhật trực tuyến).
2. Nếu file knowledge thiếu nội dung cần dùng → **dừng lại**, chạy quy trình cập nhật (mục dưới), KHÔNG suy đoán từ trí nhớ.
3. Mỗi file bắt buộc có dòng `Cập nhật: YYYY-MM-DD (nguồn: URL)` ở đầu.

## Cấu trúc
| Thư mục/file | Nội dung |
|---|---|
| `phap-luat/danh-muc-van-ban.md` | DANH MỤC MASTER: toàn bộ văn bản, trạng thái hiệu lực, ngày ban hành/hiệu lực, URL nguồn, điều khoản chính. **File này đọc trước tiên mỗi lần làm việc.** |
| `phap-luat/ND-206-2026.md` | Nghị định 206/2026/NĐ-CP (hiệu lực 01/7/2026) — các điều khoản chính đã xác minh. |
| `phap-luat/ND-10-2021.md` | Nghị định 10/2021/NĐ-CP — HẾT HIỆU LỰC từ 01/7/2026. Chỉ dùng để đối chiếu dự án cũ. |
| `thong-tu/TT-11-2021-va-sua-doi.md` | Thông tư 11/2021/TT-BXD + sửa đổi bởi TT 60/2025/TT-BXD. |
| `gia/cong-bo-gia-va-dinh-muc.md` | Nguồn tra cứu giá VL/NC/CM, định mức, suất vốn đầu tư (liên kết + chu kỳ công bố). |
| `gia/cong-bo-gia-dia-phuong.md` | Bảng giá cụ thể theo địa phương (tỉnh/thành) — bổ sung khi nhận dự án ở tỉnh đó. |

## Quy trình cập nhật (thực hiện thường xuyên)
1. Chạy `python scripts/cap-nhat-van-ban.py` (nằm ở thư mục gốc skill) — script kiểm tra các URL nguồn và in ra bảng trạng thái.
2. Khi phát hiện văn bản mới/bổ sung (Nghị định, Thông tư sửa đổi, Công bố giá):
   - Dùng `web_search` + `web_extract` lấy nội dung từ **nguồn chính thống**: vanban.chinhphu.vn, moj.gov.vn, bxd.gov.vn, congbao.chinhphu.vn, cổng TTĐT tỉnh.
   - Cập nhật `danh-muc-van-ban.md` (trạng thái hiệu lực) + file chi tiết tương ứng.
   - Ghi nhận ngày cập nhật + URL tại đầu file.
3. **Chu kỳ đề nghị:** kiểm tra `danh-muc-van-ban.md` trước MỖI lần nhận hồ sơ dự toán mới (đã nhúng vào Phase 0 của skill).

## Trạng thái pháp lý hiện hành (xác minh 27/09/2026)
- **Luật Xây dựng 135/2025/QH15** — hiệu lực 01/7/2026 (thay thế Luật 50/2014/QH13).
- **Nghị định 206/2026/NĐ-CP** — ban hành 15/6/2026, hiệu lực 01/7/2026, **thay thế Nghị định 10/2021/NĐ-CP** (Điều 38.3 NĐ 206).
- **Thông tư 11, 12, 13/2021/TT-BXD** — vẫn hiệu lực, đã được sửa đổi bởi **Thông tư 60/2025/TT-BXD** (ban hành 30/12/2025, hiệu lực 15/02/2026).
- Chi tiết + URL: xem `phap-luat/danh-muc-van-ban.md`.
