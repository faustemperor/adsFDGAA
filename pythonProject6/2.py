user_data = {}
for _ in range(3):
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    user_data[name] = age
print(user_data)