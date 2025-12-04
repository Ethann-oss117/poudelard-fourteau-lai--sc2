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

def modifier_argent(joueur,montant) :
    joueur["argent"] = joueur["argent"] + montant


def ajouter_objet(joueur,cle,objet) :
    if cle =="sotileges" or cle == "inventaire" :
        joueur[cle].append(objet)

