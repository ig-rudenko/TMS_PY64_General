# Задание 1
# Через цикл вывести в консоль все элементы списка.
# Используя цикл, вывести в консоль все элементы списка в обратном порядке.
# Используя цикл, вывести в консоль все элементы списка, а их буквы в обратном порядке.
list1 = ['apple', 'banana', 'cherry']

last_index = len(list1) - 1  # 11

i = last_index
while i >= 0:
    print(list1[i])
    i -= 1  # i = i - 1


for i in range(last_index, -1, -1):
    print(list1[i])


for element in list1[::-1]:  # list1[0:last_index:-1]
    print(element)


for element in reversed(list1):
    print(element)


list1.reverse()  # ИЗМЕНЕНИЕ СПИСКА!
for element in list1:
    print(element)


# Задание 2
# Используя цикл, вывести в консоль все ключи словаря.
# Используя цикл, вывести в консоль все ключи и значения словаря.
dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Используя цикл, вывести в консоль все ключи словаря.
for key in dict1:
    print(key)

for key in dict1.keys():
    print(key)

[print(key) for key in dict1]

# Используя цикл, вывести в консоль все ключи и значения словаря.
for key, value in dict1.items():
    print(key, value)

for key in dict1:
    print(key, dict1[key])

for key in dict1.keys():
    print(key, dict1[key])

# Задание 3
# На вход пользователь вводит целое число (использовать функцию input).
# Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно.
# Используя цикл, вывести в консоль все числа от введенного числа до 1 включительно.
# Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно, которые делятся на 3 без остатка.

user_number = int(input('Введите число: '))  # 10

i = 0
while i <= user_number:
    print(i)    # 10
    i += 1      # 11


for i in range(1, user_number + 1):
    print(i)

# Используя цикл, вывести в консоль все числа от введенного числа до 1 включительно.
for i in range(user_number, 0, -1):
    print(i)

for i in reversed(range(1, user_number + 1)):
    if user_number % 3 == 0:
        print(i)


# Задание 4
# На вход пользователь вводит предложение (использовать функцию input).
# Посчитайте количество слов в предложении и выведите результат в консоль.
# Используя цикл, выведите в консоль все слова предложения в обратном порядке.
# Используя цикл, создайте словарь, где ключами являются длина слов,
#           а значениями - список слов в предложении с такой длиной.

user_text = input('Введите предложение: ')

user_words = user_text.split()  # ['Привет', 'мир', 'как', 'дела']
print(len(user_words))

new_dict = {}
for word in user_words:
    length = len(word)  # 5

    words_list = new_dict.get(length)
    if words_list is None:
        new_dict[length] = [word]
    else:
        words_list.append(word)

new_dict = {}
for word in user_words:
    length = len(word)  # 5
    new_dict.setdefault(length, []).append(word)


# Задание 5
# На вход пользователь должен ввести username, email, имя и фамилию по очереди (использовать функцию input).
# Для каждого параметра: если введенные данные не соответствуют требованиям
# (например, username должен быть длиной от 3 до 20 символов),
# выведите сообщение об ошибке и попросите ввести данные заново.
# Создайте словарь с данными пользователя и выведите его в консоль.

# Задание 6*
# Напишите в коде случайное число от 1 до 100.
# Пользователь должен угадать это число.
# Используя цикл, попросите пользователя ввести число до тех пор, пока он не угадает.
# Если пользователь ввел не число, выведите сообщение "Вы ввели не число".
# Если пользователь ввел число, которое не попало в диапазон от 1 до 100, выведите сообщение "Число не входит в диапазон от 1 до 100".
# Если пользователь ввел число больше загаданного, выведите сообщение "Загаданное число меньше".
# Если пользователь ввел число меньше загаданного, выведите сообщение "Загаданное число больше".
# Если пользователь угадал число, выведите сообщение "Вы угадали!" и завершите программу.

# Задание 7*
# Имеется структура данных пользователя.

# Используя цикл, выведите все активности по логам пользователя в консоль со временем и описанием.
# Если пользователь активен, выведите сообщение "Пользователь активен", иначе выведите "Пользователь не активен".
# Если у пользователя есть аватар, то выведите его в консоль, если нет, то выведите "Нет аватара".


user1 = {
    "userId": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": {
        "firstName": "Jane",
        "lastName": "Doe",
        "birthDate": "1992-04-12",
        "gender": "female",
        "avatarUrl": "https://example.com/avatars/janedoe.jpg",
        "bio": "Digital marketer and blogger."
    },
    "accountStatus": {
        "isActive": True,
        "lastLogin": "2025-01-10T09:15:00Z",
        "createdAt": "2023-03-20T11:00:00Z"
    },
    "activityLogs": [
        {
            "timestamp": "2025-01-09T18:30:00Z",
            "activity": "Commented on a post"
        },
        {
            "timestamp": "2025-01-08T16:45:00Z",
            "activity": "Liked a post"
        }
    ]
}

# Задание 8*

# Имеется структура данных продукта.

# Сейчас кол-во товара на складе равно 0. Посчитайте кол-во исходя из вариантов товара на складе.
# Выведите через цикл все варианты товара на складе в виде строки в формате: "Название - цена (кол-во на складе)".
# Используя цикл, найдите вариант товара с максимальной ценой и выведите его название и цену в консоль.
# Выведите через цикл все отзывы о товаре в виде строки в формате: "Пользователь - Оценка - Комментарий".
# Посчитайте через цикл количество отзывов с оценкой 5 и выведите их количество в консоль.
# Через цикл выведите только названия файлов картинок (например, "main.jpg" и "side.jpg") товара в консоль.
# Используя цикл, найдите и выведите в консоль все отзывы пользователя с именем "techguy123".

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
        "quantity": 0
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
            "price": 198.99,
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
