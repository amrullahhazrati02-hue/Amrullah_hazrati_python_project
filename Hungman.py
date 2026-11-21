import random
word_list=["lyla","cow","right"]

lives=6

chosen_word=random.choice(word_list)
print(chosen_word)
game_over=False
placeholder=""
word_length=len(chosen_word)
for position in range(0,word_length):
    placeholder+="_"
correct_letters=[]
print(placeholder)
while not game_over:
    guess=input("Enter your guess: ").lower()



    display=""
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess not in chosen_word:
        lives-=1
        print(f"You have {lives } lives")
        print(f"You have {6-lives} lives left.")
        if lives==0:
            game_over=True
            print("You Lose!")
    if "_" not in display:
        game_over=True
        print("You won!")
