# -*- coding: utf-8 -*-
"""
cap-nhat-van-ban.py — Kiểm tra trạng thái các nguồn văn bản pháp lý
dùng cho skill kiem-tra-du-toan.

Chạy:  python scripts\\cap-nhat-van-ban.py
Kết quả: bảng trạng thái từng nguồn (HTTP OK / lỗi), gợi ý khi phát hiện
văn bản thay thế mới hơn. KHÔNG tự sửa file — chỉ báo cáo để người vận hành
cập nhật knowledge/ theo quy trình trong knowledge/README.md.
"""
import re
import sys
import urllib.request
from datetime import datetime

# (Tên, URL nguồn chính thống)
NGUON = [
    ("NĐ 206/2026/NĐ-CP (hiện hành)",
     "https://vanban.chinhphu.vn/?pageid=27160&docid=218454"),
    ("NĐ 10/2021/NĐ-CP (đã thay thế — đối chiếu dự án cũ)",
     "https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=202663"),
    ("Luật Xây dựng 135/2025/QH15",
     "https://vanban.chinhphu.vn/?pageid=27160&docid=216514&classid=1&typegroupid=3"),
    ("TT 60/2025/TT-BXD (sửa TT 11/12/13/14-2021)",
     "https://vanban.chinhphu.vn/?pageid=27160&docid=216436"),
    ("PDF gốc TT 60/2025/TT-BXD",
     "https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/60-bxd.pdf"),
    ("TT 11/2021/TT-BXD",
     "https://luatvietnam.vn/xay-dung/thong-tu-11-2021-tt-bxd-208906-d1.html"),
    ("TT 12/2021/TT-BXD",
     "https://luatvietnam.vn/xay-dung/thong-tu-12-2021-tt-bxd-208840-d1.html"),
    ("TT 13/2021/TT-BXD",
     "https://luatvietnam.vn/xay-dung/thong-tu-13-2021-tt-bxd-208825-d1.html"),
    ("TT 14/2023/TT-BXD (sửa TT 11/2021)",
     "https://luatvietnam.vn/xay-dung/thong-tu-14-2023-tt-bxd-sua-doi-mot-so-dieu-cua-thong-tu-11-2021-tt-bxd-290126-d1.html"),
    ("TT 01/2025/TT-BXD (sửa TT 11/2021)",
     "https://chinhphu.vn/?pageid=27160&docid=212647"),
]

# Mẫu dò "dấu hiệu thay thế" trong trang: văn bản mới hơn thay thế văn bản cũ
DANG_DAU_THAY_THE = re.compile(
    r"(thay thế|bãi bỏ|hết hiệu lực|sửa đổi, bổ sung)", re.I)
MAU_SO_ND = re.compile(r"Nghị\s*định\s*số\s*(\d{1,4})\s*/\s*(\d{4})\s*/\s*NĐ-CP")
MAU_SO_TT = re.compile(r"Thông\s*tư\s*số\s*(\d{1,2})\s*/\s*(\d{4})\s*/\s*TT-?BXD")

UA = {"User-Agent": "Mozilla/5.0 (HermesAgent/1.0; cap-nhat-van-ban)"}


def kiem_tra(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(400_000).decode("utf-8", "ignore")
            return r.status, body
    except Exception as e:  # noqa: BLE001
        return None, str(e)


def can_bao():
    print(f"Kiểm tra nguồn văn bản — {datetime.now():%Y-%m-%d %H:%M}\n")
    ok = loi = 0
    for ten, url in NGUON:
        status, body = kiem_tra(url)
        if status in (200, 206):
            ok += 1
            doi = ""
            if "chinhphu" in url or "luatvietnam" in url:
                th = DANG_DAU_THAY_THE.search(body)
                if th:
                    # lấy số NĐ/TT lớn nhất năm 2026+ để gợi ý
                    nd = [(int(n), int(y)) for n, y in MAU_SO_ND.findall(body)]
                    tt = [(int(n), int(y)) for n, y in MAU_SO_TT.findall(body)]
                    cand = sorted(set(nd + tt), reverse=True)[:3]
                    if cand:
                        doi = "  ⚠ trang có đề cập thay đổi — xem: " + \
                              ", ".join(f"{n}/{y}" for n, y in cand)
            print(f"[OK {status}] {ten}{doi}")
        else:
            loi += 1
            print(f"[LỖI {status}] {ten}\n        {url}\n        {body[:120]}")
    print(f"\nTóm tắt: {ok} nguồn khả dụng / {loi} lỗi. Tổng nguồn: {len(NGUON)}")
    if loi:
        print("Khuyến nghị: kiểm tra lại nguồn lỗi bằng trình duyệt trước khi dùng cho báo cáo.")
    return 0 if loi == 0 else 1


if __name__ == "__main__":
    sys.exit(can_bao())
