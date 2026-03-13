class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

sv1 = Student("Nguyễn Văn An", 8.5)
sv2 = Student("Trần Thị Bình", 9.0)

print("===== BÀI 7 =====")
print("Thông tin sinh viên 1:")
print(f"Tên: {sv1.ten}")
print(f"Điểm: {sv1.diem}")

print("\nThông tin sinh viên 2:")
print(f"Tên: {sv2.ten}")
print(f"Điểm: {sv2.diem}")
