import random
import os
from HIgher_lower_game_data import data, logo, vs


def format_data(account):
    """takes account data and return it"""

    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name} , a {account_description} , from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """takes guess and follower count and return if they're right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

    # display art


print(logo)
account_b = random.choice(data)
game_should_continue = True
score = 0
# repeatable game
while game_should_continue:
    # generate random account from data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"compare A {format_data(account_a)}")
    print(vs)
    print(f"compare B {format_data(account_b)}")

    # followers
    guess = input("Who has more followers 'A' or 'B' ? ").lower()
    # followers count
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system('cls')
    print(logo)

    if is_correct:
        print(f"You're right , current score is {score}")
        score += 1
    else:
        game_should_continue = False
        print(f" Sorry ! That's wrong. Final score : {score}")
