from poudelard.univers.personnage import *

def introduction():
    print("Bienvenue dans le Monde Magique !")
    print("Vous êtes sur le point vivre la genèse de votre histoire.")
    input()


def creer_personnage():
    attributs={}
    nom=str(input("Entrez le nom de votre personnage : "))
    prenom=str(input("Entrez le prénom de votre personnage : "))
    print("\n")
    print("\n")
    print("Choisissez vos attributs : ")
    courage=int(input("Niveau de courage (1-10) : "))
    while courage<1 or courage>10:
        courage=int(input("Niveau de courage (1-10) : "))
    attributs["Courage"]=courage

    intelligence=int(input("Niveau d'intelligence (1-10) : "))
    while intelligence<1 or intelligence>10:
        intelligence=int(input("Niveau d'intelligence (1-10) : "))
    attributs["Intelligence"]=intelligence

    loyaute=int(input("Niveau de loyauté (1-10) : "))
    while loyaute<1 or loyaute>10:
        loyaute=int(input("Niveau de loyauté (1-10) : "))
    attributs["Loyaute"]=loyaute

    ambition=int(input("Niveau de ambition (1-10) : "))
    while ambition<1 or ambition>10:
        ambition=int(input("Niveau de ambition (1-10) : "))
    attributs["Ambition"]=ambition

    print("Profil du personnage : \n")
    print(initialiser_personnage(nom,prenom,attributs))


