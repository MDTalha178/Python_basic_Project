from art import logo

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

symbols = {
    "+":"add",
    "-":"subtract",
    "*":"multiply",
    "/":"divide"
}




def calculation():
    print(logo)
    num1 = float(input("Enter your first number: "))
    for symbol in symbols:
        print(symbol)
    should_countinue = False
    while should_countinue !=True:
        choice = input("Pick up an operation")
        num2 = float(input("Enter your second number: "))
        if choice == "+":
            answer = add(num1, num2)
        elif choice == "-":
            answer = subtract(num1, num2)
        elif choice =="*":
            answer = multiply(num1, num2)
        else:
            answer = divide(num1, num2)
        print(f"{num1} {choice} {num2} = {answer}")

        if input(f"Type y to countinue calulating  with {answer} and type n to start with new calculation")=="y":
            answer = num1 
        else:
            should_countinue = True
            calculation()
calculation()