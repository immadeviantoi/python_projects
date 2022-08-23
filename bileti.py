count = int(input('Количество билетов: '))
lst = [int(input('Возраст посетителя: ')) for i in range(count)]
sum = 0
for j in lst:
    if j < 18:
        sum = sum
    elif 18 <= j <=25:
        sum += 990
    elif j > 25:
        sum += 1390
    else:
        print('Ошибка при вводе возраста посетителя')
if count > 3:
    sum = sum * 0.9
print(f'{sum} рублей к оплате')