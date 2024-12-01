grades = {
    "математика": 5,
    "физика": 4,
    "информатика": 5,
    "химия": 3
}
average = sum(grades.values()) / len(grades)
print(f"Средний балл: {average}")
best_subject = max(grades.items(), key=lambda item: item[1])[0]
print(f"Лучшая оценка по предмету: {best_subject}")