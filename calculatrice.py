nb1 = input("Entrez un premier nombre : ")
nb2 = input("Entrez un second nombre : ")

while not nb1.isdigit() or not nb2.isdigit():
    print("Veuillez rentrer des nombres SVP")
    nb1 = input("Entrez un premier nombre : ")
    nb2 = input("Entrez un second nombre : ")

operateur = ""

while operateur != "-" or operateur != "+" or operateur != "/" or operateur != "*":
    operateur = input("Veuillez choisir un opérateur parmis les suivants (- + / *) : ")
    if operateur == "-" or operateur == "+" or operateur == "/" or operateur == "*":
        break

nb1 = int(nb1)
nb2 = int(nb2)

if operateur == '-':
    print(f"Le résultat de {nb1} - {nb2} est égal à {nb1 - nb2}")
elif operateur == '+':
    print(f"Le résultat de {nb1} + {nb2} est égal à {nb1 + nb2}")
elif operateur == '/':
    print(f"Le résultat de {nb1} / {nb2} est égal à {nb1 / nb2}")
elif operateur == '*':
    print(f"Le résultat de {nb1} * {nb2} est égal à {nb1 * nb2}")
else:
    print("L'opération n'est pas possible")