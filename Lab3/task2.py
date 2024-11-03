def find_common_participants(group1, group2, delimiter=','):
    # Разделение строк на списки фамилий
    set1 = set(group1.split(delimiter))
    set2 = set(group2.split(delimiter))

    # Нахождение общих участников и сортировка результата
    common_participants = sorted(set1.intersection(set2))

    return common_participants


# Пример использования функции с разделителем '|'
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции
common = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники:", common)
