from tkinter import *
from random import randrange
import pygame

# initialisation de la musique
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("ultimate-snack.mp3")
    pygame.mixer.music.play(loops=-1)

# interface graphique tkinter avant commencement du jeu

fen = Tk()
fen.title('Jeu du serpent')
can = Canvas(fen, width=500, height=500, bg='#4fbd25')
can.grid(row=1, column=0, columnspan=3)
fen.iconbitmap("snake.ico")
image = PhotoImage(file="snake.png")
can.create_image(250, 250, image=image)
can.create_text(250, 250, text="Jeu du serpent", font=("Courrier", 30))
can.create_text(250, 290, text="Appuyer sur Commencer pour jouer", font=("Courrier", 15))
can.create_text(250, 400, text="Jeu créer par TadomiKa-Ari", font=("Courrier", 15))

# initialisation des variables
score = 0
direction = "Right"
snake = [(240, 240), (230, 240), (220, 240)]  # Liste des segments du serpent
snake_objects = []
recommencer_button = None

def ouvrir_jeu():
    global can, snake_objects, score, direction, snake, recommencer_button
    can.delete("all")  # Effacer le contenu du canevas
    can.config(bg='gray')
    btn_quit = Button(fen, text='quitter', command=fen.quit)
    btn_quit.grid(row=2, column=1)
    Label(fen, text='Score:  ').grid(row=0, column=0)
    Label(fen, text=score).grid(row=0, column=1)
    pomme(can)

    # Réinitialiser les variables du jeu
    score = 0
    direction = "Right"
    snake = [(240, 240), (230, 240), (220, 240)]
    snake_objects = []

    # Dessiner le serpent
    for segment in snake:
        snake_objects.append(can.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green"))

    deplacer_serpent()

    # Cacher le bouton "Recommencer" s'il existe
    if recommencer_button:
        recommencer_button.grid_forget()

def start_game():
    print("Le jeu commence !")
    Boutton.destroy()
    ouvrir_jeu()
    play_music()

def pomme(can):
    x = randrange(150, 350, 10)
    y = randrange(150, 350, 10)
    can.create_oval(x, y, x + 10, y + 10, fill='red')

def deplacer_serpent():
    global snake, snake_objects, direction, score

    # Calculer la nouvelle position de la tête du serpent
    x, y = snake[0]
    if direction == "Up":
        y -= 10
    elif direction == "Down":
        y += 10
    elif direction == "Left":
        x -= 10
    elif direction == "Right":
        x += 10

    # Vérifier les limites de la fenêtre et les collisions
    if x < 0 or x > 490 or y < 0 or y > 490 or (x, y) in snake:
        print("Game Over !")
        game_over()
        return

    # Ajouter la nouvelle position de la tête
    snake = [(x, y)] + snake[:-1]

    # Déplacer les segments du serpent
    for i, segment in enumerate(snake):
        can.coords(snake_objects[i], segment[0], segment[1], segment[0] + 10, segment[1] + 10)

    # Répéter le mouvement toutes les 100 ms
    fen.after(100, deplacer_serpent)

def game_over():
    global can, recommencer_button
    can.delete("all")
    can.config(bg="green")
    can.create_text(250, 250, text="Tu as perdu !", font=("Courrier", 30))
    can.create_text(250, 290, text="ton score est de :", font=("Courrier", 15))
    can.create_text(250, 320, text=score, font=("Courrier", 15))
    recommencer_button = Button(fen, text="Recommencer", command=start_game)
    recommencer_button.grid(row=2, column=2)

def changer_direction(event):
    global direction
    if event.keysym == "Up" and direction != "Down":
        direction = "Up"
        print("haut")
    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"
        print("bas")
    elif event.keysym == "Left" and direction != "Right":
        direction = "Left"
        print("gauche")
    elif event.keysym == "Right" and direction != "Left":
        direction = "Right"
        print("droite")

# Bouton pour commencer
Boutton = Button(fen, text='Commencer', command=start_game)
Boutton.grid(row=0, column=1)

# Bouton pour quitter
btn_quit = Button(fen, text='quitter', command=fen.quit)
btn_quit.grid(row=2, column=1)

# déplacement touche
fen.bind_all('<Up>', changer_direction)
fen.bind_all('<Down>', changer_direction)
fen.bind_all('<Right>', changer_direction)
fen.bind_all('<Left>', changer_direction)

# affichage de la fenetre   
fen.mainloop()