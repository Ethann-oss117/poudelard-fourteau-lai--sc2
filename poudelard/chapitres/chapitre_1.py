from poudelard.univers import personnage
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
    print("Choisissez vos attributs : \n")
    courage=demander_nombre("Niveau de courage", 1,10)
    attributs["Courage"]=courage

    intelligence=demander_nombre("Niveau d'intelligence", 1,10)
    attributs["Intelligence"]=intelligence

    loyaute=demander_nombre("Niveau de loyauté", 1,10)
    attributs["Loyaute"]=loyaute

    ambition=demander_nombre("Niveau de ambition", 1,10)
    attributs["Ambition"]=ambition
    afficher_personnage(initialiser_personnage(nom, prenom, attributs))
    return initialiser_personnage(nom, prenom, attributs)


def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard... \n")
    print("Cher élève, Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard !  \n")
    chx=demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ? \n", ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."])
    if chx == 2:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: \n")
        print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » \n")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit()

def rencontrer_hagrid(personnage):
    print("Hagrid :  Salut ", personnage["Prenom"], "! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse. ")
    c=demander_choix("Voulez-vous suivre Hagrid ? \n", ["Oui", "Non"])
    if c == 2:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")

def acheter_fourniture(personnage):
    dico_shop = load_fichier("../data/inventaire.json")
    print("Bienvenue sur le Chemin de Traverse !")

    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]

    while obligatoires != []:
        total_obligatoires = 5
        for objet in obligatoires:
            for cle in dico_shop:
                nom_obj = dico_shop[cle][0]
                prix_obj = dico_shop[cle][1]
                if nom_obj == objet:
                    total_obligatoires += prix_obj #ok

        print("Catalogue des objets disponibles :")
        i = 1
        for cle in dico_shop:
            print(str(i) + ". " + dico_shop[cle][0] + " - " + str(dico_shop[cle][1]) + " galions")
            i = i + 1 #ok

        print("\n")
        print("Vous avez", personnage["Argent"], "galions.")
        print("Objets obligatoires restant à acheter : \n")
        for obj in obligatoires:
            print(obj, "\n") #ok


        choix = demander_nombre("Entrez le numéro à acheter", 1, len(dico_shop))

        for cle in dico_shop:
            if str(choix) == cle:
                nom_obj_temp = dico_shop[cle][0]
                prix_obj_temp = dico_shop[cle][1]
                if personnage["Argent"]-prix_obj_temp <= total_obligatoires and nom_obj_temp not in obligatoires:
                    choix2 = demander_choix("Attention, cet achat risque de vous empêcher d’acheter tout le matériel obligatoire. Voulez-vous continuer ? \n", ["Oui", "Non"])
                    if choix2 == 1:
                        print("Vous n'aurez pas assez d'argent pour tout ! Fin du jeu.")
                        exit()
                else:
                    modifier_argent(personnage,-prix_obj_temp)
                    ajouter_objet(personnage,"Inventaire", nom_obj_temp)
                    print("Vous avez acheté :", nom_obj_temp, "(-" + str(prix_obj_temp) + " galions).")
                    if nom_obj_temp in obligatoires:
                        obligatoires.remove(nom_obj_temp)

    print("Tous les objets obligatoires ont été achetés !")
    print("\n")

    print("Il est temps de choisir votre animal de compagnie pour Poudlard !")
    print("Vous avez", personnage["Argent"], "galions.")

    animaux = {
        "Chouette": 20,
        "Chat": 15,
        "Rat": 10,
        "Crapaud": 5
    }

    print("Voici les animaux disponibles :")
    l = 1
    for n in animaux:
        print(str(l) + ". " + n + " - " + str(animaux[n]), "galions")
        l = l + 1

    choix_animal= demander_nombre("Quel animal voulez vous ? ", 1, len(animaux))

    l = 1
    for n in animaux:
        if l == choix_animal:
            prix_animal = animaux[n]
            if personnage["Argent"] < prix_animal:
                print("Vous n’avez pas assez d’argent ! Fin du jeu.")
                exit()
            modifier_argent(personnage, -prix_animal)
            ajouter_objet(personnage, "Inventaire", n)
            print("Vous avez choisi :", n, "(-" + str(prix_animal), "galions).")
        l = l + 1

    print("Tous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :")
    afficher_personnage(personnage)


def lancer_chapitre_1():
    introduction()
    perso=creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(perso)
    acheter_fourniture(perso)
    print("Fin du Chapitre 1 ! Votre aventure commence à Poudlard...")
    return perso

lancer_chapitre_1()
