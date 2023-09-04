
# Gestion des saisies

while True:
    try:
        identifiant = int(input("Enter you Identifiant: "))
        break
    except ValueError:
        print("!!! Attention l'entré n'est pas valide. Veuillez réessayer ...")


enter = None

# Le dernier bloc sera afficher quelque soit le cas
while True:
    try:
        enter = int(input("Enter you Identifiant: "))
        break
    except ValueError:
        print("!!! Attention l'entré n'est pas valide. Veuillez réessayer ...")
    finally:
        print("L'identifiant est composé de de chiffre uniquement.")


# Utiliser la classe d'exception: ZeroDivisionError
try:
    enter / 0
except ZeroDivisionError:
    pass # Ne rien mangé

# Raise NameError
