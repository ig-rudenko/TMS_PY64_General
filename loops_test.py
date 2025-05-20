product1 = {
    "productId": 1001,
    "productName": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
    "brand": "SoundPro",
    "category": "Electronics",
    "price": 199.99,
    "currency": "USD",
    "stock": {
        "available": True,
        "quantity": 50
    },
    "images": [
        "https://example.com/products/1001/main.jpg",
        "https://example.com/products/1001/side.jpg"
    ],
    "variants": [
        {
            "variantId": "1001_01",
            "color": "Black",
            "price": 199.99,
            "stockQuantity": 20
        },
        {
            "variantId": "1001_02",
            "color": "White",
            "price": 199.99,
            "stockQuantity": 30
        }
    ],
    "dimensions": {
        "weight": "0.5kg",
        "width": "18cm",
        "height": "20cm",
        "depth": "8cm"
    },
    "ratings": {
        "averageRating": 4.7,
        "numberOfReviews": 2
    },
    "reviews": [
        {
            "reviewId": 501,
            "userId": 101,
            "username": "techguy123",
            "rating": 5,
            "comment": "Amazing sound quality and battery life!"
        },
        {
            "reviewId": 502,
            "userId": 102,
            "username": "jane_doe",
            "rating": 4,
            "comment": "Great headphones but a bit pricey."
        }
    ]
}

new_review = {
    "reviewId": 502,
    "userId": 102,
    "username": "jane_doe",
    "rating": 2,
    "comment": "Great headphones but a bit pricey."
}

product1["reviews"].append(new_review)

# В цикле мы проходим по всем элементам списка и вычисляем сумму всех рейтингов.

# Не делаем этого так, потому что нам не нужно проверять каждый случай.
# if len(product1["reviews"]) == 1:
#     average_rating = product1["reviews"][0]["rating"]
# elif len(product1["reviews"]) == 2:
#     average_rating = product1["reviews"][0]["rating"] + product1["reviews"][1]["rating"]
# elif len(product1["reviews"]) == 3:
#     average_rating = product1["reviews"][0]["rating"] + product1["reviews"][1]["rating"] + product1["reviews"][2]["rating"]
summ_rating = 0

reviews_length = len(product1["reviews"])  # 23
current_index = 0
stop_index = reviews_length - 1

while current_index <= stop_index:
    summ_rating += product1["reviews"][current_index]["rating"]
    print("Индекс ревью:", current_index, "Сумма рейтингов:", summ_rating, "Длина списка:", reviews_length)
    current_index += 1

print("Средний рейтинг:", summ_rating / reviews_length)



# Цикл FOR

summ_rating = 0
for review in product1["reviews"]:
    summ_rating += review["rating"]

print("Средний рейтинг:", summ_rating / len(product1["reviews"]))



list1 = ["el_1", 2, "el_3", 3]

for item in list1:
    print("Элемент списка:", item, "Тип:", type(item))

# Аналог на цикле WHILE
# -----------------------
current_index = 0
while current_index < len(list1):
    some_var = list1[current_index]
    # ===========
    # Наш код
    # ...
    print("Элемент списка:", some_var, "Тип:", type(some_var))
    # ===========
    current_index += 1
# -----------------------


text = """Логический тип данных в Python представлен типом bool. 
Объекты этого типа могут принимать одно из двух значений: True (истина) или False (ложь).  3
Логические операторы в Python, которые сводят результат к логическому значению True или False, включают:
and — оператор «и»: выражение "истинно", если оба его компонента истинны.  5
or — оператор «или»: выражение 'истинно', если хотя бы один из его компонентов истинен.  5
not — оператор «не»: изменяет логическое значение компонента на противоположное.  5"""

text_parts = text.split("\n")  # Символ переноса строки - `\n`

print(text_parts)

# text_parts = [
#     'Логический тип данных в Python представлен типом bool. ',
#     'Объекты этого типа могут принимать одно из двух значений: True (истина) или False (ложь).  3',
#     'Логические операторы в Python, которые сводят результат к логическому значению True или False, включают:',
#     'and — оператор «и»: выражение "истинно", если оба его компонента истинны.  5',
#     "or — оператор «или»: выражение 'истинно', если хотя бы один из его компонентов истинен.  5",
#     'not — оператор «не»: изменяет логическое значение компонента на противоположное.  5',
# ]

for line in text_parts:
    print("Количество слов в строке:", len(line.split()), "Содержимое строки:", line)
