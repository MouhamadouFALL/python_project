import csv
import codecs
import collections
import pdb


personnes = {
    "1": {
        "nom": "Dupont",
        "prénom": "Jean",
        "âge": 30,
        "profession": "Ingénieur",
        "ville": "Paris"
    },
    "2": {
        "nom": "Martin",
        "prénom": "Sophie",
        "âge": 25,
        "profession": "Designer",
        "ville": "Lyon"
    },
    "3": {
        "nom": "Durand",
        "prénom": "Pierre",
        "âge": 40,
        "profession": "Professeur",
        "ville": "Marseille"
    }
}

# get(): permet de recuperer la valeur de la clé passer en parametre
# si la clé n'existe pas, il retourne None
res = personnes.get("3")
print(res)

# get() permet de recuperer la valeur de la clé passer en parametre 
# si la clé n'existe pas, il retourne le valeur passer en parametre
res = personnes.get("4", "Personne inconnue")
print(res)

# on peut recuperer la valeur d'une clé en utilisant les crochets
res = personnes["3"]
print(res)

pdb.set_trace()


# un dictionnaire n'a pas d'ordre
with codecs.open("departement.csv", "r", "utf8", "replace") as dept:
    rd = csv.reader(dept)

    # concevoir un dictionnnaire de key val à partir d'une liste données

    # Solution 1
    # codes = [d[1] for d in rd]
    # dept.seek(0)
    # departements = [d[2] for d in rd]
    # jsondep = dict(zip(codes, departements))

    # une solution 2 améliorée
    # codes, departements = zip(*((d[1], d[2]) for d in rd))
    # codes_dept = dict(zip(codes, departements))

    # Solution 3 
    # codes_dept = dict(((d[1], d[2]) for d in rd))

    # Solution 4 avec les compréhension de liste
    codes_dept = {d[0]: d[2] for d in rd}
    print(codes_dept)

    # ordonner un dictionnaire dans le but de savoir le dernier élément ajouter
    collections.OrderedDict(codes_dept)
