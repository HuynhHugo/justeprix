print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100")

from random import randint

price = randint(1,100)

tries = 0

while tries < 5: 
    answer = int(input(""))
    if answer < price:
        print ("C'est plus")
        tries += 1
    if answer > price:
        print ("C'est moins")
        tries += 1
    if answer == price:
        print ("C'est ça")
        tries += 1
        break
    if tries == 5:
        print ("C’est perdu")
        break