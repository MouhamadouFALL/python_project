
import sys
import pathlib
import sqlite3

import collections

try:
    rep_history = pathlib.Path(sys.argv[1]) # convertir un argument en chemin 
except IndexError:
    sys.exit("Vous devez passer en paraametre un chemin vers un fichier Historique.")

history = rep_history / "History"

if not history.is_file():
    sys.exit("Imposssible de trouver le fichier "+ str(history))

cnx = sqlite3.connect(str(history))
cr = cnx.cursor()

# query = "SELECT * FROM urls"

query = "SELECT url, visit_count from urls"

res = cr.execute(query)

if res:
    dict_hist = {}
    for line in res:
        x, score = line
        if len(x.split("."))>=2:
            a, b, *c = x.split(".")
            if b in dict_hist:
                dict_hist[b] += score
            else:
                dict_hist[b] = score
    #dict_hist = tuple(dict_hist)
    #cpt = collections.Counter(dict_hist)
    #print(cpt.most_common(10))


### Traiter un fichier historique des site visités pour un navigateur Firfox
# g = (line[0][-2::-1].replace('www.', '') for line in res)
# cpt = collections.Counter(g)
# print(cpt.most_common(10))