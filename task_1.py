Задача 1.2

import datetime
import random

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
my_favorite_songs = [
    ['Потеря минуты', 3.03],
    ['Новое спасение', 4.02],
    ['Оставаясь в живых', 3.40],
    ['Вне контакта', 3.03],
    ['Своего рода сказка', 5.28],
    ['Легко', 4.15],
    ['Прекрасный день', 4.04],
    ['Некуда бежать', 2.58],
    ['В этом мире', 4.02],
]



res =  random.sample(my_favorite_songs, 3)
list = round(res[0][1] + res[1][1]+ res[2][1])

print(datetime.time(list).strftime("%M:%S"))

print(res)
print("A,C: Три песни звучат", list, "минут")

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
my_favorite_songs_dict = {
    'Потеря минуты': 3.03, 'Новое спасение': 4.02, 'Остаться в живых': 3.40,
    'Вне контакта': 3.03, 'Своего рода сказка': 5.28, 'Легко': 4.15,
    'Прекрасный день': 4.04, 'Некуда бежать': 2.58, 'В этом мире': 4.02,
}

total = 0
for number in range(3):
    song, length = random.choice(list(my_favorite_songs_dict.items()))
    print(song + ':' + repr(length))
    total+=length
print(total)    



# Пункт C. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

# Сгенерируйте случайные песни с помощью модуля random
fst_ns = ['Ля','Зеленый','Слон','Неверный','Блямс','Тыщь','Мышь','Кукарача','Засада','Хомо','Сахар','Турляля','Бубубум']
snd_ns = ['Сцапиенс','Гыгы','Куры','Шлимазл','АВМЯК','Финка','Румынка','Бубу','Баба','Дед','Три','Шаббат','База']
rnd_fl = 1.1



total = 0
for number in range(3):
    length = random.uniform(rnd_fl, rnd_fl*9)
    fst = random.choice(fst_ns)
    snd = random.choice(snd_ns)
    print(fst + ' ' + snd  + ' - ' + '{:.2f}'.format(length))
    total+=length
print('{:.2f}'.format(total))    

# Да, можно так
# ###################### Решение ######################

# Импорты
from random import sample, choices
from datetime import timedelta
from math import modf

# Пункт А
time = my_favorite_songs[0][1] + my_favorite_songs[2][1] + my_favorite_songs[4][1]
print(f'Пункт А: Три песни звучат {time} минут.')

# Пункт С(А)
time = 0
for song in sample(my_favorite_songs, 3):
    time += song[1]

print(f'Пункт C(A): Три песни звучат {round(time, 2)}')

# Пункт D(А)
total_time = timedelta()
for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(A): Три песни звучат {total_time}')


# Пункт B
time = my_favorite_songs_dict['Waste a Moment'] + my_favorite_songs_dict['Staying\' Alive'] + my_favorite_songs_dict['Easy']
print(f'Пункт B: Три песни звучат {time} минут.')

# Пункт C(B)
time = 0
for song in sample(tuple(my_favorite_songs_dict), 3):
    time += my_favorite_songs_dict[song]

print(f'Пункт C(B): Три песни звучат {round(time, 2)}')

# Пункт D(А)
total_time = timedelta()
for song in sample(tuple(my_favorite_songs_dict), 3):
    s, m = modf(my_favorite_songs_dict[song])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(B): Три песни звучат {total_time}')
