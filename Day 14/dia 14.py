import random

from game_data import logo, vs, data

def followers_compare(compare_a, compare_b):

    followers_a = compare_a["follower_count"]
    followers_b = compare_b["follower_count"]
    if followers_a > followers_b:
        return "a"
    else:
        return "b"
    
def game():
    score = 0
    game_over = False
    print(logo)
    compare_a= random.choice(data)
    name_a = compare_a["name"]
    description_a = compare_a["description"]
    from_a= compare_a["country"]
    while not game_over:
        
        compare_b=random.choice(data)
        if compare_a == compare_b:
            compare_b = random.choice(data)
        name_b = compare_b["name"]
        description_b = compare_b["description"]
        from_b= compare_b["country"]
        print(f"Compare A: {name_a}, a {description_a}, from {from_a}. ")
        follower = compare_a["follower_count"]
        
        print(vs)
        
        print(f"Compare B: {name_b}, a {description_b}, from {from_b}. ")
        followerb = compare_b["follower_count"]
        
        right_answer = followers_compare(compare_a, compare_b)
        print(right_answer)
        guess= input("Who has more followers? Type 'A' or 'B':").lower()
        
        if guess != right_answer:
            game_over = True
            print(f"Game over.")
        else:
            score +=1
            
        
        print(f"Your Score is {score}")
game()
