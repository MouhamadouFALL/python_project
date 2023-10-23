
# on demande l'age à l'utilisateur puis on vérifie si l'age est inférieur ou supérieur à 18 ans.
# Donnez votre âge :
# if age >= 18:
#   vous etes majeur
# else:
#   vous etes encore mineur

age = None
age = int(input("Enter your age: "))
if age >= 18:
    print("you are over 18.")
else:
    print("You are still a minor")