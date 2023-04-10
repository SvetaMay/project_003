# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'Один'
# switch_it_up(3) -> 'Три'
# switch_it_up(10000) -> Нет
# Использовать условный оператор if-elif-else нельзя!
number = {0:'ноль',  1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять'}
def switch_it_up(number):
    for i in number:
        if i == 0:
            print('ноль')
    for i in number:
        if i == 1:
            print('один')
            print('два') 
            print('три')
            print('четыре')
            print('пять')
            print('шесть')
            print('семь')
            print('восемь')
            print('девять')
             

print(switch_it_up(number))
