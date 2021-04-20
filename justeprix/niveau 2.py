from random import randint
import time

print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100:")
print("Vous aurez 60 seconde pour écrire vos réponse, mais si le temps est écoulé votre dernière réponse ne sera donc pas pris en compte.\nBonne chance!")

nombre_hasard = randint(1,100)

nombre_proposition = 0

temps = time.time()

tentatives = 5

while nombre_proposition != nombre_hasard and tentatives > 0:

    print("\n")
    print("Entrer votre proposition:")

    proposition = input()

    if proposition.isdigit():

        proposition = int(nombre_proposition)

        temps_passee = int(time.time() - temps)
        
        if temps_passee >= 60:
            print("Votre dernière réponse ne sera donc pas pris en compte car le temps est écoulé.")
            break

        if nombre_proposition < nombre_hasard:
            print("C'est plus")
        elif nombre_proposition > nombre_hasard:
            print ("C'est moins")
        else:
            print("C'est gagné")

        tentatives -= 1 
        if tentatives == 0:
            print("C'est perdu!")

    else:
        print("Tu dois entrer un nombre")