import csv 
import codecs


with codecs.open("departement.csv", "r", "utf8", "replace") as dept:
    rd = csv.reader(dept, delimiter=",")

    departements = []
    [departements.append(line[2]) for line in rd]

tuple_dep = tuple(departements)

print(tuple_dep)