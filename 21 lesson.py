"""1 створити клас людина і 4 похідних похідних класи з унікальними методами, атрибутами

Human - Adult
Human - Child


Adult - Student
Adult - Worker - Teacher
Teacher працює з студентами

2 Переглянути magic methods, реалузувати для своїх класів"""
import random


class Human:
    def __init__(self,ferst,last):
        self.ferst = ferst
        self.last = last


class Child(Human):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)
    def children(self,age):
        self.age = int(input("Напишите сколько лет ученику: "))
        return f"{ferst} {last} {self.age}"


class Adult(Human):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)


class Student(Adult):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)

    @property
    def studen(self):
        return f"Student {self.ferst} {self.last}"

    def __add__(self):
        print("Вы хотите добавить студента")
        self.ferst = input("Введите Имя: ")
        self.last = input("Введите Фамилию: ")
        return "Вы добавили студента"

    @studen.deleter
    def studen(self):
        print("Удалены данные")
        self.ferst = None
        self.last = None


class Worker(Adult):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)


class Techer(Worker,Student):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)

    @property
    def teacherr(self):
        return f"Techer {self.ferst} {self.last}"

    @property
    def techerrrr(self):
        print("Ваши студент")
        print(student.studen)
        print(student2.studen)
        print(student3.studen)
        print(studentt.studen)
        return


techer = Techer("Андрей","Паламарчук")
student = Student("Андрей","Линник")
student2 = Student("Юрa","Москоленко")
student3 = Student("Влад","Чуприна")
studentt = Student("","")

print(techer.teacherr)
print(techer.techerrrr)
print(studentt.__add__())
print(techer.techerrrr)
del student.studen
print(student.studen)

