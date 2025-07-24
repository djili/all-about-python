import math

class Calculatrice:
    def __init__(self):
        self.historique = []

    def ajouter_historique(self, operation, resultat):
        ligne = f"{operation} = {resultat}"
        self.historique.append(ligne)
        with open("historique.txt", "a") as f:
            f.write(ligne + "\n")

    def addition(self, a, b):
        res = a + b
        self.ajouter_historique(f"{a} + {b}", res)
        return res

    def soustraction(self, a, b):
        res = a - b
        self.ajouter_historique(f"{a} - {b}", res)
        return res

    def multiplication(self, a, b):
        res = a * b
        self.ajouter_historique(f"{a} * {b}", res)
        return res

    def division(self, a, b):
        if b == 0:
            raise ValueError("Division par zéro interdite.")
        res = a / b
        self.ajouter_historique(f"{a} / {b}", res)
        return res

    def puissance(self, a, b):
        res = a ** b
        self.ajouter_historique(f"{a} ** {b}", res)
        return res

    def racine(self, a):
        if a < 0:
            raise ValueError("Impossible de calculer la racine carrée d’un nombre négatif.")
        res = math.sqrt(a)
        self.ajouter_historique(f"√{a}", res)
        return res

    def sinus(self, a):
        res = math.sin(math.radians(a))
        self.ajouter_historique(f"sin({a})", res)
        return res

    def menu(self):
        print("""
              === CALCULATRICE ===
              1. Addition
              2. Soustraction
              3. Multiplication
              4. Division
              5. Puissance
              6. Racine carrée
              7. Sinus
              0. Quitter
              """)

    def demarrer(self):
        while True:
            self.menu()
            choix = input("Choisissez une option : ")
            try:
                if choix == "1":
                    a = float(input("a = "))
                    b = float(input("b = "))
                    print("Résultat :", self.addition(a, b))
                elif choix == "2":
                    a = float(input("a = "))
                    b = float(input("b = "))
                    print("Résultat :", self.soustraction(a, b))
                elif choix == "3":
                    a = float(input("a = "))
                    b = float(input("b = "))
                    print("Résultat :", self.multiplication(a, b))
                elif choix == "4":
                    a = float(input("a = "))
                    b = float(input("b = "))
                    print("Résultat :", self.division(a, b))
                elif choix == "5":
                    a = float(input("a = "))
                    b = float(input("b = "))
                    print("Résultat :", self.puissance(a, b))
                elif choix == "6":
                    a = float(input("a = "))
                    print("Résultat :", self.racine(a))
                elif choix == "7":
                    a = float(input("a (en degrés) = "))
                    print("Résultat :", self.sinus(a))
                elif choix == "0":
                    print("Fin du programme.")
                    break
                else:
                    print("Choix invalide.")
            except ValueError as ve:
                print("Erreur :", ve)
            except Exception as e:
                print("Erreur inattendue :", e)

# Lancer la calculatrice
if __name__ == "__main__":
    calc = Calculatrice()
    calc.demarrer()