import random
from poudelard.univers.personnage import ajouter_objet
from poudelard.utils.input_utils import load_fichier, demander_texte


#{'Nom': 'Potter', 'Prenom': 'Harry', 'Argent': 100, 'Inventaire': [], 'Sortileges': [], 'Attributs': {'Courage': '8', 'Intelligence': '9', 'Loyaute': '10', 'Ambition': '10'}}

def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    sorts=load_fichier(chemin_fichier)
    sort_off=0
    sort_def=0
    sort_uti=0
    print("Tu commences tes cours de magie à Poudlard... \n")
    while (sort_off < 1) or (sort_def < 1) or (sort_uti < 3):
        sort_rdm=random.choice(sorts)
        if sort_rdm["type"] == "Utilitaire" and sort_uti < 3:
            sort_uti += 1
            ajouter_objet(joueur, "Sortileges",sort_rdm)
            print("Tu viens d'apprendre le sortilège : ", sort_rdm["nom"],"\n")
            sorts.remove(sort_rdm)
            input("Appuie sur Entrée pour continuer... \n")
        elif sort_rdm["type"] == "Défensif" and sort_def < 1:
            sort_def+=1
            ajouter_objet(joueur, "Sortileges", sort_rdm)
            print("Tu viens d'apprendre le sortilège : ", sort_rdm["nom"], "\n")
            sorts.remove(sort_rdm)
            input("Appuie sur Entrée pour continuer... \n")
        elif sort_rdm["type"] == "Offensif" and sort_off < 1:
            sort_off+=1
            ajouter_objet(joueur, "Sortileges",sort_rdm)
            print("Tu viens d'apprendre le sortilège : ", sort_rdm["nom"], "\n")
            sorts.remove(sort_rdm)
            input("Appuie sur Entrée pour continuer... \n")
    print("Tu as terminé ton apprentissage de base à Poudlard ! \n")
    print("Voici les sortilèges que tu maîtrises désormais : \n")

    for val in joueur["Sortileges"]:
        print("- ", val["nom"], " ("+str(val["type"])+")", " : ", val["description"])



def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    lst_final=[]
    score_final=0
    question_maison=load_fichier(chemin_fichier)
    print("Bienvenue au quiz de magie de Poudlard ! \n")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison. \n")
    while len(lst_final) != 4:
        question=random.choice(question_maison)
        if question not in lst_final:
            lst_final.append(question)

    for i in range(4):
        print(str(i+1)+'. ', lst_final[i]["question"])
        rep=demander_texte("Votre Réponse ? ").strip().lower()
        question_encours=lst_final[i]["reponse"].split("/") #au cas ou deux reponses separées d'un / dans le json
        reponses_propres = []
        for elem in question_encours:
            elem=elem.strip()
            elem=elem.lower()
            reponses_propres.append(elem)
        if rep in reponses_propres:
            print("Bonne réponse ! +25 points pour ta maison. \n")
            score_final += 25
        else:
            print("Mauvaise réponse. La bonne réponse était : ", lst_final[i]["reponse"],"\n")

    print("Score obtenu : ", score_final)

def lancer_chapitre_3(personnage,maisons):
    pass

