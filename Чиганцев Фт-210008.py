import logging
from random import randint # Подключение модуля для работы со случайной генерацией чисел
logging.basicConfig(filename = 'py.log', level = logging.INFO)
while True: # Цикл обработки ввода целого числа
    try:
        N = int(input('Введите целое число - количество бочонков: '))
        break
    except ValueError:
        print('Ошибка ввода. Попробуйте еще раз')
numb = []  # Создание списка чисел
for j in range(N):  # Заполнение списка чисел от 1 до n
    numb .append(j+1)
for i in range(N):
    input('Нажмите Enter чтобы вытащить следующий бочонок')
    new_random =randint(0, len(numb ) - 1)
    print(f'Бочонок под номером {i+1}: ', numb [new_random])
    logging.info(numb [new_random])
    numb .pop(new_random)

print('Бочонки закончились')

