 # Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.

def remove_exclamation_marks(s):
    return s.replace("!", "")

# Пункт B.
# Удалите восклицательный знак из конца строки. 

def remove_last_em_var1(s):
    return s[:-1] if s.endswith('!') else s


# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак. Слова разделены одним пробелом.
# ++МД: Слово "!" считается за слово с одним "!"? Если нет, то нарушение условия. 
# ++МД: Если да - то хреново составлены тесты

def word_has_only_one(s):
    k = s.count('!')
    return True if (k==1) else False 


def remove_word_with_one_em(s): # maximum kolhoz
    k = s.split (" ")
    res = ""
    for n in range(len(k)):
       if (not word_has_only_one(k[n])): # спорно. 
        res += " " + k[n]
    return res
    

# smoke test
test_cases = ["Привет! Здравствуйте!", 
              "Привет!", 
              " ",  
              "О, нет!!!", 
              "Привет!!!", 
              "! Привет"]

d_test_cases = ["Привет!", 
                "Привет! Привет!", 
                "Привет Привет! Привет!", 
                "Привет! ! Привет Привет!", 
                "Привет! Привет!! Привет!", 
                "Привет! ! Привет! Привет!"]

print("Пункт А")

for n in range(len(test_cases)):
    print(remove_exclamation_marks(test_cases[n]))

print("Пункт Б")

for n in range(len(test_cases)):
    print(remove_last_em_var1(test_cases[n]))
    
print("Пункт В")

for n in range(len(d_test_cases)):
    print(remove_word_with_one_em(d_test_cases[n]))
