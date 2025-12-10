
def initialiser_personnage(Nom, Prenom, attributs):
    argent = 100

    joueur = {
        "Nom": Nom,
        "Prenom": Prenom,
        "Argent": argent,
        "Inventaire": [],
        "Sortileges": [],
        "Attributs": attributs
    }

    return joueur

def afficher_personnage(joueur):
    print("Profil du personnage :")
    print("Nom :", joueur["Nom"])
    print("Prenom :", joueur["Prenom"])
    print("Argent :", joueur["Argent"])
    print("Inventaire :", joueur["Inventaire"])
    print("Sortileges :", joueur["Sortileges"])
    print("Attributs :")
    for cle,val in joueur["Attributs"].items():
        print(" - ",cle," : ",val)

def modifier_argent(joueur,montant) :
    joueur["Argent"] = joueur["Argent"] + montant


def ajouter_objet(joueur,cle,objet) :
    if cle =="Sortileges" or cle == "Inventaire" :
        joueur[cle].append(objet)

