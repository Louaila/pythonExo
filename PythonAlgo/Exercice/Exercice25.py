
def calcul (nb1,nb2) :
 
    addition = nb1 + nb2
    difference =  nb1 - nb2
    quotient = nb1 / nb2
    produit = nb1 * nb2


    return(addition,difference,quotient,produit )

combien_nombre = int(input('donne moi le premier nombre : '))
combien_nombre2 = int(input('donne moi 2 nombre : '))



resultat1, resultat2,resultat3,resultat4 = calcul (combien_nombre,combien_nombre2)
print(f'la somme est {resultat1} , la difference est {resultat2}, le quotient est {resultat3} et le produit est {resultat4}')



resultat = calcul(combien_nombre,combien_nombre)
print (resultat)