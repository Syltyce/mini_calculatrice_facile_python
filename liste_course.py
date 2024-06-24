choix = ""
liste = []

while choix != "5":
    print("Choisissez une option parmi les 5 suivantes : ")
    print("1 : Ajouter un  élément à la liste")
    print("2 : Retirer un élément de la liste")
    print("3 : Afficher la liste")
    print("4 : Vider la liste")
    print("5 : Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        element = input("Entrez l'élement que vous souhaitez ajouté à la liste : ")
        liste.append(element)
        print(f"L'élément {element} a bien été ajouté à la liste")

    elif choix == "2":
        element_a_suppr = input("Quel élément souhaitez-vous supprimer : ")
        if element_a_suppr in liste:
            liste.remove(element_a_suppr)
            print(f"L'élément {element_a_suppr} a bien été supprimé à la liste")
        else:
            print(f"L'élément {element_a_suppr} n'existe pas")
    
    elif choix == "3":
        if liste:
            print("Voici le contenu de la liste : ")
            for i, item in enumerate(liste, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste est vide")

    elif choix == "4":
        liste.clear()
        print("La liste a été vidé")

    elif choix == "5":
        print("Merci et à bientôt")

    else:
        print("Choix incorrect")
