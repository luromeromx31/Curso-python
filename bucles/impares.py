print("Programa que imprime numeros impares.")

max=int(input("Introduce el valor maximo a calcular: "))

#def impares(max):
for i in range(max):
    if i%2!=0:
        print(i, end=" ")

print("")