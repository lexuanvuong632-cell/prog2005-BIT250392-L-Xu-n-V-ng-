TEN_TEP = "sanpham.txt"
def nhap_san_pham():
    """Chức năng 1: Nhập và thêm sản phẩm mới vào tệp"""
    print("\n--- NHẬP SẢN PHẨM MỚI ---")
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")


    while True:
        try:
            gia = float(input("Nhập giá sản phẩm: "))
            break
        except ValueError:
            print("Giá phải là số. Vui lòng nhập lại!")

    # Ghi vào tệp (chế độ append - thêm vào cuối)
    with open(TEN_TEP, 'a', encoding='utf-8') as tep:
        tep.write(f"{ma};{ten};{gia}\n")

    print("Đã thêm sản phẩm thành công!")


def hien_thi_danh_sach():
    """Chức năng 2: Hiển thị danh sách sản phẩm từ tệp"""
    print("\n--- DANH SÁCH SẢN PHẨM ---")
    try:
        with open(TEN_TEP, 'r', encoding='utf-8') as tep:
            san_pham = tep.readlines()

        if not san_pham:
            print("Chưa có sản phẩm nào.")
            return []

        print(f"{'Mã':<10} {'Tên':<20} {'Giá':<10}")
        print("-" * 40)

        danh_sach = []
        for dong in san_pham:
            dong = dong.strip()
            if dong:  # Bỏ qua dòng trống
                parts = dong.split(';')
                if len(parts) == 3:
                    ma, ten, gia = parts
                    print(f"{ma:<10} {ten:<20} {float(gia):<10.1f}")
                    danh_sach.append((ma, ten, float(gia)))

        return danh_sach

    except FileNotFoundError:
        print("Tệp chưa tồn tại. Chưa có sản phẩm nào.")
        return []


def sap_xep_theo_gia():
    """Chức năng 3: Sắp xếp sản phẩm theo giá giảm dần"""
    print("\n--- SẢN PHẨM SẮP XẾP THEO GIÁ GIẢM DẦN ---")


    try:
        with open(TEN_TEP, 'r', encoding='utf-8') as tep:
            san_pham = tep.readlines()

        if not san_pham:
            print("Chưa có sản phẩm nào.")
            return


        danh_sach = []
        for dong in san_pham:
            dong = dong.strip()
            if dong:
                parts = dong.split(';')
                if len(parts) == 3:
                    ma, ten, gia = parts
                    danh_sach.append((ma, ten, float(gia)))

        if not danh_sach:
            print("Không có dữ liệu hợp lệ.")
            return


        danh_sach.sort(key=lambda sp: sp[2], reverse=True)

        # Hiển thị kết quả
        print(f"{'Mã':<10} {'Tên':<20} {'Giá':<10}")
        print("-" * 40)
        for ma, ten, gia in danh_sach:
            print(f"{ma:<10} {ten:<20} {gia:<10.1f}")

    except FileNotFoundError:
        print("Tệp chưa tồn tại. Chưa có sản phẩm nào.")


def menu_chinh():
    """Hiển thị menu chính và xử lý lựa chọn"""
    while True:
        print("\n" + "=" * 40)
        print("CHƯƠNG TRÌNH QUẢN LÝ SẢN PHẨM")
        print("=" * 40)
        print("1. Nhập sản phẩm mới")
        print("2. Hiển thị danh sách sản phẩm")
        print("3. Sắp xếp sản phẩm theo giá giảm dần")
        print("4. Thoát")
        print("-" * 40)

        lua_chon = input("Nhập lựa chọn của bạn (1-4): ")

        if lua_chon == '1':
            nhap_san_pham()
        elif lua_chon == '2':
            hien_thi_danh_sach()
        elif lua_chon == '3':
            sap_xep_theo_gia()
        elif lua_chon == '4':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")


if __name__ == "__main__":
    menu_chinh()
