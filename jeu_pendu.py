import getpass

mot = getpass.getpass("Entrez le mot à trouver : ")

liste = []
votre_liste = []

for x in mot:
    liste.append(x)
    votre_liste.append(' _ ')

print("".join(votre_liste))

nb_erreur = 9

while nb_erreur > 0:
    print(f"Vous avez {nb_erreur} tentatives avant de perdre")

    lettre = input("Veuillez saisir une lettre ou le mot que vous pensez avoir trouvé : ")

    if len(lettre) > 1:
        if lettre == mot:
            print(f"Félicitations ! Vous avez trouvé le mot : {lettre}")
            break
    
    if lettre in liste:
        for (x,y) in enumerate(liste):
            if y == lettre:
                votre_liste[x] = y

        v = "".join(votre_liste)
        print(f"La lettre {lettre} est bien dans le mot")
        print(v)

    else:
        nb_erreur -= 1
        print(f"La lettre {lettre} n'est pas dans le mot")
        print(f"Il vous reste {nb_erreur} tentatives")

if nb_erreur == 0:
    print("Vous avez perdu")