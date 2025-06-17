w = "hello world"
new_str = w + " " + str(123) + " " + "is a string"
print(new_str)

# Форматирование строки через % (старый вариант)

new_str = "%s %d is a string" % (w, 123)

print(new_str)

# Форматирование строки через .format()

template = "{} {} is a string"
new_str = template.format(w, 123)
print(new_str)

template = "{1} {0} is a string {0} {1}"
new_str = template.format(w, 123)
print(new_str)

template = "{hello} {number} is a string"
new_str = template.format(hello=w, number=123)
print(new_str)


# Форматирование строки через f-строки (новый вариант)

new_str = f"{w} {123} is a string {"NO" if w else "YES"} {w.lower()} {w[2]} {len(w)} {w[::-1]}"
print(new_str)


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


print(f"{10 / 3:.4f}")


for review in product1["reviews"]:
    print(f"{review['username']:<20} | {review['rating']:^6} | {review['comment']}")


username_col_width = 14
rating_col_width = 6

print(f"{'Username':<{username_col_width}} | {'Rating':^{rating_col_width}} | Comment")
for review in product1["reviews"]:
    print(f"{review['username']:<{username_col_width}} | {review['rating']:^{rating_col_width}} | {review['comment']}")
