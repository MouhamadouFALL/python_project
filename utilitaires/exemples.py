


# Forcer à nommer le 2ème arguments (bullet) en utilisant * devant bullet
def listing(iterable, *,bullet='- '):
    """ Retourne une chaine à afficher.
    """
    
    items = []
    for elt in iterable:
        items.append("%s %s" % (bullet, elt))
        
    return "\n".join(items)


### Unpacking 
a, b, c = 2, 4, 6 # <==> a, b, c = (2, 4, 6)
a, b, c = [2, 4, 6]
a, b, c = set([2, 4, 6])
print(a, b, c)
# le dernier element dans c, l'avant dernier dans b et le reste dans a
*a, b, c = range(60)
# le premier element dans a, le dernier dans c et le reste dans b
a, *b, c = range(60)
# le premier element dans a, le deuxieme dans b et le reste dans c
a, b, *c = range(60)

### Unpacking avec les fonctions
def ajouter(a=0, b=0):
    return a + b

ajouter(5, 4)

# calcule la somme de tous les arguments qu’elle reçoit
vals = (2, 3)
ajouter(*vals) # unpacking tuple ou liste

dict_vals = {'a': 2, 'b': 4}
ajouter(**dict_vals) # unpacking dictionnaire

### Les listes en intension python
    # permettent de parcourir une liste et de creer une nouvelle liste
    
def somme(*args):
    total = 0
    for x in args:
        total += x
    return total

somme(1) # renvoie 1
somme(1, 2) # renvoie 3
somme(1, 2, 3) # renvoie 6



nombres = range(20)
nombres_square = [x * 2 for x in nombres ]

nombres = range(20)
nombres_square = [x** 2 for x in nombres if x % 2 == 0]

# créer une nouvelle liste en ajoutant un élément au début et à la fin d’une autre liste,
a = [2, 3, 4]
b = [1, *a, 5]
print(b) # ==> [1, 2, 3, 4, 5].


## x, **y, z = {"a":1, "b":2, "c":3}

a = {"x":1, "y":2}
b = {"y":3, "z":4}
c = {**a, **b} # c = {“x”:1, “y”:3, “z”:4}.

def afficher(**kwargs):
    print(f"Nom : {kwargs['nom']}")
    print(f"Age : {kwargs['age']}")

afficher(**{"nom":"Alice", "age":25})




# Avec les Sets
nombres = range(20)
nombres_square = {x** 2 for x in nombres if x % 2 == 0}



# Avec les dictionnaires
nombres = range(20)
nombres_square = {str(x): x** 2 for x in nombres if x % 2 == 0} 

### Generateurs
# les generateurs permettent d'economiser de memoire
generateur = (x** 2 for x in range(100) if x % 2 == 0)
# on peut appliquer la boucle for sur un generateur
# on peut transformer un generateur en tuple ou liste
# on ne peut pas utiliser ungenerateur deux fois de suite
# on ne peut pas indexer un generateur
# on ne peut pas determiner la taille dun generateur

# Creer un generateur avec une fonction
def carre(start, end):
    for x in range(start, end):
        yield x * x


# Définir la fonction générateur
def lire_fichier(nom_fichier):
    # Ouvrir le fichier en mode lecture
    with open(nom_fichier, "r") as fichier:
        # Parcourir chaque ligne du fichier
        for ligne in fichier:
            # Renvoyer la ligne courante
            yield ligne

# Appeler la fonction et stocker le résultat dans une variable
generateur = lire_fichier("mon_fichier.txt")

# Utiliser une boucle for pour afficher les lignes du fichier
for ligne in generateur:
    print(ligne)


# Biblio sys permet de manipuler des repertoires



