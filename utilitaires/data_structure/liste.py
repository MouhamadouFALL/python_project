import csv
import codecs


# Liste de noms de fruits
fruits = ["Pomme", "Banane", "Orange", "Fraise", "Mangue", "Ananas", "Raisin", "Pastèque", "Kiwi", "Poire"]
#La complétion de liste 
new_fruits = [len(fruit) if len(fruit) > 4 else 0 for fruit in fruits]

# Liste de noms de villes
cities = ["Dakar", "Kaolack", "Fatick", "Saint-Louis", "Tambacounda", "Thisse", "Ziguinchor"]

with codecs.open("departement.csv", encoding="utf8", errors="replace") as dept:
    rd = csv.reader(dept)

    for line in rd:
        print(line[1:3])


# Liste à deux dimensions

#   x 0  1  2  /   y
m = [[1, 2, 3], #  0
     [4, 5, 6], #  1
     [7, 8, 9]] #  2

for y in m:
    ligne = ""
    for x in y:
        ligne += str(x) + " "
    print(ligne)

