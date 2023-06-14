
# on génère un nombre magique puis on demande à l'utilisateur de deviner ce en donner une réponse.

# générer un entier
# demander à l'utilisateur de deviner ce nombre
# vérifier la réponse de l'utilisateur

# Impporter le module random spécialiser dans la génération de nombre aléatoire
import random


magic_number = random.randint(1, 50)
res = None
historique = []

while res != magic_number:
    res = int(input("Devinez le nombre proposé par de système entre 1 et 50: "))
    historique.append(res)

    if res > magic_number:
        print("Ce nom est plus grand.")
    elif res < magic_number:
        print("Ce nombre est plus petit.")

print("Bravo!!!")
taille = len(historique)
# print("Vous avez" + str(taille) + "cooups.")
print("Vous avez", taille, "cooups.")
print("Votre historique de répondes: ")
for coup in historique:
    print('* ', coup)
