---
name: kiem-tra-du-toan
description: Kiểm tra bảng tính dự toán, khối lượng, đơn giá và định mức.
version: 0.2.0
author: Anh Vũ (anhvuxd), Hermes Agent
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [du-toan, xay-dung, khoi-luong, don-gia, dinh-muc, excel]
    related_skills: [xlsx]
---

# Kỹ năng Kiểm tra Dự toán Xây dựng (kiem-tra-du-toan)

Quy trình 6 phase kiểm tra/thẩm tra hồ sơ dự toán công trình. **Nguyên tắc cốt lõi: mọi số định mức, tỷ lệ %, đơn giá, điều khoản trích trong kết quả ĐỀU phải trỏ được đến file trong `knowledge/` (kèm điều/khoản/URL). Không có trong knowledge → không được tự bịa, ghi vào mục "Cần tra cứu" của báo cáo.**

## Khi nào dùng
- Nhận hồ sơ dự toán (Excel/bảng biểu) cần rà soát trước khi duyệt, đấu thầu, thẩm tra.
- Đối chiếu khối lượng bóc tách với bảng tiên lượng.
- Kiểm tra mã định mức, đơn giá, giá VL/NC/CM, bảng tổng hợp chi phí.
- **Không dùng cho:** thiết kế kết cấu, tính toán sức bền.

## Quy tắc tham chiếu (bắt buộc mọi phase)
1. `knowledge/phap-luat/danh-muc-van-ban.md` là **file đọc trước tiên** mỗi lần làm việc.
2. Trích dẫn theo mẫu: `[Tên file knowledge | Điều X khoản Y]` hoặc `[Tên file | Bảng X Phụ lục Y, URL]`.
3. Văn bản đánh dấu ❓ trong danh mục: chạy `python scripts/cap-nhat-van-ban.py` (từ thư mục gốc skill) hoặc `web_search` xác minh trước khi trích.
4. Nguồn bổ sung ngoài knowledge (giá địa phương, thuế...) phải ghi URL + ngày truy cập vào báo cáo.

## Phase 0 — Kiểm tra căn cứ pháp lý (LUÔN làm trước, không bỏ qua)
1. Đọc `knowledge/phap-luat/danh-muc-van-ban.md`. Nếu dòng `Cập nhật:` ở đầu file cách nay **> 30 ngày** → chạy `python scripts/cap-nhat-van-ban.py` và đối chiếu kết quả, cập nhật file nếu có thay đổi (theo quy trình trong `knowledge/README.md`).
2. Xác định thời điểm áp dụng pháp luật của dự án:
   - Phê duyệt **trước 01/7/2026** → NĐ 10/2021 (+NĐ 35/2023, NĐ 144/2025) + Luật 50/2014 (sửa đổi).
   - Phê duyệt **từ 01/7/2026** → NĐ 206/2026 + Luật 135/2025/QH15.
   - Định mức/giá công bố trước 01/7/2026 vẫn dùng đến khi có bản mới ([ND-206-2026.md | Điều 36.7]).
3. Đọc phần "Căn cứ pháp lý" trong hồ sơ dự toán; đối chiếu từng văn bản với danh mục: văn bản nào **không có** trong danh mục hoặc **sai hiệu lực** → đánh dấu ngay, đây là lỗi hệ thống của hồ sơ.
**Hoàn tất khi:** đã chốt bộ NĐ/TT áp dụng và đã đánh dấu toàn bộ văn bản hồ sơ "khớp/không khớp" với danh mục.

## Phase 1 — Thông tin chung & danh mục đầu việc
1. Kiểm tra: loại/cấp công trình, địa điểm, nguồn vốn, thời điểm lập dự toán, tên chủ đầu tư/tư vấn (ghi vào báo cáo).
2. Rà soát danh mục công tác: sót/trùng (ví dụ có bê tông móng mà thiếu đào đất, ván khuôn; chi phí đã nằm trong định mức/cp chung lại lập mã riêng).
3. Kiểm tra cấu trúc bảng tổng hợp đúng pháp luật áp dụng:
   - NĐ 206: cấu trúc CP xây dựng theo [ND-206-2026.md | Điều 12] (cp trực tiếp; cp gián tiếp = cp chung + cp một số công việc không xác định được KL; TNCSTTTT; VAT; nhà tạm).
   - NĐ 10: theo [ND-10-2021.md | Điều 12.2].
