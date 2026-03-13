print("===== BÀI 2 =====")

# Thử với giá trị mặc định trước
print("Thử với số mặc định: a=10, b=3")
a = 10
b = 3
print(f"Lũy thừa: {a}^{b} = {a ** b}")
print(f"Căn bậc 2 của {a} = {a ** 0.5}")
print(f"Chia lấy phần nguyên: {a} // {b} = {a // b}")
print(f"Chia lấy phần dư: {a} % {b} = {a % b}")
print()

try:
    so1 = float(input("Nhập số thứ nhất: "))
    so2 = float(input("Nhập số thứ hai: "))

    print(f"\nLũy thừa: {so1}^{so2} = {so1 ** so2}")
    print(f"Căn bậc 2 của {so1} = {so1 ** 0.5}")
    print(f"Căn bậc 2 của {so2} = {so2 ** 0.5}")
    print(f"Chia lấy phần nguyên: {so1} // {so2} = {so1 // so2}")
    print(f"Chia lấy phần dư: {so1} % {so2} = {so1 % so2}")
    print(f"Làm tròn {so1} = {round(so1)}")
    print(f"Làm tròn {so2} = {round(so2)}")
except ValueError:
    print("Lỗi: Bạn phải nhập số!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
