from poudelard.univers.personnage import *
from poudelard.utils.input_utils import *

def introduction():
    print("Bienvenue dans le Monde Magique !")
    print("Vous êtes sur le point vivre la genèse de votre histoire.")
    input()


def creer_personnage():
    attributs={}
    nom=demander_texte("Entrez le nom de votre personnage : ")
    prenom=demander_texte("Entrez le prénom du personnage : ")
    print("\n")
    print("\n")
    print("Choisissez vos attributs : ")
    courage=demander_nombre("Niveau de courage", 1,10)
    attributs["Courage"]=courage

    intelligence=demander_nombre("Niveau d'intelligence", 1,10)
    attributs["Intelligence"]=intelligence

    loyaute=demander_nombre("Niveau de loyauté", 1,10)
    attributs["Loyaute"]=loyaute

    ambition=demander_nombre("Niveau de ambition", 1,10)
    attributs["Ambition"]=ambition

    print("Profil du personnage : \n")
    print(initialiser_personnage(nom,prenom,attributs))

def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard... \n")
    print("Cher élève, Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard !  \n")
    chx=demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?", ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."])
    if chx == 2:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: \n")
        print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » \n")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit()

def rencontrer_hagrid(personnage):
    print("Hagrid :  Salut ", personnage["Prénom"], "! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse. ")
    c=demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if c == 2:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")

def acheter_fourniture(personnage):
    dico_shop=load_fichier(data/inventaire.json)
    print("Bienvenue sur le Chemin de Traverse !")