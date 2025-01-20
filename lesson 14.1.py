class GroupLimitError(Exception):
    """Исключение, выбрасываемое при превышении лимита студентов в группе."""
    pass

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
            raise GroupLimitError("Нельзя добавить более 10 студентов в группу!")
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


# Тесты
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)  # Вывод информации о группе

# Проверка поиска студента
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Unknown') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student), 'Test3'

# Удаление студента
gr.delete_student('Taylor')
print(gr)  # Должен остаться только один студент

# Проверка лимита студентов
try:
    for i in range(11):  # Попытка добавить 11 студентов
        gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Surname{i}', f'ID{i}'))
except GroupLimitError as e:
    print(e)  # Должно выбросить ошибку
