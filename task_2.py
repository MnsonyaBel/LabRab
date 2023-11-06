salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

minus_list = []

for months in range(9):
    spend = spend + spend*increase
    sr = salary - spend
    minus_list.append(sr)
minus_list_pr = sum(minus_list)
mm = minus_list_pr*(-1) + 1000 # +1000 т.к. в первый месяц рост цен не затрагивает траты но траты выше на 1000 чем зарплата

money_capital = round(mm, 2)
months = 10
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
