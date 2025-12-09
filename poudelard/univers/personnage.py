
def initialiser_personnage(Nom, Prenom, attributs):
    argent = 100

    joueur = {
        "Nom": Nom,
        "Prenom": Prenom,
        "Argent": argent,
        "Inventaire": [],
        "Sortileges": [],
        "Attributs": {}
    }

    return joueur

def afficher_joueur(joueur):
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
    joueur["argent"] = joueur["argent"] + montant


def ajouter_objet(joueur,cle,objet) :
    if cle =="sotileges" or cle == "inventaire" :
        joueur[cle].append(objet)

