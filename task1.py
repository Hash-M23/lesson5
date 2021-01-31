from collections import namedtuple

Companies = namedtuple('Companies', 'name profit')
companies_total = int(input('Сколько всего предприятий:'))
total_profit = 0
companies_info = []

for i in range(companies_total):
    name = input(f'Введите название компании под номером {i + 1}: ')
    quarter_1 = float(input('Введите её прибыль за 1-ый квартал: '))
    quarter_2 = float(input('Введите её прибыль за 2-ой квартал: '))
    quarter_3 = float(input('Введите её прибыль за 3-ий квартал: '))
    quarter_4 = float(input('Введите её прибыль за 4-ый квартал: '))
    profit = (quarter_1 + quarter_2 + quarter_3 + quarter_4)
    companies_info.append(Companies(name, profit))
    total_profit += profit

avg_profit = total_profit / companies_total

print('Компании с годовой прибылью выше среднего: ')

for i in range(companies_total):
    if avg_profit < companies_info[i].profit:
        print(companies_info[i].name)

print('Компании с годовой прибылью выше среднего: ')

for i in range(companies_total):
    print('Компании с годовой прибылью ниже среднего: ')
    if avg_profit > companies_info[i].profit:
        print(companies_info[i].name)