

try:
    file = open("path")
except EnvironmentError as e:
    print("Impossible d'ouvrir le fichier. [", e, "]")
else:
    text = file.read()
finally:
    try:
        file.close()
    except NameError:
        pass

### Les Contexts Manager
with open("path") as file:
        text = file.read()
    # Ou pour etre plus clair        
try:
    with open("path") as file:
        text = file.read()
except EnvironmentError as e:
    print("Impossible d'ouvrir le fichier. [", e, "]")


# Faire du Debug
import pdb; pdb.set_trace()
    # les arguments
        # l: permet de montrer notre posistion dans le programme
        # n: pour continuer à debugger le programme d'une ligne
        # nomVar: entrer nom variable pour afficher son contenu
        # 