
### methode 1: pas recommander
# dept = open("departement.csv", mode="r")
# print(dept)

# dept.close()


### methode 2

import csv

with open('departement.csv', mode="r", encoding="utf8") as dept:
    #rd = csv.reader(dept, delimiter=";") # le cas ou le delimiteur est ;
    rd = csv.reader(dept) # un objet generateur qui retourne une liste pour chaque ligne
    for r in rd:
        print(r)





