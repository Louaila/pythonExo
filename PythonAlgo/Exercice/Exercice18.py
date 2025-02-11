
def compter_lettre_a(compteur : str) :
      return compteur.count("a")


resultat = compter_lettre_a('louaila')

print(resultat)



def compter_lettre_a(lettre: str):

    compteur_a = 0  

    for items in lettre:  
        if items == "a": 
            compteur_a += 1  

    return compteur_a