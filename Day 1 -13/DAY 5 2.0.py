#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How long would you like your password to be ?\n")) 
nr_symbols = int(random.randint(0,nr_letters)-1)
nr_numbers = int(random.randint(0,nr_letters)-11)

passw=[]
for i in range(nr_letters):
    passw += random.choice(letters)
for i in range(nr_symbols):
    passw += random.choice(symbols)
for i in range(nr_numbers):
    passw += random.choice(numbers)

random.shuffle(passw)
password=""
for i in passw:
    password += i
print(f"Your PASSWORD is : {password}")
    