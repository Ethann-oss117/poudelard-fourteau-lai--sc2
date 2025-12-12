import random
from poudelard.univers.personnage import ajouter_objet
from poudelard.utils.input_utils import load_fichier


def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    sorts=load_fichier(chemin_fichier)
    sort_off=0
    sort_def=0
    sort_uti=0
    print("Tu commences tes cours de magie à Poudlard... \n")
    while (sort_off != 1) and (sort_def != 1) and (sort_uti != 3):
        sort_rdm=random.choice(sorts)

        if sort_rdm["type"] == "Utilitaire":
            sort_uti += 1
            ajouter_objet(joueur, "Sortileges",sort_rdm)
            print("Tu viens d'apprendre le sortilège : ", sort_rdm["nom"],"\n")
            sorts.remove(sort_rdm)
            input("Appuie sur Entrée pour continuer... \n")
        if sort_rdm["type"] == "Défensif":
            sort_def+=1
            ajouter_objet(joueur, "Sortileges", sort_rdm)
            print("Tu viens d'apprendre le sortilège : ", sort_rdm["nom"], "\n")
            sorts.remove(sort_rdm)
            input("Appuie sur Entrée pour continuer... \n")
        if sort_rdm["type"] == "Offensif":
            sort_off+=1
            ajouter_objet(joueur, "Sortileges",sort_rdm)
            print("Tu viens d'apprendre le sortilège : ", sort_rdm["nom"], "\n")
            sorts.remove(sort_rdm)
            input("Appuie sur Entrée pour continuer... \n")
    print("Tu as terminé ton apprentissage de base à Poudlard ! \n")
    print("Voici les sortilèges que tu maîtrises désormais : \n")

    for val in joueur["Sortileges"]:
        print("- ", val["nom"], " ("+str(val["type"])+")", " : ", val["description"])



apprendre_sorts({'Nom': 'Potter', 'Prenom': 'Harry', 'Argent': 100, 'Inventaire': [], 'Sortileges': [], 'Attributs': {'Courage': '8', 'Intelligence': '9', 'Loyaute': '10', 'Ambition': '10'}})

#{'Nom': 'Potter', 'Prenom': 'Harry', 'Argent': 100, 'Inventaire': [], 'Sortileges': [], 'Attributs': {'Courage': '8', 'Intelligence': '9', 'Loyaute': '10', 'Ambition': '10'}}