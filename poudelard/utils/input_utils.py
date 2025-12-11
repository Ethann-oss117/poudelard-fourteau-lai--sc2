import json

def demander_texte(message):
    txt=str(input(message))
    while txt is None or txt == "":
        txt=str(input(message))
    txt=txt.strip()
    return txt

def demander_nombre(message, min_val=None, max_val=None):
    def est_chiffre(n):
        if 0 <= ord(n) - ord('0') <= 9:
            return True
        else:
            return False
    def est_negatif(n):
        if n[0]=='-':
            return True
        else:
            return False
    if min_val != None or max_val != None:
        nb=input(message+" ("+str(min_val)+"-"+str(max_val)+") ")
        nb = nb.strip()
        while nb !=None:
            while nb!="":
                lng_nb=len(nb)
                if est_negatif(nb)==True:
                    lng_nb-=1
                cpt=0
                for val in nb:
                    if est_chiffre(val)==True:
                        cpt=cpt+1
                if cpt==lng_nb:
                    return nb
                else:
                    print("Veuillez saisir un Nombre : ")
                    nb = input(message + " (" + str(min_val) + "-" + str(max_val) + ") ")
            print("Veuillez saisir un Nombre : ")
            nb = input(message + " (" + str(min_val) + "-" + str(max_val) + ") ")
    else:
        nb = input(message)
        nb = nb.strip()
        while nb != None:
            while nb != "":
                lng_nb = len(nb)
                if est_negatif(nb) == True:
                    lng_nb -= 1
                cpt = 0
                for val in nb:
                    if est_chiffre(val) == True:
                        cpt = cpt + 1
                if cpt == lng_nb:
                    return nb
                else:
                    print("Veuillez saisir un Nombre : ")
                    nb = input(message)
            print("Veuillez saisir un Nombre : ")
            nb = input(message)


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
