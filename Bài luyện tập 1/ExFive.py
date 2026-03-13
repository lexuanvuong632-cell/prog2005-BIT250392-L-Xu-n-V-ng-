print("===== BÀI 5 =====")
import random

M = int(input("Nhập số hàng M: "))
N = int(input("Nhập số cột N: "))

ma_tran = []
for i in range(M):
    hang = []
    for j in range(N):
        hang.append(random.randint(0, 99))
    ma_tran.append(hang)

print("\nMa trận vừa tạo:")
for hang in ma_tran:
    for phan_tu in hang:
        print(f"{phan_tu:3}", end=" ")
    print()

while True:
    hang_so = int(input(f"\nNhập số hàng cần hiển thị (1-{M}): "))
    if 1 <= hang_so <= M:
        break
    print(f"Hàng không hợp lệ! Vui lòng nhập từ 1 đến {M}.")

print(f"Hàng {hang_so}: {ma_tran[hang_so - 1]}")

while True:
    cot_so = int(input(f"Nhập số cột cần hiển thị (1-{N}): "))
    if 1 <= cot_so <= N:
        break
    print(f"Cột không hợp lệ! Vui lòng nhập từ 1 đến {N}.")

cot = []
for i in range(M):
    cot.append(ma_tran[i][cot_so - 1])
print(f"Cột {cot_so}: {cot}")

gia_tri_lon_nhat = ma_tran[0][0]
for i in range(M):
    for j in range(N):
        if ma_tran[i][j] > gia_tri_lon_nhat:
            gia_tri_lon_nhat = ma_tran[i][j]

print(f"Giá trị lớn nhất trong ma trận: {gia_tri_lon_nhat}")
print()
