print("Introducir contraseña y vaidar dato")
val=0
pwd=input("Introduce contraseña: ")

for i in range(len(pwd)):
    if (pwd[i]==" " or len(pwd)<8):
        val=1
    

if val==1:
        print("La contraseña es incorrecta")
else:
        print("La contraseña es correcta")