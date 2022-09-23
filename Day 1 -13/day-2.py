#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill= float(input("What was the total bill? "))
print(f"${bill}")
while True:
    tip= int(input("How much tip would you like to give? 10, 12, or 15? "))
    if tip != 10 and tip != 12 and tip != 15:
      print("Tip must be equal to 10,12 or 15 ")
    else:
      break
persons = int(input("How many people to split the bill? "))
def tip_spliter(tip):

  tip_percentage = int(tip) / 100
  total_tip = bill * tip_percentage
  tip_plus_bill = bill + total_tip
  billxperson = tip_plus_bill / persons
  final_amount = round(billxperson, 2)
  return final_amount
total_amount = tip_spliter(tip)
print(f'Each person should pay: ${total_amount}')