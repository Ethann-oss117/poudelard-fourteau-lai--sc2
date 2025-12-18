from poudelard.chapitres.chapitre_1 import creer_personnage
from poudelard.univers.maison import repartition_des_maisons
from poudelard.univers.personnage import initialiser_personnage, afficher_personnage
from poudelard.utils.input_utils import demander_choix, load_fichier


def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...")
    print()
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    choix1 = demander_choix("Que répondez-vous ?",["1Bien sûr, assieds-toi !","Désolé, je préfère voyager seul."])
    if choix1==1 :
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
        joueur["Attributs"]["Loyaute"] += 1
    else :
        joueur["Attributs"]["Ambition"] += 1

    print()
    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    choix2 = demander_choix("Que répondez-vous ?",["Oui, j’adore apprendre de nouvelles choses !","Euh… non, je préfère les aventures aux bouquins."])
    if choix2==1 :
        joueur["Attributs"]["Intelligence"] += 1
    else :
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour !")
        joueur["Attributs"]["Intelligence"] += 1

    print()
    print("Puis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choix3 = demander_choix("Comment réagissez-vous ?",["Je lui serre la main poliment.","Je l’ignore complètement.","Je lui réponds avec arrogance."])
    if choix3==1 :
        joueur["Attributs"]["Ambition"] += 1
    elif choix3==2 :
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
        joueur["Attributs"]["Loyaute"] += 1
    else :
        joueur["Attributs"]["Courage"] += 1

    print()
    print("Le train continue sa route. Le château de Poudlard se profile àl’horizon...")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")
    print()
    print("Tes attributs mis à jour :",joueur["Attributs"])

def mot_de_bienvenue() :
    print("Bienvenue à Poudlard, jeune sorcier")
    input("Appuyer sur entrée pour continuer")
    print("Les portes du château s’ouvrent devant toi, révélant des couloirs mystérieux, des sortilèges anciens et des rencontres inoubliables.")
    input()
    print("Ton aventure ne fait que commencer .")
    input()
    print("Je te souhaite bonne chance, et surtout...")
    input()
    print("Que la magie soit avec toi.")

questions = [
 (
 "Tu vois un ami en danger. Que fais-tu ?",
 ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
 ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
 ),
 (
 "Quel trait te décrit le mieux ?",
 ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
 ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
 ),
 (
 "Face à un défi difficile, tu...",
 ["Fonces sans hésiter", "Cherches la meilleure stratégie",
"Comptes sur tes amis", "Analyses le problème"],
 ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
 )
]

def ceremonie_repartition(joueur) :
    maison = repartition_des_maisons(joueur,questions)
    print()
    joueur["Maison"]= maison
    print("Le Choixpeau s’exclame :",maison,"!!!")
    print("Tu rejoins les élèves de",maison,"sous les acclamations !")


def installation_salle_commune(joueur) :
    salle = load_fichier("../data/maisons.json")
    maison = joueur["Maison"]
    print("Vous suivez les préfets à travers les couloirs du château...\n")
    print(salle[maison]["emoji"], salle[maison]["description"], "\n")
    print(salle[maison]["message_installation"], "\n")
    print("Les couleurs de votre maison sont :", salle[maison]["couleurs"][0], "et",salle[maison]["couleurs"][1])

def lancer_chapitre_2(joueur) :
    rencontrer_amis(joueur)
    mot_de_bienvenue()
    ceremonie_repartition(joueur)
    installation_salle_commune(joueur)
    afficher_personnage(joueur)
    print("Le chapitre 2 est terminé")
