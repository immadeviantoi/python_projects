per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму вашего депозита '))
deposit = list(per_cent.values())
for i in range(len(deposit)):
    deposit[i] = money + money / 100 * deposit[i]
print('Список депозит - значений - ', deposit, '.', 'Максимальная сумма, которую вы можете заработать — ', int(max(deposit)))