# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)


class MyMatrix:
    
    data = [] # (rows*cols) string cell
    cols = 0
    rows = 0
    
    def __init__(self, rows_count, cols_count): # Инициализируем объект матрицы. Все ячейки по умолчанию "none"
            dat = []
            for n in range(rows_count):
                row = ["None"]*cols_count
                dat.append(row)
            self.data = dat
            self.cols = cols_count
            self.rows = rows_count
    
    # ==== PRINT ====
    def printBlock(self): # Gecnfz 
        print("\n") 
     
    def printMatrix(self): # печать в консоль объекта матрицы.
        for n in range(self.rows):
            rw = ""
            for m in range(self.cols):
                rw += "\t["+str(self.data[n][m])+"]"
            print(rw)
        self.printBlock()
    
    def printMatrixWCoord(self):
        rw = " (x)"
        range_to_list = list(range(self.cols))
        for m in range(self.cols):
            rw += "\t("+str(range_to_list[m])+")"
        print(rw) 
         
        for n in range(self.rows):
            rw = " ("+ str(n) +")"
            for m in range(self.cols):
                rw += "\t["+str(self.data[n][m])+"]"
            print(rw)
        self.printBlock()
    
    def printAll(self):
        print("\n Matrix [" + str(self.rows) + "]*[" + str(self.cols) + "]")
        self.printMatrixWCoord()
    
    # ==== GETTERS ====
    
    def getCols(self): # Хм... что за странные функции?
        print(self.cols)
        
    def getRows(self): # Хм... что за странные функции?
        print(self.rows)
    
#       * принимать новые значения,  - ++МД: это что за зхверь? Инит() что ли?
#       * заменять существующие значения, 
    
    # ==== SETTERS ====
    
    def setCellByCoord(self, row, col, newValue): # интерфейс: отсчет строк и колонок начинается с 0
        self.data[row][col] = newValue
        
    def setCellByHumanCoord(self, row, col, newValue): # интерфейс: отсчет строк и колонок начинается с 1
        self.data[row-1][col-1] = newValue
        
    def setMatrixToZero(self):
        for n in range(self.rows):
            for m in range(self.cols):
                self.data[n][m] = 0
        
    
# Дымовое тестирование
x = MyMatrix(5,5)
x.printAll()
x.setMatrixToZero()
x.setCellByCoord(2,2, 1)
x.printMatrixWCoord()
x.setCellByHumanCoord(2,2, 2)
x.printMatrixWCoord()

