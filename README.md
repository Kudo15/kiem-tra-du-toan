# Skill: Kiểm tra, thẩm tra, thẩm định dự toán xây dựng công trình

Skill chuyên dụng cho **Hermes Agent** phục vụ công tác kiểm tra, rà soát, thẩm tra và thẩm định bảng tính dự toán, khối lượng, đơn giá, định mức và các khoản mục chi phí đầu tư xây dựng công trình theo đúng quy định pháp luật Việt Nam.

## 1. Cấu trúc thư mục

```
kiem-tra-du-toan/
├── SKILL.md                          # Quy trình 7 bước (Phase 0 -> Phase 6) & hướng dẫn vận hành
├── README.md                         # Giới thiệu tổng quan repository
├── .gitignore                        # Cấu hình bỏ qua các file tạm
├── knowledge/                        # Hệ thống căn cứ pháp lý & quy định hiện hành
│   ├── README.md                     # Quy tắc vàng: Không tự bịa, luôn dẫn nguồn
│   ├── phap-luat/                    # Luật, Nghị định (NĐ 10/2021, NĐ 206/2026...)
│   │   ├── danh-muc-van-ban.md       # Danh mục Master quản lý hiệu lực văn bản
│   │   ├── ND-10-2021.md
│   │   └── ND-206-2026.md
│   ├── thong-tu/                     # Thông tư quản lý chi phí & định mức
│   │   └── TT-11-2021-va-sua-doi.md  # TT 11/2021 và các nội dung sửa đổi tại TT 60/2025
│   └── gia/                          # Hướng dẫn công bố giá & dữ liệu địa phương
│       ├── cong-bo-gia-va-dinh-muc.md
│       └── cong-bo-gia-dia-phuong.md
├── scripts/                          # Script hỗ trợ tự động hóa
│   └── cap-nhat-van-ban.py           # Script tự động rà soát trạng thái hiệu lực văn bản pháp luật
└── output/                           # Thư mục lưu trữ báo cáo thẩm tra và bảng tính kết quả
    ├── Bao_cao_tham_tra_du_toan_...docx
    └── Bang_so_lieu_kiem_tra_du_toan_...xlsx
```

## 2. Quy trình kiểm tra 7 bước (Phase 0 đến Phase 6)

- **Phase 0:** Kiểm tra tính hiện hành và hiệu lực của văn bản quy phạm pháp luật.
- **Phase 1:** Kiểm tra cấu trúc tổng dự toán, TMĐT và ranh giới phân chia gói thầu.
- **Phase 2:** Kiểm tra đo bóc khối lượng, ranh giới và giao cắt giữa các hạng mục.
- **Phase 3:** Kiểm tra mã hiệu định mức, cấp phối và biện pháp thi công.
- **Phase 4:** Kiểm tra đơn giá vật tư, nhân công, giá ca máy và thiết bị.
- **Phase 5:** Kiểm tra định mức tỷ lệ %, chi phí gián tiếp, chi phí QLDA, tư vấn và dự phòng phí.
- **Phase 6:** Kiểm tra kỹ thuật lập bảng tính, lỗi liên kết Excel và lỗi đọc số tiền thành chữ.

## 3. Bản quyền & Tác giả

- **Phát triển cho:** Hermes Agent (Nous Research)
- **Tác giả:** Kudo15
- **Giấy phép:** MIT
