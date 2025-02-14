
concurrents = ["lou", "hamza", "assia", "sephora"]


def panne_moteur(concurrents):
    if len(concurrents) > 1:
        premier = concurrents.pop(0)
        concurrents.append(premier)


def passe_en_tete(concurrents):
   
    if len(concurrents) > 1:
        concurrents[0], concurrents[1] = concurrents[1], concurrents[0]


def sauve_honneur(concurrents):
   
    if len(concurrents) > 1:
        concurrents[-1], concurrents[-2] = concurrents[-2], concurrents[-1]


def tir_blaster(concurrents):

    if concurrents:
        concurrents.pop(0)


def retour_inattendu(concurrents, module):

    concurrents.append(module)





panne_moteur(concurrents)
print(concurrents)


sauve_honneur(concurrents)
print(concurrents)


tir_blaster(concurrents)
print(concurrents)


#ça ne fonctionne pas je ne sais pas pourquoi
retour_inattendu(concurrents)
print(concurrents)

