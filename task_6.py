types = {1: "Блокирующий", 2: "Критический", 3: "Значительный", 4: "Незначительный", 5: "Тривиальный"}

tickets = {1: ["API_45", "API_76", "E2E_4"], 2: ["UI_19", "API_65", "API_76", "E2E_45"], 3: ["E2E_45", "API_45", "E2E_2"], 4: ["E2E_9", "API_76"], 5: ["E2E_2", "API_61"]}


def types_of_tickets(types, tickets):
    for key, value in types.items():
        tickets[value] = tickets.pop(key)  # Спросил у ИИ "напомни как менять название ключа в словаре". Он мне показал только конструкцию d['new_key'] = d.pop('old_key'). Остальное сам понял и догадался как с этим работать


def delete_duplicates(tickets):  # В задании написано сначала удалить дубли, потом связать уровень критичности с другим списком. Поэтому я сделал поиск по ключам 1-5, а не "Блокирующий" - "Тривиальный"
    for key in tickets.keys():
        lst = tickets[key]
        for i in range(int(key) + 1, len(tickets) + 1):
            for element in lst:
                if element in tickets[i]:
                    tickets[i].remove(element)


delete_duplicates(tickets)
types_of_tickets(types, tickets)
print(tickets)
