print("===== BÀI 8 =====")
while True:
    try:
        diem = float(input("Nhập điểm sinh viên (0-10): "))

        if 0 <= diem <= 10:
            print(f" Điểm {diem} hợp lệ!")
            break  # Thoát vòng lặp nếu hợp lệ
        else:
            print(" Điểm không hợp lệ! Điểm phải từ 0 đến 10.")

    except ValueError:
        print("Lỗi: Bạn phải nhập số!")
