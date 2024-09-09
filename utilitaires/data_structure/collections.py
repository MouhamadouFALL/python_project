import csv
import codecs
import collections


with codecs.open("departement.csv", "r", "utf8", "replace") as dept:
    rd = csv.reader(dept, delimiter=",")
    ign, codes, departements, *_ = zip(*rd) # <==> codes, departements = zip(*((d[1], d[2]) for d in rd))
    print(codes)
    # zip(*iterable) : permet de recipérer les valeurs de chaque colonne dans une collection(iterable)
    # Counter de collections compte le nombre d'occurence de la collection(liste, tuple, set) puis retourne
    # le résultat sous forme dictionnaire
    # autrement le nombre de répétition d'un élément dans une liste
    res = dict(collections.Counter(dep[0] for dep in departements))
    print(res)

    # recuperer les deux premiers éléments du résultat
    res = dict(collections.Counter(dep[0] for dep in departements).most_common(2))
    print(res)
