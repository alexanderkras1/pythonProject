class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise ValueError("Нельзя добавить более 10 студентов в группу!")
        self.group.add(student)

    def delete_student(self, last_name):
        self.group = {student for student in self.group if student.last_name != last_name}

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group Number: {self.number}\nStudents:\n{all_students}"

    def __hash__(self):
        return hash(str(self))
