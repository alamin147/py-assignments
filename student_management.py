class StudentDatabase:
    student_list = []

    def __init__(self):
        pass

    @classmethod
    def add_student(cls, s):
        for student in cls.student_list:
            if student._student_id == s._student_id:
                print(f"Student id-{s._student_id} already exists")
                return False
        cls.student_list.append(s)
        print("Student added")
        return True

    @classmethod
    def students_info(cls):
        if not cls.student_list:
            print("No students found")
            return
        for student in cls.student_list:
            print(f"ID: {student._student_id}, Name: {student._name}, Department: {student._department}, Enrolled: {student._is_enrolled}")


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self._student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self._is_enrolled:
            print(f"Student {self._name} is already enrolled")
            return False
        else:
            self._is_enrolled = True
            print(f"Student {self._name} has been enrolled")
            return True

    def drop_student(self):
        if not self._is_enrolled:
            print(f"Student {self._name} is not currently enrolled")
            return False
        else:
            self._is_enrolled = False
            print(f"Student {self._name} has been dropped")
            return True

    def view_student_info(self):
        print(f"ID: {self._student_id}, Name: {self._name}, Department: {self._department}, Enrolled: {self._is_enrolled}")


s1 = Student(1, "Alice", "CSE", True)
s2 = Student(2, "Bob", "EEE", False)
s3 = Student(3, "Charlie", "BBA", True)

while True:
    print("\n" + "="*30)
    print("Student Management System")
    print("="*30)
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n--- All Students ---")
            StudentDatabase.students_info()

        elif choice == 2:
            try:
                enroll_id = int(input("Enter student id to enroll: "))
                student_found = False
                for student in StudentDatabase.student_list:
                    if student._student_id == enroll_id:
                        student.enroll_student()
                        student_found = True
                        break
                if not student_found:
                    print(f"Invalid student ID: {enroll_id}")
            except ValueError:
                print("Invalid input! Please enter a valid student ID.")

        elif choice == 3:
            try:
                drop_id = int(input("Enter student id to drop: "))
                student_found = False
                for student in StudentDatabase.student_list:
                    if student._student_id == drop_id:
                        student.drop_student()
                        student_found = True
                        break
                if not student_found:
                    print(f"Invalid student ID: {drop_id}")
            except ValueError:
                print("Invalid input! Please enter a valid student ID.")

        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Wrong choice! Please try again.")

    except ValueError:
        print("Invalid input! Please enter a number between 1-4.")
