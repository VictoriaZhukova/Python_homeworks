def month_to_season(month):
    if 0 < month < 3 or month == 12:
        return "Зима"
    elif 2 < month < 6:
        return "Весна"
    elif 5 < month < 9:
        return "Лето"
    elif 8 < month < 12:
        return "Осень"
    return None


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
