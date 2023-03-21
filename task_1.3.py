# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней
    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней
    # Введите номер месяца: 15
    # Такого месяца нет!
    
import datetime
    
number = input('Введите номер месяца:')
month = int(number)


if int(month) < 1 or int(month) > 12:
    print('Такого месяца нет')
pass
month_name = datetime.date(2023,month, 1).strftime("%B")
if int(month) == 2:
    days_in_month = 28
    print('Вы ввели:', month_name, ",", days_in_month, "days" )
elif int(month) == 4 or int(month) ==6 or int(month) ==9 or int(month) == 12:
    days_in_month = 30
    print('Вы ввели:', month_name, ",", days_in_month, "days" )
else:
   days_in_month = 31
   print('Вы ввели:', month_name, ",", days_in_month, "days" )