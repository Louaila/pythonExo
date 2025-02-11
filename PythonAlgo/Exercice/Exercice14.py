#structure iterative for
# == ' operateur de comparaison
# = ' operateur de designation ' 

for items in range (1,101):
    if items % 3 == 0 and items % 5 == 0:
        print("frizzBuzz")
    elif items % 5 == 0:
        print ("Buzz")
    elif  items % 3 == 0 :
       print ("Frizz")
    else :
        print(items)   

