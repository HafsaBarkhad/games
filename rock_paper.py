# 2 player needed com against player
# choises are rock paper scissor player cooses any of the three while computer chooses randomly any of the 3

# result annouced aftr player quits


import random
computer_score =0
user_score = 0
choices=[ "rock","paper","scissors"]
limit=0
# print(computer_input)
# print(user_input)
while True:
    if limit < 3:
        print(f"{3-limit} limits remaining")
        user_input = input("choose either ROCK PAPER SCISSORS or q to quit the game").lower()
        computer_input = random.randint(0, 2)
        limit+=1
        # print(f"limit-=1 + limits remaining")





        if user_input == "q":
            break
        elif user_input not in choices:
            continue

        elif user_input==choices[computer_input] :
            continue
        elif user_input == "paper" and choices[computer_input] == "rock":
            user_score +=1
            continue
        elif user_input == "scissors" and choices[computer_input] == "paper":
            user_score +=1
            continue

        elif user_input == "rock" and choices[computer_input]== "scissors":
            user_score += 1
            continue
        else:
            computer_score +=1
            continue
    else:
        break

print(f"user score {user_score}")
print(f"computer score {computer_score}")






