
maisons = {
    "Gryffondor": 0,
    "Serpentard": 0,
    "Poufsouffle": 0,
    "Serdaigle": 0
}

def actualiser_point_maison(maisons,nom_maison,points) :
    if nom_maison=="Gryffondor" or nom_maison=="Serpentard" or nom_maison=="Poufsouffle" or nom_maison=="Serdaigle" :
        ecart=points   #je sauvegarde les nombre de point attribue pour le restitué dans le print
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
    gagnante=[]   #on crée une liste qui va prendre la ou les maisons gagnantes
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

