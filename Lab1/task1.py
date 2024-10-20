numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# Находим индекс элемента со значением None
none_index = numbers.index(None)
# Вычисляем сумму всех элементов, исключая None
sum_without_none = sum(x for x in numbers if x is not None)
# Общее количество элементов (включая None)
total_count = len(numbers)
# Вычисляем среднее арифметическое
average = sum_without_none / total_count
# Заменим пропущенный элемент на среднее арифметическое
numbers[none_index] = average
print("Измененный список:", numbers)