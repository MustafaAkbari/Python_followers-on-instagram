import random
from art import logo, vs
from game_data import data


score = 0
is_choice_finished = False
while not is_choice_finished:
    person_1 = random.choice(data)
    person_2 = random.choice(data)
    if person_1 == person_2:
        person_2 = random.choice(data)
    print(logo)
    print(f"Compare A: {person_1['name']}, {person_1['description']}, {person_1['country']}")
    print(vs)
    print(f"Compare B: {person_2['name']}, {person_2['description']}, {person_2['country']}")
    followers = input("Who has more followers in instagram?\nType 'A' for person_1 and"
                      "Type 'B' for person_2: ").lower()
    if followers == "A":
        if person_1["follower_count"] > person_2["follower_count"]:
            score += 1
            print(f"you're right! current score: {score}")
        else:
            print(f"You were wrong! final score: {score}")
            is_choice_finished = True
    else:
        if person_2["follower_count"] > person_1["follower_count"]:
            score += 1
            print(f"you're right! current score: {score}")
        else:
            print(f"You were wrong! final score: {score}")
            is_choice_finished = True





