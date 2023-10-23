

# Parcourir les fichiers d'un mot répertoire et identifier le mot le plus utilisé

    # parcourir le repertoire puis lire les fichiers un à un 
    # stocké le contenu, retirer les ponctuations puis recupérer les mots un à un
    # stocké le compteur dans un dictionnaire puis l'incrément au fur et à mesure
    # Indiquer le mot le plus utilisé 


import pathlib

directory = pathlib.Path(r"C:\Users\Naby FALL\Desktop\Python\python_project\repertoire")

stats = {}

ponctuations = (",", ".", ";", "«", "»", "'", "?", "-")
for path in directory.iterdir():
    file = open(str(path))

    text = file.read().lower()

    for signe in ponctuations:
        text = text.replace(signe, "")

    for mot in text.split():
        if len(mot) >= 2:
            if mot in stats:
                stats[mot] += 1
            else:
                stats[mot] = 1
        
mot_le_plus_utilise = None
score_max = 0

for mot, score in stats.items():
    if score > score_max:
        score_max = score
        mot_le_plus_utilise = mot

print("Le mot le plus utilisé: ")
print(mot_le_plus_utilise, ":", score_max)