

# Sondage de couleurs
# Demander à l'utiisateur sa couleur préférée
# Faire le sondage des couleurs saisies

res = None
couleurs = {}
responses = []

while res != "stop":
    res = input("Enter your favorite color:  ")
    if  res != 'stop':
        if res in couleurs:
            couleurs[res] += 1
        else:
            couleurs[res] = 1
print("Sondage des couleurs")
for couleur, score in couleurs.items():
    print(couleur, ":", score)