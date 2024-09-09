

from math import *
from statistics import *
from collections import deque
import heapq


### 1.1. Unpacking a Sequence into Separate Variable 
    #(Décomposition d'une séquence en variables séparées)

    # Problème
        # Vous disposez d'un tuple ou d'une séquence à N éléments 
        # que vous souhaitez décomposer en une collection de N variables.
    # Solution
        # Toute séquence (ou itérable) peut être décomposée en variables 
        # à l'aide d'une simple opération d'affectation. 
        # La seule condition est que le nombre de variables et la structure correspondent à la séquence.

p = (4, 5)
x, y = p
print(x, ',', y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]

name, shares, price, date = data
print(name, shares, price, date)

name, shares, price, (year, month, day) = data
print(name, shares, price, year, month, day)

### Message d'erreur:
    # x, y, z = (, 5)   # ValueError: not enough values to unpack (expected 3, got 2)
                        # pas assez de valeurs à décompresser (attendu 3, obtenu 2) 
    # x, x = (4, 5, 6)  # ValueError: too many values to unpack (expected 2)
                        # trop de valeurs à décompresser (attendu 2)

# ignorer certaines données de la séquence de donnée
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares, price)

# Discussion
    # Le déballage fonctionne en fait avec n'importe quel objet itérable, 
    # et pas seulement avec les tuples ou les listes. Cela inclut les chaînes de caractères, 
    # les fichiers, les itérateurs et les générateurs.
    # Cependant, assurez-vous que le nom de la variable que vous choisissez 
    # n'est pas déjà utilisé pour quelque chose d'autre.

datel = ['ACME', 50, 91.1, (2012, 12, 21), ['e', 12, 'BBBE']]
*_, date, l = datel
print(l)

# 1.2. Décompression d'éléments à partir d'itérables de longueur arbitraire
    # Problème
        # Vous devez décompresser N éléments d'un itérable, 
        # mais l'itérable peut être plus long que N éléments, 
        # ce qui provoque une exception (“too many values to unpack”) 

    # Solution:
        # Python “star expressions” can be used to address this problem. For example, suppose
        # you run a course and decide at the end of the semester that you’re going to drop the first
        # and last homework grades, and only average the rest of them.

def drop_first_last(grades):
    first, *middle, last = grades
    return mean(middle) # moyenne

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name, email, phone_numbers)

records = [
 ('foo', 1, 2),
 ('bar', 'hello'),
 ('foo', 3, 4),
]

def do_foo(s, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# Le déballage en étoile peut également être utile lorsqu'il est combiné à certains types d'opérations 
# de traitement des chaînes de caractères, telles que le fractionnement

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(name, homedir, sh)

# Il peut arriver que vous souhaitiez décompresser des valeurs et les jeter. 
# Vous ne pouvez pas spécifier un simple * lors du décompactage, 
# mais vous pouvez utiliser un nom de variable à jeter courant (_) ou (ign) (ignoré)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record # name, *ign, (*ign, year) = record
print(name, year)

# For example, if you have a list, you can easily split it into head and tail components like this:

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head, tail)

# On pourrait imaginer d'écrire des fonctions qui effectuent 
# un tel découpage afin d'exécuter une sorte de récursivité intelligente. 
# une sorte d'algorithme récursif astucieux.
def somme(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(somme(items))

# 1.3. Keeping the Last N Items
    # Problem
        # Vous souhaitez conserver un historique limité des derniers éléments 
        # vus au cours d'une itération ou d'un autre type de traitement.
    # Solution:
        # La conservation d'un historique limité est une utilisation parfaite de collections.deque. 
        # exemple, le code suivant effectue une simple recherche de texte sur une séquence de lignes 
        # et produit la ligne correspondante ainsi que les N lignes de contexte précédentes 
        # lorsqu'elles sont trouvées

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
with open("efile.txt") as f:
    for line, prevlines in search(f, 'pyhton', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.appendleft(5)
print(q)
q.pop()
print(q)
q.popleft()
print(q)




# Lorsque l'on écrit du code pour rechercher des éléments, il est courant d'utiliser une fonction de générateur in-volving yield, comme le montre la solution de cette recette. 
# Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is automatically removed.

# 1.4. Finding the Largest or Smallest N Items
    # Problem:
        # You want to make a list of the largest or smallest N items in a collection
    # Solution:
        # The heapq module has two functions—nlargest() and nsmallest()—that do exactly what you want.

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
p_gd = heapq.nlargest(4, nums) # 4 elts les plus grands
p_pt = heapq.nsmallest(3, nums) # 3 ets les plus petit de la liste
print(p_gd)
print(p_pt)

portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)

# 1.5. Implementing a Priority Queue (Mise en œuvre d'une file d'attente prioritaire)
    # Problem
        # 







