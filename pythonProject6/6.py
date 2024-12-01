employees = {}

while True:
    action = input("Введите действие (добавить, вывести, найти, изменить, удалить, выход): ").strip().lower()

    if action == "добавить":
        emp_id = input("Введите идентификатор сотрудника: ")
        name = input("Введите имя: ")
        position = input("Введите должность: ")
        salary = float(input("Введите зарплату: "))
        employees[emp_id] = {
            "имя": name,
            "должность": position,
            "зарплата": salary
        }

    elif action == "вывести":
        for emp_id, info in employees.items():
            print(f"ID: {emp_id}, Имя: {info['имя']}, Должность: {info['должность']}, Зарплата: {info['зарплата']}")

    elif action == "найти":
        emp_id = input("Введите идентификатор сотрудника для поиска: ")
        emp_info = employees.get(emp_id)
        if emp_info:
            print(f"Имя: {emp_info['имя']}, Должность: {emp_info['должность']}, Зарплата: {emp_info['зарплата']}")
        else:
            print("Сотрудник не найден.")

    elif action == "изменить":
        emp_id = input("Введите идентификатор сотрудника для изменения зарплаты: ")
        if emp_id in employees:
            new_salary = float(input("Введите новую зарплату: "))
            employees[emp_id]['зарплата'] = new_salary
            print("Зарплата обновлена.")
        else:
            print("Сотрудник не найден.")

    elif action == "удалить":
        emp_id = input("Введите идентификатор сотрудника для удаления: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Сотрудник удален.")
        else:
            print("Сотрудник не найден.")

    elif action == "выход":
        break

    else:
        print("Некорректное действие. Попробуйте еще раз.")