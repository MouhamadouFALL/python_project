
import sys
import pathlib
import sqlite3

from tkinter import Tk, Frame, Text, filedialog, messagebox, END

app = Tk()
app.title("10 SITES LES PLUS VISITES")
fenetre = Frame(app)
zone_texte = Text(fenetre, height=30, width=70)
zone_texte.pack()
fenetre.pack()

dossier_profil = filedialog.askdirectory()
if not dossier_profil:
    sys.exit(0)

history = pathlib.Path(dossier_profil) / "History"

if not history.is_file():
    messagebox.showwarning("Erreur", "Imposssible de trouver le fichier ")
    sys.exit(1)


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
    
    for site, score in dict_hist.items():
        line = site + " : " + str(score) + " visites.\n"
        zone_texte.insert(END, line)


app.mainloop()






