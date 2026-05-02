print("Привет! Я бот-помощник для расчёта норм воды и "
      "калорий.")
print("Давай познакомимся поближе.\n")

user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе лет? "))

print(f"\n{user_name}, теперь мне нужно узнать твои "
      "параметры.")

user_weight = float(input("Введи вес "
"(кг, например 75.5): "))
user_height = float(input("Введи рост "
"(м, например 1.75): "))

bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

water_ml = user_weight * 30
water_l = water_ml / 1000

print("Результаты расчётов для", user_name,
      "(возраст:", user_age, "лет):")
print("Твой ИМТ:", bmi_rounded)
print("Твоя норма воды:",
      round(water_l, 1), "литров")