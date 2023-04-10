# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например
#* = [4,6,2,1,9,63,-134,566]   - >  max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> мин = -110, макс = 56
# * [42, 54, 65, 87, 0] -> мин = 0, макс = 87
# * [5] -> мин = 5, макс = 5
# функции max и min использовать нельзя!







import datetime
# def default(data):
#   for data in arr:
#     data = sorted(data)
#     return data

# arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]
# def minimum(arr):
#         print ("МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ")
#         print ("Метод сортировки встроенный")
# start_time=datetime.now()
# for data in arr :
#     data = sorted(data)
#     print ["Минимальное значение из массива:", data, min(data)]

# def maximum(arr):
#         print ("МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ")
#         print ("Метод сортировки встроенный")
# start_time = datetime.now()
# for data in arr :
#         data=sorted(data)
#         print ["Максимальное значение из массива:", data, max(data)]
        
        
        
arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]

def minimum(arr):
    pass

def maximum(arr):
    pass

def bubble(num):
  n = len(num)
  for i in range (n-1):
    for j in range (n-i-1):
      if num[j] > num[j+1]:
        num[j], num[j+1] = num[j+1], num[j]
  return num


def minimum(arr):
  print ("MIN ЗНАЧЕНИЯ")
  for num in arr:
    print(num, bubble(num)[0])


def maximum(arr):
  print ("MAX ЗНАЧЕНИЯ")
  for num in arr:
    print (num, bubble(num)[len(num)-1])

print(minimum(arr))
print(maximum(arr))