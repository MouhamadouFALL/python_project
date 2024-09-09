import csv
import codecs
import collections

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
