#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./input/Letters/starting_letter.txt", mode="r") as data:
    starting_letter = data.read()


with open("./input/Names/invited_names.txt", mode="r") as names:
    invited_names = names.readlines()

for names in invited_names:
    xname= names.strip()
    x = starting_letter.replace("[name]", xname)
    with open(f"Output/ReadyToSend/Letter_for_{xname}.txt", mode="w") as completed_letter:
        completed_letter.write(x)