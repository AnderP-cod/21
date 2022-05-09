class Human:
    def __init__(self,ferst,last):
        self.ferst = ferst
        self.last = last


class Adult(Human):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)


class Child(Human):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)


class Worker(Adult):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)


class Techer(Worker):
    def __init__(self,ferst,last):
        super().__init__(ferst,last)

    @property
    def teacherr(self):
        return f"Child {self.ferst} {self.last}"

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