**Hoàn tất khi:** danh mục công tác đã rà đủ, cấu trúc bảng khớp pháp luật áp dụng.

## Phase 2 — Kiểm tra đo bóc khối lượng (căn cứ: TT 13/2021/TT-BXD)
1. Đơn vị tính (ĐVT): đối chiếu ĐVT mã định mức với đơn vị khối lượng nhập (bẫy: `100m³` vs `m³`, `10m³`, `1 tấn`).
2. Công thức diễn giải: D×R×C×số cấu kiện; khớp với bản vẽ/thuyết minh khi được cung cấp.
3. Quy tắc chuyên ngành (đánh dấu cần xem xét, KHÔNG tự tính thay):
   - Đào đắp: hệ số nở rời, taluy, tỷ lệ máy/thủ công.
   - Bê tông: đã trừ giao cắt dầm–cột–sàn, lỗ rỗng chưa.
   - Cốt thép: ước lượng thép/1m³ bê tông theo loại kết cấu (giá trị ước lượng phải ghi rõ là ước lượng kinh nghiệm, không phải định mức).
   - Ván khuôn: diện tích tiếp xúc.
4. Lỗi số học: kiểm tra lại phép nhân tổng hợp từng dòng bằng script (`openpyxl`/`pandas`) khi có file Excel.
**Hoàn tất khi:** từng dòng KL đã kiểm ĐVT + diễn giải; sai số học được liệt kê kèm số dòng.

## Phase 3 — Kiểm tra định mức & đơn giá (căn cứ: TT 12/2021 + TT 60/2025)
1. Mã hiệu: công nghệ thi công khớp thực tế không (ép cọc máy ép tải vs robot; sơn 1 lót 2 phủ; mác bê tông; cự ly vận chuyển; loại xe).
2. Cấp phối: xi măng PCB30/40; cỡ hạt đá (1x2, 2x4, 4x6); cát m-2,0/m-1,5 — đối chiếu với thuyết minh.
3. Hao phí máy: đối chiếu Phụ lục V TT 13/2021 (+bổ sung TT 60/2025, xem [TT-11-2021-va-sua-doi.md | Điều 2, Điều 3]) khi có trong knowledge; chưa có → ghi "cần tra Phụ lục V TT 13/2021 mã M....".
4. Định mức mới/điều chỉnh: yêu cầu danh mục + phương pháp xác định theo [ND-10-2021.md | Điều 21] / [ND-206-2026.md | Điều 20.5].
**Hoàn tất khi:** từng mã công tác đã chấm "đúng/sai/cần tra" kèm căn cứ file.

## Phase 4 — Kiểm tra giá VL, NC, ca máy
1. Theo [cong-bo-gia-va-dinh-muc.md]: giá VL phải đúng công bố của tỉnh **đúng kỳ/tháng** tại thời điểm lập DT; không có trong công bố → yêu cầu 3 báo giá/hóa đơn (ghi căn cứ).
2. Có file `knowledge/gia/cong-bo-gia-dia-phuong.md` cho tỉnh của dự án → đối chiếu trực tiếp từng mã vật tư. **Chưa có** → tải công bố mới nhất từ cổng TTĐT/Sở XD tỉnh, điền vào file (kèm URL + ngày), sau đó đối chiếu.
3. Nhân công: đúng nhóm–vùng theo QĐ UBND tỉnh. Ca máy: định mức hao phí × nguyên giá + bù nhiên liệu.
4. Cự ly vận chuyển: khớp thực tế công trường ↔ nguồn cung.
**Hoàn tất khi:** bảng giá đã đối chiếu hết; chênh lệch > ngưỡng (đề xuất: |Δ|>5% hoặc lệch kỳ công bố) được liệt kê kèm nguồn giá hai bên.

