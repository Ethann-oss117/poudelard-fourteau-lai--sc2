import json

def demander_texte(message):
    txt=str(input(message))
    while txt is None or txt == "":
        txt=str(input(message))
    txt=txt.strip()
    return txt

def demander_nombre(message, min_val=None, max_val=None):
    nb=input(message+" ("+str(min_val)+"-"+str(max_val)+") ")
    while nb is None or int(nb) < min_val or int(nb) > max_val or nb == "":
        print("Veuillez entre un nombre entre "+" ("+str(min_val)+"-"+str(max_val)+") :")
        nb = input(message + " (" + str(min_val) + "-" + str(max_val) + ") :")
    nb=int(nb)
    return nb

def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(i+1,". ", options[i], "\n")
    choix=demander_nombre("Votre choix ?", 1, len(options))
    return choix

def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding='utf-8') as fichier:
        data = json.load(fichier)
    return data
