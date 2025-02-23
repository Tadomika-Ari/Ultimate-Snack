from tkinter import *
from random import randrange
from random import random
import pygame


# initialisation de la musique
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("ultimate-snack.mp3")
    pygame.mixer.music.play(loops=-1)



# interface paramètre son

def parametre():
    reglage = Tk()
    reglage.title('Paramètre son')
    can = Canvas(reglage, width=100, height=100)
    can.grid(row=1, column=0, columnspan=3)
    reglage.iconbitmap("snake.ico")
    can.create_text(250, 250, text="Paramètre son", font=("Courrier", 30))
    augmenter_son = Button(reglage, text="Augmenter le son")
    augmenter_son.grid(row=2, column=0)
    baisser_son = Button(reglage, text="Baisser le son")
    baisser_son.grid(row=2, column=1)
    couper_son = Button(reglage, text="Couper le son")
    couper_son.grid(row=2, column=2)
    btn_reglage = Button(reglage, text='quitter', command=reglage.destroy)
    btn_reglage.grid(row=3, column=1)


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
fen_reglage = Button(fen, text="Reglage", command=parametre)
fen_reglage.grid(row=2, column=0)




# initialisation des variables
score = 0
direction = "Right"
snake = [(240, 240), (230, 240), (220, 240)]  # Liste des segments du serpent
snake_objects = []
recommencer_button = None
walls = []
pomme_obj = None
pomme_pos = (0, 0)

def ouvrir_jeu():
    global can, snake_objects, score, direction, snake, recommencer_button, walls, pomme_obj, pomme_pos
    can.delete("all")  # Effacer le contenu du canevas
    can.config(bg='gray')
    btn_quit = Button(fen, text='quitter', command=fen.quit)
    btn_quit.grid(row=2, column=1)
    Label(fen, text='Score précédant :  ').grid(row=0, column=0)
    Label(fen, text=score).grid(row=0, column=1)

    # Réinitialiser les variables du jeu
    score = 0
    direction = "Right"
    snake = [(240, 240), (230, 240), (220, 240)]
    snake_objects = []
    walls = []

    # Dessiner le serpent
    for segment in snake:
        snake_objects.append(can.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green"))

    # Créer des murs aléatoires
    creer_murs(can, randrange(1, 10, 1))  # Par exemple, créer 10 murs

    # Créer une pomme
    pomme_pos = pomme(can)

    deplacer_serpent()

    # Cacher le bouton "Recommencer" s'il existe
    if recommencer_button:
        recommencer_button.grid_forget()

def start_game():
    print("Le jeu commence !")
    Boutton.destroy()
    fen_reglage.destroy()
    ouvrir_jeu()
    play_music()

def pomme(can):
    global pomme_obj
    x = randrange(0, 500, 10)
    y = randrange(0, 500, 10)
    pomme_obj = can.create_oval(x, y, x + 10, y + 10, fill='red')
    return (x, y)

def creer_murs(can, nombre_murs):
    global walls
    for _ in range(nombre_murs):
        x = randrange(0, 500, 10)
        y = randrange(0, 500, 10)
        wall = can.create_rectangle(x, y, x + 10, y + 10, fill='black')
        walls.append((x, y))

def deplacer_serpent():
    global snake, snake_objects, direction, score, walls, pomme_pos

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
    if x < 0 or x > 490 or y < 0 or y > 490 or (x, y) in snake or (x, y) in walls:
        print("Game Over !")
        game_over()
        return

    # Vérifier si le serpent mange la pomme
    if (x, y) == pomme_pos:
        score += 1
        can.delete(pomme_obj)
        pomme_pos = pomme(can)
        # Ajouter un nouveau segment au serpent
        snake.append(snake[-1])
        snake_objects.append(can.create_rectangle(snake[-1][0], snake[-1][1], snake[-1][0] + 10, snake[-1][1] + 10, fill="green"))

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