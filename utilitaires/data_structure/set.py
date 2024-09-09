import csv
import codecs


with codecs.open("departement.csv", encoding="utf8", errors="replace") as dept:
    rd = csv.reader(dept)
    print(list(rd))
    departemets = set(line[2] for line in rd)
    print(departemets)

print("############ Ajouter dans Set ############")
# Ajouter dans un set
departemets.add("DAKAR")
departemets.update(['Thies', 'Mbour']) # ajout d'une liste
print(departemets)

### Supprimer un elemet dans un set
if "Mbour" in departemets: departemets.remove("Mbour") # remove retourne un élément s'il n'existe pas 
departemets.discard("Thies") # supprime un élément sans retourner un message d'erreur
print("############ Supprimer dans Set ############")
print(departemets)

# Créer un set 
print("############ créer un set ############")
fruits = {"Fraise", "Mangue", "Coco", "Banana"} # crée un set mutable
print(fruits)
animaux = set(["Lion", "Tigre", "Chat", "Chien", "Rat"]) # crée un set mutable
print(animaux)

tech = frozenset(["ecran", "UC", "Souris"])
print(tech)

