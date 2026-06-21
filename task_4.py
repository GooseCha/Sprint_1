new_tasks = ["task_001", "task_011", "task_007", "task_015", "task_005"]
completed_tasks = ["task_002", "task_012", "task_006"]

completed_tasks.append(new_tasks.pop(new_tasks.index("task_005")))
# С помощью index узнаем номер таска в списке. С помощью pop по индексу (номеру в списке) удаляем и копируем нужный нам таск. С помощью append переносим его в completed tasks

new_tasks.remove("task_007")

print(new_tasks[len(new_tasks) - 1])
# Т.к. len даст нам количество элементов в спике, а первый элемент имеет 0 номер, надо вычесть один из длинны списка. ИИ потом напомнил что можно использовать отрицательный индекс, но решил оставить свое решение

print(new_tasks)  # Для проверки выполнения задачи вывожу оба списка
print(completed_tasks)
