adresses = []

def voir_adresse(adresses):
    if not adresses:
        print("Aucune adresse enregistrée.")
    else:
    
        for i in adresses:
            print(f"AD n° {adresses.index(i)}")
            for cle, valeur in i.items():
                print(f"{cle} : {valeur}")


def ajouter_adresse ():
    number = int(input(f' ajouter le numero  : '))
    complement = input(f' ajouter un complement adresse : ' )
    name =  input(f' ajouter un nom de rue  : ')
    ville = input(f' ajouter la ville : ')
    code_postal = int(input(f' ajouter le code postal  : '))
    
    dico_adresse = { 
        "numero" : number,
        "complement" : complement,
        "intitulé_voie" : name,
        "commune" : ville,
        "code_postal" : code_postal
    }

    return dico_adresse
    
adresse_a_ajouter = ajouter_adresse()
adresses.append(adresse_a_ajouter)
voir_adresse(adresses)








