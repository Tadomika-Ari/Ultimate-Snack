from tkinter import *
from random import randrange
import random

# interface graphique tkinter avant commencement du jeu

fen = Tk()
fen.title('Jeu du serpent')
can = Canvas(fen,width = 300, height = 300 , bg = 'white')
can.grid(row=1,column=0,columnspan=3)

# interface graphique du jeu

def ouvrir_jeu():
    jeu = Tk()
    jeu.title('Jeu du serpent')
    can = Canvas(jeu,width = 500, height = 500 , bg = 'gray')
    can.grid(row=1,column=0,columnspan=3)
    btn_quit = Button(jeu, text='quitter', command=fen.quit)
    btn_quit.grid(row=2 , column=1)


def start_game():
    print("Le jeu commence !")
    Boutton.destroy()
    ouvrir_jeu()
    fen.destroy()

# Bonton pour commencer

Boutton = Button(fen, text='Commencer', command=start_game)
Boutton.grid(row=0, column=1)

# Bouton pour quitter

btn_quit = Button(fen, text='quitter', command=fen.quit)
btn_quit.grid(row=2 , column=1)



# affichage de la fenetre   

fen.mainloop()




