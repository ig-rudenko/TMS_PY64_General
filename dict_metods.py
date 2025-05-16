fr = {
    "name": "France",
    "capital": "Paris",
    "population": 67364357,
    "area": 551695,
    "currency": "Euro",
    "languages": ["French"],
    "region": "Europe",
    "subregion": "Western Europe",
    "flag": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg"
}

ge_langs = ["German"]
ge = {
    "name": "Germany",
    "Capital": "Berlin",
    "population": 83240525,
    "area": 357022,
    "currency": "Euro",
    "languages": ge_langs,
    "region": "Europe",
    "subregion": "Western Europe",
    "flag": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg"
}

# Пытаемся получить значение ключа "capital", но если такого ключа нет, то вернется значение "-".
print(ge.get("capital", "-"))

ge.setdefault("area", 0)  # Если ключа нет, то добавляем его со значением 0 и возвращаем.
ge["area"] = ge["area"] / 1000

# Проще решение:
ge["area"] = ge.setdefault("area", 0) / 1000

print(ge["area"])

# Получаем список ключей
keys = list(ge.keys())

# Получаем список значений
values = list(ge.values())

# Получаем список кортежей (ключ, значение)
items = list(ge.items())

print("keys: ", keys)
print("values: ", values)
print("items: ", items)

t = [
    ('name', 'Germany'),
    ('Capital', 'Berlin'),
]

# Объединение словарей.
new_dict = {'name': "ERROR"}
ge.update(new_dict)

# Удаление элемента по ключу, с возвратом значения.
# cap = ge.pop("Capital")

# Удаление элемента по ключу.
del ge["languages"]

# ---- Пустой список
# empty_list = list()
print("languages: ", ge.get("languages", []))

print(ge_langs)

# Полная очистка словаря.
ge.clear()

user = {
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
    "preferences": {
        "language": "fr",
        "theme": "light",
        "notifications": {
            "email": False,
            "sms": True,
            "push": True
        },
        "privacy": {
            "showOnlineStatus": True,
            "profileVisibility": "public"
        }
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

print("User is active:", user["accountStatus"].get("is_active"))


# product["variants"][-1]["color"].lower() == "red"

product = {
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
            "color": "Red",
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
        "numberOfReviews": 120
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
