import math

def afficher_menu():
    print("\n=== CALCULATRICE SIMPLE ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Racine carrée")
    print("7. Sinus")
    print("8. Cosinus")
    print("9. Logarithme")
    print("10. Quitter")

def demander_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

def addition(a, b): return a + b
def soustraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b
def puissance(a, b): return a ** b
def racine(a):
    if a < 0:
        return "Erreur : racine carrée d’un nombre négatif"
    return math.sqrt(a)
def sinus(a): return math.sin(math.radians(a))
def cosinus(a): return math.cos(math.radians(a))
def logarithme(a):
    if a <= 0:
        return "Erreur : le logarithme nécessite un nombre > 0"
    return math.log10(a)

def calculatrice():
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-10) : ")

        if choix == "10":
            print("Merci d’avoir utilisé la calculatrice.")
            break

        if choix in ["1", "2", "3", "4", "5"]:
            a = demander_nombre("Entrez le premier nombre : ")
            b = demander_nombre("Entrez le deuxième nombre : ")

            if choix == "1":
                resultat = addition(a, b)
                print(f"{a} + {b} = {resultat}")
            elif choix == "2":
                resultat = soustraction(a, b)
                print(f"{a} - {b} = {resultat}")
            elif choix == "3":
                resultat = multiplication(a, b)
                print(f"{a} * {b} = {resultat}")
            elif choix == "4":
                resultat = division(a, b)
                print(f"{a} / {b} = {resultat}")
            elif choix == "5":
                resultat = puissance(a, b)
                print(f"{a} ^ {b} = {resultat}")

        elif choix in ["6", "7", "8", "9"]:
            a = demander_nombre("Entrez un nombre : ")

            if choix == "6":
                resultat = racine(a)
                print(f"√{a} = {resultat}")
            elif choix == "7":
                resultat = sinus(a)
                print(f"sin({a}) = {resultat}")
            elif choix == "8":
                resultat = cosinus(a)
                print(f"cos({a}) = {resultat}")
            elif choix == "9":
                resultat = logarithme(a)
                print(f"log({a}) = {resultat}")
        else:
            print("Choix invalide.")
            continue

        encore = input("Souhaitez-vous faire une autre opération ? (o/n) : ")
        if encore.lower() != "o":
            print("Fin du programme.")
            break

# Lancer la calculatrice
calculatrice()
