import random

toss = input("Heads or Tails?")
        

list = ["heads", "tails"]
randomToss = random.choice(list)

if toss == randomToss:
    print("you won the toss")

else:
    print("you lose the toss")


# a = random.randint(1, 2)
# print(a)

# for i in range(0, 6):
#         a = random.randint(1, 6)
#         print(a)

