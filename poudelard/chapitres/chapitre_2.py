from poudelard.utils.input_utils import demander_choix


def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    print("Que répondez-vous ?")
    choix1 = demander_choix("1. Bien sûr, assieds-toi !\n2. Désolé, je préfère voyager seul.",["1","2"])
    if choix1==1 :
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
        joueur["Attributs"]["Loyaute"] += 1
    else :
        joueur["Attributs"]["Ambition"] += 1

    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    print("Que répondez-vous ?")
    choix2 = demander_choix("1. Oui, j’adore apprendre de nouvelles choses !\n2. Euh… non, je préfère les aventures aux bouquins.")