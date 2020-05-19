def generaPares(limite):
    num=1

    #milista=[]

    while num<limite:
        #milista.append(num*2)
        yield num*2
        num+=1
    
    #return milista

devuelvePares=generaPares(10)

for i in devuelvePares:
    print(i)

devuelvePares=generaPares(10)

print("bucle: while")
i=0
while i<3:
    print(next(devuelvePares))
    i+=1

print("bucle: for")
for i in range(0,3):
    print(next(devuelvePares))
