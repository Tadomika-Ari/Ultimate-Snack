from tkinter import *
from random import randrange
import random

# interface graphique tkinter

fen = Tk()
fen.title('Jeu du serpent')
can = Canvas(fen,width = 500, height = 500 , bg = 'gray')
can.grid(row=1,column=0,columnspan=3)

# Bonton pour commencer

Boutton=Button(fen, text='Commencer')
Boutton.grid(row=0, column=1)

# Bouton pour quitter

btn_quit = Button(fen, text='quitter', command=fen.quit)
btn_quit.grid(row=2 , column=1)



# affichage de la fenetre   

fen.mainloop()



