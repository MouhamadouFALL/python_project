import csv
import codecs


with codecs.open("departement.csv", encoding="utf8", errors="replace") as dept:
    rd = csv.reader(dept)

    departemets = []
    for line in rd:
        departemets.append(line[2])

print(departemets)

print("################### Ajout de plusieurs ########################")
### ajout des élements d'une liste à la fin d'une liste existante
departemets.extend(['Dakar', 'kaolack'])
### ajout des élements d'une liste dans une liste existante à une position donnée
departemets[2:2] = ['Dakar', 'kaolack']
print(departemets)

# departemets[:] # modifier le contenu d'une liste existante

print("################### Supprimer un élément dans une liste #######")
# departemets.pop() # supprime le dernier element de la liste puis retourne la valeur supprimée
# departemets.pop(departemets.index('Ardennes')) # ou bien remove()
# departemets.remove('Hautes-Alpes')
del(departemets[2])
print(departemets)




