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
    def studen(self):
        return f"Student {self.ferst} {self.last}"

    @property
    def techerrrr(self):
        print("Ваши студент")
        print(student.studen)
        print(student2.studen)
        return student3.studen

    @studen.deleter
    def studen(self):
        print("Удалены данные")
        self.ferst = None
        self.last = None

techer = Techer("Андрей","Паламарчук")
student = Student("Андрей","Линник")
student2 = Student("Юрa","Москоленко")
student3 = Student("Влад","Чуприна")


print(techer.teacherr)
print(techer.techerrrr)


def techer5():
    item = int(input("Выберите что вы хотите сделать 1) добавить студента 2) удалить студента: "))
    if item == 1:
        student4 = Student(input("Ведите имя студента: "), input("Ведите фамилию студента: "))
        return student4.studen
    elif item == 2:
        print("Кого вы хотите удалить")
        item2 = int(input("1) Андрей Линник , 2)Юрa Москоленко , 3)Влад Чуприна : "))
        if item2 == 1:
            del student.studen
            print(student.ferst)
            print(student.last)
        elif item2 == 2:
            del student2.studen
            print(student2.ferst)
            print(student2.last)
        elif item2 == 3:
            del student3.studen
            print(student3.ferst)
            print(student3.last)
        else:
            print("Ошибка")
    else:
        print("Ошибка")

print(techer5())