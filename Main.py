from tkinter import *
from random import randrange
from random import *

# interface graphique tkinter avant commencement du jeu

fen = Tk()
fen.title('Jeu du serpent')
can = Canvas(fen,width = 150, height = 150 , bg = 'white')
can.grid(row=1,column=0,columnspan=3)
can.create_text(75,75,text="Jeu du serpent")

# interface graphique du jeu

def ouvrir_jeu():
    jeu = Tk()
    jeu.title('Jeu du serpent')
    can = Canvas(jeu,width = 500, height = 500 , bg = 'gray')
    can.grid(row=1,column=0,columnspan=3)
    btn_quit = Button(jeu, text='quitter', command=fen.quit)
    btn_quit.grid(row=2 , column=1)
    Label(jeu, text='Score:  ').grid(row=0,column=0)
    Label(jeu, text=scores).grid(row=0,column=1)


def start_game():
    print("Le jeu commence !")
    Boutton.destroy()
    ouvrir_jeu()
    fen.destroy()

def pomme ():
    x =randrange(150,150,150)
    y = randrange(150,150,150)
    can.create_oval(x,y,x+5,y+5,fill='red')

def scores ():
    set(score=10)
    if pomme == True:
        score = score + 1
        print(score)
        return score



# Bonton pour commencer

Boutton = Button(fen, text='Commencer', command=start_game)
Boutton.grid(row=0, column=1)

# Bouton pour quitter

btn_quit = Button(fen, text='quitter', command=fen.quit)
btn_quit.grid(row=2 , column=1)


# affichage de la fenetre   

fen.mainloop()



