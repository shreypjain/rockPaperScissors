from random import randint

possibilities = ['rock','paper','scissors']

computer = possibilities[randint(0,2)]

user = input("what would you like to play, dont worry i have already chosen my answer, I cant cheat ;). Please either put rock, scissor, or paper, otherwise you automatically lose haha: ")

if user == "rock" and computer == "scissors":
    print("you won, I chose: " + computer)
elif user == "paper" and computer == "rock":
    print("you won, I chose: " + computer)
elif user == "scissors" and computer == "paper":
    print("you won, I chose: " + computer)
elif computer == "rock" and user == "scissors":
    print("I won, I chose: " + computer)
elif computer == "paper" and user == "rock":
    print("I won, I chose: " + computer)
elif computer == "scissors" and user == "paper":
    print("I won, I chose: " + computer)
elif not user in possibilities:
    print("cant even play the game by using the right words. I won!")

