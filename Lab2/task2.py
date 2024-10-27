salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
# Определим функцию для расчета необходимой подушки безопасности, чтобы прожить заданное количество месяцев.
def required_safety_cushion(salary, spend, months, increase):
    money_capital_needed = 0
    for month in range(months):
        # Рассчитываем дефицит в текущем месяце (если он есть)
        deficit = spend - salary
        if deficit > 0:
            money_capital_needed += deficit
        # Увеличиваем расходы на следующий месяц с учетом роста цен
        spend *= (1 + increase)
    return round(money_capital_needed)
# Рассчитаем необходимую подушку безопасности
money_capital_needed = required_safety_cushion(salary, spend, months, increase)# Вывод результата
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital_needed}")