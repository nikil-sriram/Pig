import random

numberofplayers = int(input("Enter the number of players:"))
players = [[] for i in range(numberofplayers)]
turnofplayer = 1
score = 0

print(players)

print(f"Player {turnofplayer}'s turn has just started")
print(f"Your total score is {score}")

while True:
        wouldyouliketoroll = input("Would you like to roll (y/n)")
        if wouldyouliketoroll == "y":
            randomnumber = random.randint(1,6)
            score = players[turnofplayer-1].append(randomnumber)
            print(f"You rolled a: {randomnumber}")
            sumofscores = sum(players[turnofplayer-1])
            print(f"Your score is: {sumofscores}")
            if randomnumber == 1:
                  break
        else:
              break