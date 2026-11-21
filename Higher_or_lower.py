import random

data=[
    {
        "name":"Amrullah Hazrati",
        "age":13,
        "Country":"Afghanistan"
    },
    {
        "name":"Abdulbasit Hazrati",
        "age":19,
        "Country":"Pakistan"
    },
    {
        "name":"Rohullah Hazrati",
        "age":14,
        "Country":"Iran"
    },
    {
        "name":"Waris Hazrati",
        "age":18,
        "Country":"Canada"
    },
    {
        "name":"Nasrat Hazrati",
        "age":17,
        "Country":"Spain"
    },
    {
        "name":"Abdulmuswer Hazrati",
        "age":15,
        "Country":"Turkish"
    },
    {
        "name":"Hasibullah Hazrati",
        "age":14,
        "Country":"Tajikistan"
    },
    {
        "name":"Imran Hazrati",
        "age":21,
        "Country":"Kabul"
    }

]
Should_continue=True
score = 0

while Should_continue:

    A = random.choice(data)
    print(f"Name: {A['name']} Country: {A['Country']}")
    print("VS")
    B = random.choice(data)
    if A==B:
        B=random.choice(data)
        print(f"Name: {B['name']} Country: {B['Country']}")
    else:
        print(f"Name: {B['name']} Country: {B['Country']}")
    Choose=input("Who is older? Type A or B").upper()
    if A['age'] > B['age'] and Choose=="A":
        print("\n" * 20)
        score += 1
        print(f"Your score is {score}")
    elif A['age'] < B['age'] and Choose=="B":
        print("\n" * 20)
        score += 1
        print(f"Your score is {score}")


    else:
        print("\n"*20)
        print(f"Your score is {score}")
        print("Sorry, That's wrong, Please try again.")
        Should_continue=False


