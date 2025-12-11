from random import *

from poudelard.chapitres.chapitre_1 import creer_personnage
from poudelard.univers.personnage import ajouter_objet
from poudelard.utils.input_utils import load_fichier


def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    sorts=load_fichier(chemin_fichier)
    sort_off=0
    sort_def=0
    sort_uti=0
    print("Tu commences tes cours de magie à Poudlard... \n")
    while (sort_off != 1) and (sort_def != 1) and (sort_uti != 3):
        num_alea=randint(0,23)
        if sorts[num_alea]["type"] == "Utilitaire":
            sort_uti += 1
            ajouter_objet(joueur, "Sortileges",sorts[num_alea]["nom"])
            print("Tu viens d'apprendre le sortilège : ", sorts[num_alea]["nom"],"\n")
            input("Appuie sur Entrée pour continuer... \n")
        elif sorts[num_alea]["type"] == "Défensif":
            sort_def+=1
            ajouter_objet(joueur, "Sortileges", sorts[num_alea]["nom"])
            print("Tu viens d'apprendre le sortilège : ", sorts[num_alea]["nom"], "\n")
            input("Appuie sur Entrée pour continuer... \n")
        elif sorts[num_alea]["type"] == "Offensif":
            sort_off+=1
            ajouter_objet(joueur, "Sortileges", sorts[num_alea]["nom"])
            print("Tu viens d'apprendre le sortilège : ", sorts[num_alea]["nom"], "\n")
            input("Appuie sur Entrée pour continuer... \n")
    print("Tu as terminé ton apprentissage de base à Poudlard ! \n")
    print("Voici les sortilèges que tu maîtrises désormais : \n")

    for i in range(len(joueur["Sortileges"])):
        for val in sorts:
            if val["nom"]==joueur["Sortileges"][i]:
                print("- ", joueur["Sortileges"][i], " ("+str(val["type"])+")", " : ", val["description"])
apprendre_sorts(creer_personnage())

