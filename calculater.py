first = input("Enter The First Number=")
second = input("Enter The Second Number=")
first = int(first)
second = int(second)
operator = ("-------press key operation (+,-,*,/,%)------------")
operator =input("Enter operation=")
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print ("invalid operation")
