import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     

def deal_card():
    """ returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    
    if sum(cards)==21 and len(cards) ==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, dealer_score):
  if player_score > 21 and dealer_score > 21:
    return "You went over. You lose 😤"


  if player_score == dealer_score:
    return "Draw 🙃"
  elif dealer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif player_score == 0:
    return "Win with a Blackjack 😎"
  elif player_score > 21:
    return "You went over. You lose 😭"
  elif dealer_score > 21:
    return "Opponent went over. You win 😁"
  elif player_score > dealer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
   
def play_game():
   print(logo)
   player_cards=[]
   dealer_cards=[]
   is_game_over = False
   
   for item in range(2):
       player_cards.append(deal_card())
       dealer_cards.append(deal_card())

   while not is_game_over:
        player_score = calculate_scores(player_cards)
        dealer_score = calculate_scores(dealer_cards)
        print(f"   Your cards: {player_cards}, current score: {player_score}")
        print(f"   Computer's first card: {dealer_cards[0]}")
        
        if player_score == 0 or dealer_score == 0 or  player_score >= 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:  ").lower()
            if user_should_deal == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True
     
   while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_scores(dealer_cards)
  
  
   print(f"  Your final hand: {player_cards}, final score: {player_score}")
   print(f"  Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
   print(compare(player_score, dealer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()










    