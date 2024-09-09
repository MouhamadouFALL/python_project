import csv
import codecs


with codecs.open("departement.csv", "r", "utf8", "replace") as dept:
    rd = csv.reader(dept)
    departements = []
    [departements.append(d[2]) for d in rd]

    ### permet une approche fonctionnelle du traitement des lites
    ### Fonction map() effectue un traitement pour élément de la liste sans modifier la liste d'origine
    m = list(map(lambda d: d.upper(), departements))
    print(m)

    # Fonction Filter 
    f = list(filter(lambda d: d[0] in ['A', 'C',], departements))
    print(f)


    
