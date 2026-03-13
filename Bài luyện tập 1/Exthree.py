print("===== BÀI 3 =====")

while True:
    so = int(input("Nhập một số từ 1 đến 9: "))

    if 1 <= so <= 9:
        break
    else:
        print("Số không hợp lệ! Vui lòng nhập lại.")

print(f"\nBảng cửu chương của {so}:")

for i in range(1, 10):
    # i sẽ chạy từ 1 đến 9
    ket_qua = so * i
    print(f"{so} x {i} = {ket_qua}")
