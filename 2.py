# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

n = int(input("Введите длину списка: "))
list = [random.randint(1, 100) for _ in range(n)]
print(list)
desired_num = int(input("Введите искомое число: "))

closest = list[0]
count = 0

for num in list:
    if num == desired_num:
        count += 1
    if abs(num - desired_num) < abs(closest - desired_num):
        closest = num

print(f"Число {desired_num} встречается в списке {count} раз(а)")
print(f"Ближайшее число к {desired_num} в списке: {closest}")
