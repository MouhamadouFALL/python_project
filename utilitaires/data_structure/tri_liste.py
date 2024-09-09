import csv
import codecs


with codecs.open("departement.csv", encoding="utf8", errors="replace") as dept:
    rd = csv.reader(dept)

    departemets = []
    for line in rd:
        departemets.append(line[2])

print(departemets)

### Inverser une liste 
departemets.reverse()

### trier avec sorted puis afficher sans concervation du tri
print(sorted(departemets))
### transforme la liste existante en une liste triée
# departemets.sort() # trier sans cle de tri
departemets.sort(key=int) # avec clé de tri
departemets.sort(key=lambda x: x[-1]) # avec clé de tri
print(departemets)


