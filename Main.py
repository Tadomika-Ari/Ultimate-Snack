from tkinter import *
from random import randrange
from random import *


# interface graphique tkinter avant commencement du jeu

fen = Tk()
fen.title('Jeu du serpent')
can = Canvas(fen,width = 500, height = 500 , bg = '#4fbd25')
can.grid(row=1,column=0,columnspan=3)
fen.iconbitmap("snake.png")
image = PhotoImage(file="snake.png")
can.create_image(250, 250, image=image,)
can.create_text(250,250,text="Jeu du serpent", font=("Courrier", 30))
can.create_text(250,290,text="Appuyer sur Commencer pour jouer", font=("Courrier", 15))
can.create_text(250,400,text="Jeu créer par TadomiKa-Ari", font=("Courrier", 15))


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
    set(score=0)
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
