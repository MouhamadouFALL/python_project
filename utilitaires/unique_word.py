# -*- coding: utf-8 -*-
# Trouver tous les mots unique dans un text 

    # lire le fichier 
    # tout mettre en minuscule
    # remplacer les poinctuations par de chaines vides
    # retire les espaces et les sauts de ligne
    # retire les doublons

ponctuations = (",", ".", ";", "«", "»", "'", "?", "-")
file = open(r"c:\Users\Naby FALL\Desktop\Python\python_project\programmer_en_python\chanson.txt")
text = file.read().lower()

for item in ponctuations:
    text = text.replace(item, "")

mots = set(text.split())
for mot in mots:
    print(mot)

file.close()