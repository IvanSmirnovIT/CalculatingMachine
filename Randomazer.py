import random

print("Рандомайзер")

connect = True

while connect == True:
    a = input("От: ")
    b = input("До: ")
    if b < a:
        print("Нельзя вводить в первую строку значение меньше чем в первой! Перезапустите программу")

    finish = random.randint(int(a),int(b))

    print("Ответ: ", int(finish))
    print()

input()
