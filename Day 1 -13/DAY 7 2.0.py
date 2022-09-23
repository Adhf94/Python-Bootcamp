import random
from hangman_art import stages, logo
from hangman_words import word_list
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]
lives=6
chosen_word = random.choice(word_list)
blank_spaces = []
wlen=len(chosen_word)
print(logo)
print(chosen_word)

for l in chosen_word:
    blank_spaces += "_"
    
end_of_game = False

while not end_of_game:
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

    if guess in blank_spaces:
        print(f"You've already guessed {guess}")
      
    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -=1
      if lives == 0:  
        end_of_game = True
        print("\nGAME OVER")
        
    print(f"{''.join(blank_spaces)}\n lives left : {lives} ")
  
    if "_" not in blank_spaces:
      end_of_game = True
      print("You win.")

    print(stages[lives])