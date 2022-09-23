import random
word_list = ["aardvark", "baboon", "camel"]
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]
chosen_word = random.choice(word_list)
blank_spaces = []
wlen=len(chosen_word)
lives= 1
for l in chosen_word:
    blank_spaces += "_"

answer=False
if lives >= 0:
    if lives > 0:
        while True:
            guess = input("Guess a letter: ").lower()
            if guess not in abecedario or len(guess) > 1:
                    print("You must enter one letter. ")
            else:
                break
                

        for position in range(wlen):
            letter = chosen_word[position]
            if letter == guess:
                    blank_spaces[position] = letter
            else:
                print(f"{blank_spaces}\n Lives left: {lives}")
else:
    print("GAMEOVER")
        

        
        
        