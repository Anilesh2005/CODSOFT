def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def pow(a,b):
    return a ^ b
def mod(a,b):
    return a % b
print("select operation what you want to perform")
print("1.add, 2.sub, 3.mul, 4.div, 5.pow, 6.mod")
while True:
    option=input("enter your choice :")
    if option in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("enter first number :"))
            num2 = float(input("enter second number :"))
        except ValueError:
            print("wrong input, enter valid input number :")
            continue
        if option == '1':
            print(num1, "+", num2, "==", add(num1,num2))
        elif option == '2':
            print(num1, "-", num2, "==", sub(num1,num2))
        elif option == '3':
            print(num1, "*", num2, "==", mul(num1,num2))
        elif option == '4':
            print(num1, "/", num2, "==", div(num1,num2))
        elif option == '5':
            print(num1, "^", num2, "==", pow(num1,num2))                  
        elif option == '6':
            print(num1, "%", num2, "==", mod(num1,num2))        
        cal_cu = print("again calculate if you want :")
        if cal_cu == "no":  
            break
    else:
        print("invalid input value")
            