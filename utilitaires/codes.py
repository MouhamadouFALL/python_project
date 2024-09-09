
couleurs = []
reponse = None
while reponse != 'stop':
	reponse = input("Entrer votre couleur preferee ")
	couleurs.append(reponse)

couleurs.pop()
print(couleurs)


#################################################
""" Une facon de parcourir un iterable 
	avec la boucle while
"""
compteur = 0
mots = input("Entrer l'iterable :  ")
taille = len(mots)
while compteur < taille:
	print(mots[compteur])
	compteur += 1

""" Parcourir un Iterable avec la boucle for """
mots = input("Entrer l'iterable :  ")
for lettre in mots:
	print(lettre)

#################################################
# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1 # affectation multiple
while a < 10:
	print(a)
	a, b = b, a+b
	# les expressions sur le côté droit sont toutes évaluées en premier 
	# avant qu'aucune des affectations n'ait lieu .
	# Les expressions de droite sont évaluées de gauche à droite.
	
# une autre facon d'afficher
a, b = 0, 1
while a < 1000:
	print(a, end=',')
	a, b = b, a+b

#################################################
tab = []
moyenne = 0
res = 0

for i in range(0,11):
	res = float(input("Entrer un reel svp : "))
	tab.append(res)
	moyenne += tab[i]

# on calcule la moyenne
moyenne /= 10

# on cherche le maximun
maximun = tab[10]
for x in range(0, 11):
	if maximun < tab[x]:
		maximun = tab[x]

# on cherche le minimum
minimum = tab[0]
for i in range(1, 11):
	if minimum > tab[i]:
		minimum = tab[i]

print("Maximun =", maximun, "\nMinimun =", minimum, "\nMoyenne =", moyenne)

#################################################
""" cette fonction informe si un nombre entier 
	strictement positif fourni est pair ou impair
"""
nombre = int(input("Entrer un entier strictement positif : "))
if nombre > 0:
	if nombre % 2 == 0:
		print(nombre, "est pair")
	else:
		print(nombre, "est impair")
#################################################
""" Cette fonction affiche la sommme des entiers de 
	0 jusqu'à un nombre strictement positif fourni
"""
nombre = 0
nombre_tentative = 0
while (nombre <= 0 and nombre_tentative < 3):
	nombre = int(input("Entrer un entier strictement positif : "))
	nombre_tentative += 1

# Addition de 0 jusqu'à nombre
sommme = 0
if nombre > 0:
	for x in range(1, nombre + 1):
		sommme += 1
	print('La somme des nombres de 0 à', nombre, 'donne :', somme)
else:
	print("Nombre d'essais epuise-Tratement interrompu")

###########################################################