import random

logo = """
             __      ___ __  __           
            / _`|  ||__ /__`/__`          
            \__>\__/|___.__/.__/          
___    ___                __  ___ __  
 ||__||__    |\ ||  ||\/||__)|__ |__) 
 ||  ||___   | \|\__/|  ||__)|___|  \ 
 
 
                                                 """


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

lives=0
d_hard = 5
d_easy = 10
def dificulty():
    while True:
        level_dificulty =input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level_dificulty != "easy" and level_dificulty != "hard":
            print("You must choose between 'easy' or 'hard'! ")
        else:
            break
    
    if level_dificulty  == "easy":
        return d_easy
    else:
        return d_hard
def game():
    the_number = random.randint(1,100)
   
    lives = dificulty()
    
    game_over = False
    while not game_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
            if  guess > 100 or guess < 0:
                print("The number must be between 1 and 100. ")
                continue
        except ValueError:
            print("Guess must be a NUMBER")
            continue
        if guess == the_number:
            print(f"You win! the answer was {the_number}")
            game_over = True
        else:    
            if guess > the_number:
                lives -=1
                print("Too high! \n Guess again") 
            elif guess < the_number:
                lives -=1
                print("Too low!\n Guess again ")
        if lives == 0:
            print(f"You've run out of guesses, you lose.")
            print(f"The answer was {the_number}")
            game_over = True
game()
