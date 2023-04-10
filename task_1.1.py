# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = ('Потеряй мгновение, оставаясь в живых', 'Своего рода сказка', 'Начни меня', 'Новое спасение')
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.





my_favorite_songs = (
'Потеряй мгновение оставаясь в живых' 
'Новое спасение' 
'Своего рода сказка' 
'Начни меня' )
    


print(my_favorite_songs[0:35])
print(my_favorite_songs[35:49])
print(my_favorite_songs[49:67])
print(my_favorite_songs[67:77])
    
# Да, можно так, но давайте "попросим" Python найти индексы за нас
# Решение с помощью индексации строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('N') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('S') : 
     my_favorite_songs.find(', A')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('St') : 
    my_favorite_songs.rfind(', N')
    ]

print(first_song, last_song, second_song, previous_song)


# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
