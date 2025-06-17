user_input = input("Введите любое число: ")

number = None

try:
    number = float(user_input)
except (ValueError, TypeError) as error:
    print("Ошибка!", error)

except Exception:  # Перехватывает большое кол-во ошибок! Так лучше не писать, но иногда полезно.
    print("Неизвестная ошибка!")

except:  # Перехватывает все ошибки! Так лучше не писать, но иногда полезно.
    print("Неизвестная ошибка!")

else:
    # Если ошибки не было, то выполняется этот блок кода.
    print("Все ок!")
    print(number)

finally:
    # ВСЕГДА выполняется этот блок кода!
    print("Конец программы!")


# if user_input.count(".") > 1:
#     print("Ошибка!")
# if user_input.count("-") > 1:
#     print("Ошибка!")
# if user_input.count("-") == 1 and user_input[0] != "-":
#     print("Ошибка!")
#
# if user_input.replace(".", "")[1:].isdigit():
#     print("Все ок!")
# else:
#     print("Ошибка!")
