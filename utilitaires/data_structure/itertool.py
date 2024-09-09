import csv
import codecs
import itertools


with codecs.open("departement.csv", "r", "utf8", "replace") as dept:
    rd = csv.reader(dept, delimiter=",")
    codes, departements = zip(*((d[1], d[2]) for d in rd))

    res = tuple(itertools.chain(codes, departements)) # regroupe les codes et les départements
    res1 = tuple(itertools.chain.from_iterable(departements)) # iter puis retourne une liste de caractere 
    res2 = tuple(itertools.accumulate(codes))
    # grouper par criteres
    gr_res = tuple(itertools.groupby(departements, key=len))
    # 
    masque = tuple(d[0] < 'i' for d in departements)
    #print(masque)
    compres_res = tuple(itertools.compress(departements, (d[0] < 'B' for d in departements)))
    print(compres_res)
    # print(gr_res)
    # print(res)
    # print(res1)
    # print(res2)