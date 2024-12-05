print("*" * 15, " Калькулятор ", "*" * 10)
print("Для выхода введите q в качестве знака операции")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == 'q': break
    if s in '+-*/':
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        if s == '+': print("%.2f" % (num1 + num2))
        if s == '-': print("%.2f" % (num1 - num2))
        if s == '*': print("%.2f" % (num1 * num2))
        if s == '/':
            if num2 != 0:
                print("%.2f" % (num1 / num2))
            else: print("Ошибка. На ноль делить нельзя.")
    else: print("Ошибка. Неверный знак операции.")

    quest = input("Начать новое вычисление? (Yes/No): ")
    if quest == 'No': break
