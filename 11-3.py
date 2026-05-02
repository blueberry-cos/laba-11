import os
if not os.path.exists("покупки.csv"):
    with open("покупки.csv", "w", encoding="utf-8") as file:
        file.write("Продукт,Количество,Цена\n")
        file.write("Молоко,2,80\n")
        file.write("Сыр,1,500\n")
        file.write("Хлеб,2,70\n")
    print("Файл 'покупки.csv' создан!\n")
with open("покупки.csv", "r", encoding="utf-8") as file:
    строки = file.readlines()
всего = 0
print("Нужно купить:")
for i in range(1, len(строки)):
    строка = строки[i].strip()
    части = строка.split(",")
    продукт = части[0]
    количество = int(части[1])
    цена = int(части[2])
    стоимость = количество * цена
    всего = всего + стоимость
    print(f"{продукт} - {количество} шт. за {цена} руб.")
print(f"Итоговая сумма: {всего} руб.")