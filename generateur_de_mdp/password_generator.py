import os
from tkinter import *
from PIL import Image, ImageTk
import string
from random import *

# Fonction de génération de MDP
def generate_password():
    password_min = 8
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, 12)))
    insertion_mdp.delete(0, END)
    insertion_mdp.insert(0, password)

# Création et Configuration de la fenêtre
window = Tk()
window.title("Générateur de MDP")
window.geometry("1080x720")
icon_path = os.path.join(os.path.dirname(__file__), "logo_cadena.ico")
window.iconbitmap(icon_path)
window.config(background='#4065A4')
window.minsize(640, 360)

# Création frame principale
frame = Frame(window, bg='#4065A4')

# Création de l'Image
width = 300
height = 300
image_path = os.path.join(os.path.dirname(__file__), "password_onboarding.jpg")
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=photo)
canvas.grid(row=0, column=0, sticky=W)

# Créer une sous boite 
right_frame = Frame(frame, bg='#4065A4')

# Création d'un titre 
label_title = Label(right_frame, text="Mot de Passe", font=("Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

# Création d'un champ de saisie
insertion_mdp = Entry(right_frame, text="Mot de Passe", font=("Helvetica", 20), bg='#EEF1FF', fg='black')
insertion_mdp.pack()

# Création d'un bouton
generate_password_button = Button(right_frame, text="Générer MDP", font=("Helvetica", 20), bg='#23358E', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

# Afficher la frame
frame.pack(expand=YES)

# Création d'une barre de menu 
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)


menu_bar.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)

# file_menu2 = Menu(menu_bar, tearoff=0)

# menu_bar.add_cascade(label="Fichier 2", menu=file_menu2)
# file_menu2.add_command(label="Nouveau 2", command=generate_password)
# file_menu2.add_command(label="Quitter 2", command=window.quit)


window.config(menu=menu_bar)

# Lancement de la fenêtre
window.mainloop()




