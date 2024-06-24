import random

intervalle_max = int(input("Choisissez un nombre qui permettra de jauger l'intervalle du nombre que vous devez trouver : "))

nombre_a_trouver = random.randint(1, intervalle_max)

print(f"Vous devez trouver un nombre entre 0 et {intervalle_max}")

nb_tours = int(input("Combien de tours voulez-vous avoir pour trouver le nombre ? "))

bon_nombre = 0

while nb_tours > 0:
    bon_nombre = int(input("Entrez un nombre : "))
    nb_tours -= 1
    if nb_tours == 0: 
        print("Perdu !")
        break
    print(f"Il vous reste {nb_tours} essais avant de perdre")


    if nombre_a_trouver == bon_nombre:
        print(f"Félicitations tu as gagné le nombre à trouver était {nombre_a_trouver} ")
        break

