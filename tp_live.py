
print("Taper le numero de votre operation")
print("1 - Addition")
print("2 - Soustraction")
print("3 - division")
print("4 - multiplication")

operation_choisit = input("Tapez : ")

def addition(n1, n2):
    resultat = n1 + n2
    return resultat

if(operation_choisit == "1"): # Ne pas confondre == comparaison et = affectation
    nombre_clavier_1 = input("Donne moi le premier nombre : ")
    nombre_clavier_2 = input("Donne moi le second nombre : ")
    nombre_1 = float(nombre_clavier_1)
    nombre_2 = float(nombre_clavier_2)
    print(type(nombre_clavier_1))
    print(type(nombre_1))
    resultat = addition(nombre_1, nombre_2)
    print(f"Addition de {nombre_1} et {nombre_2} = {resultat}")
    
elif(operation_choisit == "2"):
    print("Soustraction")    
    
elif(operation_choisit == "3"):
    print("Division")       
    
elif(operation_choisit == "4"):
    print("Multiplication")  
       
else:
    print("Le chiffre n'est pas dans la liste")       
 
from math import exp 
def puissance(p0, t):
    return p0(1 - exp(t))
