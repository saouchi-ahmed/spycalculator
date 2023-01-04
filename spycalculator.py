
# Couleurs -
# Noir: #101419
# Bleu: #476C9B
# Rouge: #984447

"""
----
789*
456-
123+
0,/=
----
"""

from tkinter import *
from tkinter import Tk
def dechifre (string):

    liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    f = open(string, "r")
    message = f.read()

    box = ''
    textclair = ''
    for c in message:

        if c == '.':

            textclair = textclair + liste[int(box)]
            box = ''
        else:
            box = box + c


    f.close()

    return textclair
#C:/Users/HP/Desktop/python/pythonProject/projet GL/text++
def write( string,path):
    liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    textchifre = ""
    message = string
    for c in message:
        for a in liste:
            if c == a:
                textchifre = textchifre + str(liste.index(c)) + "."

    print('chifre:', textchifre)
    f = open(path, "w")
    f.write(textchifre)
    f.close()



def windowB (path):
    window=Toplevel(gui)
    window.geometry("200x200")
    window.resizable(False,False)
    v1 = StringVar()
    textbox = Entry(window, textvariable=v1)
    textbox.place(x=10,y=10,width=170)
    btnwrite = Button(window, text='write', width=5, command= lambda :write(str(v1.get()),path=path) & label.configure(text="okk"))
    btnwrite.place(x=70,y=30,width=50)
    label=Label(window,text="")
    label.place(x=70,y=60,width=50)


def new() :
    window=Toplevel(gui)
    window.geometry("200x200")
    window.resizable(True,False)
    v1 = StringVar()

    textbox = Entry(window, textvariable=v1)
    textbox.place(width=175,x=10,y=10)


    label=Label(window,text="text dechifre")
    label.place(x=50,y=40)
    btndechifre = Button(window, text='dechifre', width=5, command= lambda :label.configure(text=dechifre(str(v1.get()))))
    btndechifre.place(x=70,y=60 ,width=50)
    btnwrite = Button(window, text='write', width=5, command= lambda :windowB(path=str(v1.get())))
    btnwrite.place(x=70,y=90,width=50)
##############################################################################
expression = ""
def appuyer(touche):
    if touche == "=":
        calculer()
        return

    global expression
    expression += str(touche)
    equation.set(expression)


def calculer():
    try:
        global expression
        if expression == "+++":
            new()
        total = str(eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression = ""


def effacer():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()

    # Couleur de fond
    gui.configure(background="#101419")

    # Titre de l'application
    gui.title("Calculatrice")

    # Tailler de la fenetre
    gui.geometry("190x355")

    # Variable pour stocker le contenu actual
    equation = StringVar()

    # Boite de resultats
    resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2,width=5)
    resultat.grid(columnspan=4)

    # Boutons
    boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]
    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#476C9B", fg="#FFF", height=4, width=6)
        # Rendre le texte cliquable
        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1

    # Bouton pour effacer
    b = Label(gui, text="Effacer", bg="#984447", fg="#FFF", height=4, width=27)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=50)

    # Demarrer l'interface graphique
    gui.mainloop()
    ############################################################################################