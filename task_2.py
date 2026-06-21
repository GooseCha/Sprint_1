class Tester:
    def __init__(self, name):  # был пропущен self
        self.name = name  # Так же был пропущен self, еще и присваиваился deadline, который всегда становился True

    def work_hard(self, deadline):  # deadline почему-то всегда присваивался True. Убрал это
        if deadline:  # Здесь self для переменной не нужен. Мы просто проверяем deadline, который мы задали в метод
            print(self.name, "Что ж, ещё часок поработаю!")
        else:
            print(self.name, "Можно отдыхать")


tester_1 = Tester(name="tester_1")
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name="tester_2")
tester_2.work_hard(deadline=True)  # 'tester_2 Что ж, ещё часок поработаю!'
