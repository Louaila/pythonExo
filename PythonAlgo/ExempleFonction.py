def hello_world():
    print ("hello world")
hello_world() 




def hello_world():
    return "hello world"
ma_variable = hello_world ()
print(f' valeur de ma variable {ma_variable}')





def dire_bonjour(nom,prenom) :
    print(f"bonjour {nom} {prenom}")

dire_bonjour('louaila','touama')



def say_hello (name ='lou') :
    print(f"hello {name}")

say_hello('touama')

# on n'est pas obligé de mettre des paramettre 
say_hello()