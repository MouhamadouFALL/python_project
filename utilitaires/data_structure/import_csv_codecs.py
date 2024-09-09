
import csv
import codecs


with codecs.open('departement.csv', encoding="utf8", errors="replace") as dept:
    rd = csv.reader(dept)
    [print(line) for line in rd]
