
maisons = {
    "Gryffondor": 0,
    "Serpentard": 0,
    "Poufsouffle": 0,
    "Serdaigle": 0
}

def actualiser_point_maison(maisons,nom_maison,points) :
    if nom_maison=="Gryffondor" or nom_maison=="Serpentard" or nom_maison=="Poufsouffle" or nom_maison=="Serdaigle" :
        ecart=points
        maisons[nom_maison] += points
        if points < 0:
            print("La maison",nom_maison,"a perdu",ecart,"et a maintenant",points,"points")
        elif points > 0 :
            print("La maison",nom_maison,"a gagné",ecart,"et a maintenant",points,"points")
        else :
            print("aucun points n'a été attribué")
    else :
        print("La maison est introuvable")


def afficher_maison_gagnante(maisons):
    maxi=0
    gagnante=[]
    for cle in maisons:
        if maisons[cle] >= maxi :
            maxi=maisons[cle]
    for cle in maisons :
        if maisons[cle] == maxi :
            gagnante.append(cle)
    if len(gagnante)==1 :
        print("la maison gagnante est",gagnante)
    else :
        print("les maisons gagnantes sont",gagnante)



questions = [
 (
 "Tu vois un ami en danger. Que fais-tu ?",
 ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherchede l’aide", "Je reste calme et j’observe"],
 ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
 ),
 (
 "Quel trait te décrit le mieux ?",
 ["Courageux et loyal", "Rusé et ambitieux", "Patient ettravailleur", "Intelligent et curieux"],
 ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
 ),
 (
 "Face à un défi difficile, tu...",
 ["Fonces sans hésiter", "Cherches la meilleure stratégie",
"Comptes sur tes amis", "Analyses le problème"],
 ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
 )
]

def repartition_des_maisons(joueur,question) :
    points = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    attributs = joueur["Attributs"]
    points["Gryffondor"] += attributs["courage"] * 2
    points["Serdaigle"] += attributs["intelligence"] * 2
    points["Poufsouffle"] += attributs["loyauté"] * 2
    points["Serpentard"] += attributs["ambition"] * 2


