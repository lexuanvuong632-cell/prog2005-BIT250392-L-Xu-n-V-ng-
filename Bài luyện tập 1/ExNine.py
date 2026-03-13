class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
    def display(self):
        print(f"Sinh viên {self.ten} có điểm là {self.diem}")


print("===== BÀI 9 =====")
sv1 = Student("Nguyễn Văn An", 8.5)
sv2 = Student("Trần Thị Bình", 9.0)

sv1.display()
sv2.display()
