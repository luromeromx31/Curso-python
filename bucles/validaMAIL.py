
email=False
mimail=input("introduce tu email: ")

def mailval(mimail):
    cont=0
    
    for i in mimail:
        if (i=="@" or i==".") :
            cont=cont+1

    if cont==2:
        return True
    else:
        return False
        

if mailval(mimail):
    print("El email es correcto")
else:
    print("El email no es correcto")