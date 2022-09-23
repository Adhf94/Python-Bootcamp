import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_names_dic = {row.letter: row.code for (index, row) in data.iterrows()}
# is_on = True
# while is_on:
#     try:
#         input_name_list = [letter for letter in input("Enter your name: ").upper()]
#         output_list = [code_names_dic[letter] for letter in input_name_list]
#         print(output_list)
#     except KeyError:
#         print("Sorry, only letter in the alphabet, please.")
#     else:
#         is_on = False

#REAL LIFE IMPLEMENTATION SEGUN LA PROFESORA:

def generate_phonetic():
    word = input("Enter your name: ").upper()
    try:
        output_list = [code_names_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet, please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()