"""1 створити клас людина і 4 похідних похідних класи з унікальними методами, атрибутами

Human - Adult
Human - Child


Adult - Student
Adult - Worker - Teacher
Teacher працює з студентами

2 Переглянути magic methods, реалузувати для своїх класів"""


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
    @staticmethod
    def studentt():
        Job = input("Напишите где вы студент работаете: ")
        pay = int(input("Напишите какая у вас зарплта: "))
        return f"работа {Job}, зарплата {pay}"


class Worker(Adult):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)
    @staticmethod
    def workerr():
        Job = input("Напишите где вы работаете: ")
        pay2 = int(input("Напишите какая у вас зарплта: "))
        return f"работа {Job} , зарплата {pay2}"


class Techer(Worker,Student):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)

    def __str__(self,ferst,last):
        return f"full name {self.ferst} {self.last}"

    @property
    def techerrrr(self):
        a = Student.studentt()
        b = Worker.workerr()
        return f"Worker = {a} , Student = {b}"

    @property
    def teacherr(self):
        return f"Techer {self.ferst} {self.last}"

    @teacherr.setter
    def teacherr(self,name):
        ferst,last = name.split()
        self.ferst = ferst
        self.last = last

    @teacherr.deleter
    def teacherr(self):
        print("Удалены данные")
        self.ferst = None
        self.last = None



chldren = Techer("Андрей","Паламарчук")

print(chldren.teacherr)
print()
chldren.teacherr = 'Андрей Линник'
print(chldren.teacherr)
print()
del chldren.teacherr
print(chldren.ferst)
print(chldren.last)

print(chldren.techerrrr)
