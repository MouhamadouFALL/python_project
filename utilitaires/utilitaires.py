
""" 
    un module qui regroupe un ensemble de fonction utile
"""


def listing(iterable, bullet='- '):
    """ Retourne une chaine à afficher.

        Le listing affiche les elements de l'iterable
        un par un, ligne par ligne, annotes par des tirets  
    """
    
    items = []
    for elt in iterable:
        items.append("%s %s" % (bullet, elt))
        
    return "\n".join(items)


def moyenne(*nombres):
    """ Retourne la moyennes des parametres """
    
    if not nombres:
        raise ValueError("Vous devez passer en parametres des valeurs")
    return sum(nombres) / len(nombres)

def censure(entree, sortie, **substitutions):
    """ Censure les mots d'un fichier texte. """
    
    with open(entree) as source, open(sortie, 'w') as dest:
        for line in source:
            for mot, remplacement in substitutions.items():
                line = line.replace(mot, remplacement)
            dest.write(ligne)
   
# cette fonction est plus rapide mais utilise de la memoire            
def censure_v2(entree, sortie, **substitutions):
    """ Censure les mots d'un fichier texte. """
    
    with open(source) as source, open(sortie, 'w') as dest:
        texte = source.read()
        for mot, remplacement in substitutions.items():
            texte = texte.replace(mot, remplacement)
        dest.write(texte)
        

def mots(*pathfile):
    ponctuations = (";", ",", ":", ".", "<<", ">>", "'", "?", "!", "-")
    
    for path in pathfile:
        with open(path) as f:
            for line in f:
                for sign in ponctuations:
                    line = line.lower().replace(sign, "")
                    for mot in line.split():
                        yield mot

    