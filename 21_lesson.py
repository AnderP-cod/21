"""1 створити клас людина і 4 похідних похідних класи з унікальними
 методами, атрибутами

Human - Adult
Human - Child


Adult - Student
Adult - Worker - Teacher
Teacher працює з студентами
"""


# отец всех классов которые будут наследоваться от Human
class Human:
    def __init__(self, ferst, last):
        """Это обекты human"""
        self.ferst = ferst
        self.last = last


class Child(Human):
    def __init__(self, ferst, last):
        super().__init__(ferst, last)


class Adult(Human):
    def __init__(self, ferst, last):
        super().__init__(ferst, last)


class Student(Adult):
    def __init__(self, ferst, last):
        super().__init__(ferst, last)

    @property
    def studen(self):  # эта функция возрошяет Student
        return f"Student {self.ferst} {self.last}"

    def __add__(self):  # этот м.м. добовляет студентов
        print("Вы хотите добавить студента")
        self.ferst = input("Введите Имя: ")
        self.last = input("Введите Фамилию: ")
        return "Вы добавили студента"

    @studen.deleter
    def studen2(self):  # эта функция удаляет студентов
        print("Удалены данные")
        self.ferst = None
        self.last = None


class Worker(Adult):
    def __init__(self, ferst, last):
        super().__init__(ferst, last)


# главная функция которая манипулирует всеми
class Techer(Worker, Student):
    def __init__(self, ferst, last, lst):
        super().__init__(ferst, last)
        self.lst = [student.studen, student2.studen, student3.studen]  # передача студентов

    @property
    def class_techer(self):  # эта функция возрошяет Techer
        return f"Techer {self.ferst} {self.last} {self.lst}"


    @property
    def techerrrr(self):  # эта функция показывает всех студентов учителя
        print("Ваши студент")
        print(student.studen)
        print(student2.studen)
        print(student3.studen)
        print(studentt.studen)
        return


student = Student("Андрей", "Линник")
student2 = Student("Юрa", "Москоленко")
student3 = Student("Влад", "Чуприна")
studentt = Student("", "")
techer2 = Techer("Андрей", "Паламарчук", [student, student2, student3])

print(techer2.class_techer)
print(techer2.techerrrr)
print(studentt.__add__())
print(techer2.techerrrr)
del student.studen2
print(student.studen2)
