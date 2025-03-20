import random
#NUMBER OPTIONS
#print(help(random))
#number = random.randint(1,6)
#number = random.random()
#print(number)

#STRING OPTIONS
options = ("rock", "paper", "scissors")
print(random.choice(options))

#SHUFFLING
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)