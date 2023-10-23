
import re

# Lire un Text puis return ligne par ligne
def read_file_line(pathFile):
    """ Lire le fichier puis retourne chaque ligne du fichier """

    with open(pathFile) as fread:
        for line in fread:
            yield line


# retoune tous les mots unique dans un text
def mots_unique(pathFile):
    """ retourne tous les mots unique dans Text """

    mots = set()
    for line in read_file_line(pathFile):
        res = re.findall(r'[\w\.-]+', line)
        for mot in res:
            mots.add(mot)

        #mots = {mots.add(mot) for mot in res}

    return mots

print(mots_unique('chanson.txt'))
