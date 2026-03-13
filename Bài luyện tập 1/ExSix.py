print("===== BÀI 6 =====")
chuoi = input("Nhập chuỗi các số cách nhau bằng dấu ; (VD: 5;7;8;-2): ")
if chuoi.strip() == "":
    chuoi = "5;7;8;-2;8;11;13;9;10"
cac_so = chuoi.split(';')
cac_so_int = []
for so in cac_so:
    try:
        cac_so_int.append(int(so.strip()))
    except ValueError:
        print(f"'{so}' không phải số hợp lệ!")

print("\nCác số trong chuỗi:")
for so in cac_so_int:
    print(so)

so_chan = 0
for so in cac_so_int:
    if so % 2 == 0:
        so_chan += 1
print(f"Số lượng số chẵn: {so_chan}")

so_am = 0
for so in cac_so_int:
    if so < 0:
        so_am += 1
print(f"Số lượng số âm: {so_am}")

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

so_nguyen_to = 0
for so in cac_so_int:
    if la_so_nguyen_to(so):
        so_nguyen_to += 1
print(f"Số lượng số nguyên tố: {so_nguyen_to}")

tong = 0
for so in cac_so_int:
    tong += so
trung_binh = tong / len(cac_so_int)
print(f"Giá trị trung bình: {trung_binh}")
print()