## Phase 5 — Kiểm tra tổng hợp kinh phí & hệ số
1. Công thức từng bảng khớp cấu trúc Phase 1; hệ số %:
   - CP chung, TNCSTTTT, nhà tạm: Bảng 3.x Phụ lục III TT 11/2021 (sửa bởi TT 60/2025) — chỉ trích giá trị có trong [TT-11-2021-va-sua-doi.md]; chưa có dòng trong file → tra PDF gốc (URL đầu file) trước khi dùng.
   - CP QLDA, CP tư vấn: Phụ lục VIII TT 12/2021 (công thức nội suy (1), bảng 2.3a/2.3b xem [TT-11-2021-va-sua-doi.md | Điều 2]).
2. VAT: đúng thuế suất tại thời điểm (tra văn bản thuế nếu knowledge chưa có — ghi URL).
3. Dự phòng: tỷ lệ % × đúng cơ số (NĐ 206 Điều 6.3g / NĐ 10 Điều 6.3g, 12.7).
4. Tổng mức: đủ 7 khoản chi phí ([ND-206-2026.md | Điều 5] hoặc [ND-10-2021.md | Điều 5.2]).
**Hoàn tất khi:** từng hệ số đã đối chiếu với file knowledge; chênh lệch % được tính lại độc lập bằng script khi có Excel.

## Phase 6 — Kỹ thuật Excel & Báo cáo
1. Lỗi công thức `#REF! #VALUE! #DIV/0! #N/A`; link giữa sheets (DT chi tiết → tổng hợp VL → chênh lệch giá → tổng hợp kinh phí); vùng `SUM()` có sót dòng chèn; sai lệch do làm tròn giữa các sheet.
2. Xuất **BÁO CÁO KIỂM TRA DỰ TOÁN** (bắt buộc đủ 5 phần):
   1. *Thông tin chung:* tên công trình, loại/cấp, nguồn vốn, thời điểm lập, bộ pháp lý áp dụng (kết quả Phase 0).
   2. *Bảng chênh lệch:*
      | STT | Hạng mục/Công tác | Theo hồ sơ | Sau kiểm tra | Δ (+/−) | Căn cứ (file knowledge + Điều/khoản/URL) |
   3. *Danh sách tồn tại theo nhóm:* pháp lý (P0), khối lượng (P2), định mức (P3), giá (P4), hệ số (P5), kỹ thuật Excel (P6) — mỗi lỗi 1 dòng, kèm mức độ (trọng yếu/nhẹ).
   4. *Mục "Cần tra cứu":* mọi điểm đã ghi "cần tra" ở các phase + lý do (thiếu trong knowledge) + nguồn đề xuất tra.
   5. *Kết luận & kiến nghị:* giá trị đề nghị duyệt (nếu đủ căn cứ) hoặc danh mục việc bên lập dự toán phải giải trình/chỉnh sửa.
3. Kiểm tra lại báo cáo: mọi số trong bảng chênh lệch đều có cột căn cứ; không có con số nào không truy về được file/URL.
**Hoàn tất khi:** báo cáo 5 phần đầy đủ, mục "Cần tra cứu" được nêu rõ, file knowledge đã cập nhật (giá mới/cập nhật văn bản) nếu có thay đổi trong quá trình.

## Bẫy thường gặp (kiểm tra chéo ở mọi phase)
- Nhầm ĐVT (×100 lần) — Phase 2.
- Tính trùng cp gián tiếp (vận chuyển nội bộ, bơm nước đã trong định mức/cp chung) — Phase 1/3.
- Nhầm loại/cấp công trình → sai hệ số — Phase 5.
- Giá chưa bù chênh lệch mà đã đưa vào tổng hợp — Phase 4/5.
- Hồ sơ cũ (2021–2025) mà nhân viên lập tự ý "cập nhật" theo NĐ 206/2026 khi chưa đủ điều kiện chuyển tiếp — Phase 0.
