import csv


def save_user_input (writer_csv) :

    titre = input("titre : ")
    prix= input("prix : ")
    stock = input("stock : ")
    writer_csv.writerow([titre,prix,stock])

with open("PythonAlgo/demo_csv/exo_demo/produit.csv",mode= 'a',newline="") as fichier :
    writer_csv = csv.writer(fichier,delimiter=";")


    for i in range (1):
        print(f'entrer numero {i}')
        save_user_input (writer_csv)
    



