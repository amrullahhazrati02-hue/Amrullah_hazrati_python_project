

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
a=int(input("enter first number:\n"))
adding=print("+")
subtraction=print("-")
multiplication=print("*")
division=print("/")
chooosing= input("choose your oprition:\n")
b=int(input("enter the another number:\n"))
if chooosing == "+":
    print(add(a,b))
    answer=add(a,b)
elif chooosing == "-":
    print(subtract(a,b))
    answer=subtract(a,b)
elif chooosing == "*":
    print(multiply(a,b))
    answer=multiply(a,b)
elif chooosing == "/":
    print(divide(a,b))
    answer=divide(a,b)
else:
    print("please come again")
should_continue=True
while should_continue:
    should_continue=input("Do you want to continue.?Y or N?").lower()
    if should_continue =="y":
        whit_which_values=input(f"Whit a={answer} or new values?type new values 'N' for a={answer}'A' ").lower()
        if whit_which_values=="a":
            a=answer
            print(f"a={a}")
            adding = print("+")
            subtraction = print("-")
            multiplication = print("*")
            division = print("/")
            chooosing = input("choose your oprition:")
            b = int(input("enter the another number"))

            if chooosing == "+":
                print(add(a, b))
                answer = add(a, b)
            elif chooosing == "-":
                print(subtract(a, b))
                answer = subtract(a, b)
            elif chooosing == "*":
                print(multiply(a, b))
                answer = multiply(a, b)
            elif chooosing == "/":
                print(divide(a, b))
                answer = divide(a, b)
            else:
                print("please come again")
        elif whit_which_values=="n":
            print("\n"*20)
            a = int(input("enter first number:\n"))
            adding = print("+")
            subtraction = print("-")
            multiplication = print("*")
            division = print("/")
            chooosing = input("choose your oprition:\n")
            b = int(input("enter the another number:\n"))
            if chooosing == "+":
                print(add(a, b))
                answer = add(a, b)
            elif chooosing == "-":
                print(subtract(a, b))
                answer = subtract(a, b)
            elif chooosing == "*":
                print(multiply(a, b))
                answer = multiply(a, b)
            elif chooosing == "/":
                print(divide(a, b))
                answer = divide(a, b)
            else:
                print("please come again")



    else:
        print("please come again")
        should_continue=False






