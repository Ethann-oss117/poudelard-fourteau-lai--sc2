import json

def demander_texte(message):
    txt=str(input(message))
    while txt is None or txt == "":
        txt=str(input(message))
    txt=txt.strip() #On fait strip pour enlever les espaces en excès qui vont rendre l'affichage désordonné
    return txt

def demander_nombre(message, min_val=None, max_val=None):
    nb=int(input(message+" ("+str(min_val)+"-"+str(max_val)+") ")) #pour afficher l'intervalle des nombres à demander
    while nb is None or nb < min_val or nb > max_val or nb == "": #Saisie sécurisée
        print("Veuillez entre un nombre entre "+" ("+str(min_val)+"-"+str(max_val)+") ")
        nb = int(input(message + " (" + str(min_val) + "-" + str(max_val) + ") "))
    return nb

def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(i+1,". ", options[i], "\n")
    choix=demander_nombre("Votre choix ?", 1, len(options))
    return choix


def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r") as fichier:
        data = json.load(fichier)
    return data
