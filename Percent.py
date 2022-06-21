connect = True

while connect == True:
    number = input("Число: ")
    procent = input("Процент: ")
    while type(number) != int:
        try:
            number = int(number)
            procent = int(procent)

        except ValueError:
            print("Вводи целочисленные значения!")
            number = input("Число: ")
            procent = input("Процент: ")

    while type(procent) != int:
        try:
            procent = int(procent)
            procent = int(procent)

        except ValueError:
            print("Вводи целочисленные значения!")
            number = input("Число: ")
            procent = input("Процент: ")

    finish = number / 100 * procent

    print("Результат: ", float(finish))
