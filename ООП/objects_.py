class CatBlackSchema:
    color = 'black'  # Атрибут класса
    age = 1  # Атрибут класса
    name = 'Tom'  # Атрибут класса
    size = 'small'  # Атрибут класса
    tail = 1  # Атрибут класса


class CatOrangeSchema:
    color = 'orange'  # Атрибут класса
    age = 1  # Атрибут класса
    name = 'Tom'  # Атрибут класса
    size = 'small'  # Атрибут класса
    tail = 1  # Атрибут класса


CatBlackSchema.age += 12  # Обычно так не делают

cat_white_1 = CatBlackSchema()  # Создание экземпляра класса
cat_white_1.color = 'white'

cat_black_1 = CatBlackSchema()  # Создание экземпляра класса
cat_black_2 = CatBlackSchema()  # Создание экземпляра класса


print("Кошка 1:", cat_black_1.color, "age:", cat_black_1.age, cat_black_1.name, cat_black_1.size, cat_black_1.tail)
print("Кошка 2:", cat_black_2.color, "age:", cat_black_2.age, cat_black_2.name, cat_black_2.size, cat_black_2.tail)

cat_black_1.age += 1


print("Кошка 1:", cat_black_1.color, "age:", cat_black_1.age, cat_black_1.name, cat_black_1.size, cat_black_1.tail)
print("Кошка 2:", cat_black_2.color, "age:", cat_black_2.age, cat_black_2.name, cat_black_2.size, cat_black_2.tail)
