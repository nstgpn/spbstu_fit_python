money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
# Определим функцию для подсчета количества месяцев, в течение которых можно обходиться без долгов.
def months_without_debt(money_capital, salary, spend, increase):
    months = 0
    while money_capital >= 0:
        # Рассчитаем бюджет текущего месяца
        budget = salary + money_capital
        # Если расходы превышают бюджет, выходим из цикла
        if spend > budget:
            break
        # Обновляем подушку безопасности, вычтя из неё расходы
        money_capital -= (spend - salary)
        # Увеличиваем расходы на следующий месяц с учетом роста цен
        spend *= (1 + increase)
        months += 1
    return months
# Рассчитаем количество месяцев
months = months_without_debt(money_capital, salary, spend, increase)
print("Количество месяцев, которое можно протянуть без долгов:", months)
