# =============================
#        Базовые типы
# =============================

integer = 2
float_number = -10.45

string1 = "цитата: 'что-то'. Следующая строка. \"ФИРМА\""
string2 = 'цитата: \'что-то\'. Следующая строка. "ФИРМА"'

boolean_true = True
boolean_false = False

result = None

# =============================
#      Комплексные типы
# =============================

complex_number1 = 1 + 2.2j
complex_number2 = complex(1 + 2.2j)

# list
empty_list = []
array = ["12'\"3", 1, [2.4, 4, 4, 4], 123, 3]
words = ["one", "two", "three", 120]

# tuple
tuple1 = (1, 2, 3, "one", "two", "three")
tuple2 = 0, 3
tuple3 = 0,
tuple4 = (0,)

# set - Множество.
empty_set = set()
set1 = {1, 2, 2, 2, "2, 2, 3", 4, 5, 6, 7, 8, (9, 10)}

# frozenset - Неизменяемое множество.
empty_frozenset = frozenset()
set2 = frozenset({"one", "two", "three"})

# dict - Словарь
empty_dict = {}
dict1 = {
    "name": "Вася",
    "age": 12,
    "city": "Москва",
    "job": "Работник",
    "coordinate": [55.0, 55.0],
    "address": {
        "city": "Москва",
        "street": "Ленина",
        "house": 12,
    }
}

languages = {
    "en": {},
    "ru": {},
}

# =============================
#      Неизменяемые типы
# =============================

string = "Hello World!"
number = 1234567890
float_n = 123.456
boolean_true_ = True
boolean_false_ = False
none_type_ = None

# Кортеж
tuple_ = (1, 3, 4)

# frozenset - Неизменяемое множество.
frozenset_ = frozenset({"one", "two", "three"})

# =============================
#      Изменяемые типы
# =============================

list1 = [1, 2, 3]
dictionary = {
    "name": "Вася",
    "age": 12,
}
set_ = {"a", "b", "c"}
