import csv

new_data = []

# Открываем файл на чтение
with open("users.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f, delimiter=",")

    for i, line in enumerate(data):
        if i == 0:
            new_data.append(line)
            continue

        print(line, type(line))

        new_data.append(
            [line[0], line[1], int(line[2]) + 10, line[3], line[4]]
        )

# Создаём файл (на запись)
with open("users2.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(new_data)

print("Finished")


new_user_dict_list = []

# Открываем файл на чтение
with open("users2.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")

    for row in reader:
        print(row["name"], row["age"])
        new_user_dict_list.append(
            {
                "name": row["name"],
                "age": int(row["age"]) + 10,
            }
        )


# Создаём файл (на запись)
with open("users3.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(f, delimiter=",", fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_user_dict_list)

print("Finished")
