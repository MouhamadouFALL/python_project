
# Sans utilisation de liste en Compréhension
# on recupere les nombres paires entre 0 - 19
liste_paire = []

for elt in range(20):
    if elt % 2 == 0:
        liste_paire.append(elt)

print(liste_paire)

# Utiliser les compréhension plutot que des map
# utilisation de comprehension list 
# on liste les nombres pairs entre 0-19 multiplier par 2
liste_c_paire = [x*2 for x in range(20) if x % 2 == 0] 
print(liste_c_paire)

# Dictionnaire et compréhension de liste
nb_paires = range(20)
dic_multi_nb_pairs = dict()
dic_multi_nb_pairs = {n: n*2 for n in nb_paires if n % 2 == 0}




