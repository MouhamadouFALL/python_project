import csv 
import codecs


with codecs.open("departement.csv", "r", "utf8", "replace") as dept:
    rd = csv.reader(dept)
    departements = []
    [departements.append(line[2]) for line in rd]

departements.extend(["bouki", "Leukk"])
#print(departements)

departements += "senegal"

# unpacking
*l, m = departements # le dernier dans m et les reste dans l

# copylist = departements[:] # creer un copie de la liste originale
# la fonction id() retourne l'adresse en mémoire de l'objet

n = departements[-len("senegal"):]
print(''.join(n))
        