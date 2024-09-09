
"""
# import du module random, spécialisé dans la 
# génération de nombre aléatoire
import random

# on crée un nombre au hasard en 0 et 100
chiffre_secret = random.randint(0, 100)

# on initialise la variable reponse avec None
reponse = None
# on cree une liste pour stocker les historique
historique = []

# tant que la reponse est différente du chiffre_secret
# la boucle va continuer de tourner
while reponse != chiffre_secret:
	
	# on demande à l'utilisateur de deviner le chiffre secret
	# (on oublie de convertir la reponse en entier)
	reponse = int(input("Entrer un chiffre entre 0 et 100\n"))

	# on ajoute la reponse dans historique
	historique.append(reponse)

	# si l'essai de l'utilisateur est plus petit ou plus 
	# grand que la reponse à deviner, on lui donne un indice
	if reponse > chiffre_secret:
		print("Le chiffre secret est plus petit que ca")
	elif reponse < chiffre_secret:
		print('le chiffre secret est plus grand qu ca')

# sinon, le chiffre est deviner
print('Bravo !')

taille = len(historique)
print('Vous avez gagné en',taille,'coups.')

for coup in historique:
	print('-',coup)
"""
#################################################
# Exercice de Sondage
"""
#creation du dictionnaire de couleurs
couleurs = {}
# initialisation de la reponse par None
reponse = None

# tant que la repone est differente de chaine vide
while reponse != '':
	# demander aux utilisiturs leurs couleurs preferees
	reponse = input("Entrer votre couleur preférée !  ")
	# si la derniere reponse n'est pas vide
	if reponse:
		# si la couleur existe dans le dictionnnaire 
		if reponse in couleurs:
			# incremente le score existant de 1
			couleurs[reponse] += 1
		# si la reponse n'exite pas 
		else:
			# mettre un score de 1 
			couleurs[reponse] = 1

# afficher la liste des votes en iuterant 
# sur les paires cle:valeur du dictionnaire
print("vote pour les couleurs ")
for couleur, score in couleurs.items():
	print('-', couleur, ':', score)

"""
#################################################
# chercher un mot unique dans un texte 

ficher = open("C:\\Users\\x1carbon\\Desktop\\NABY\\Programmation\\Python\\chan.txt")
texte = ficher.read().strip().lower().split()
print(texte)
#for mot in texte: