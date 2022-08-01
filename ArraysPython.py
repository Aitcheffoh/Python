miLista =["Maria","Pepe","Marta","Antonio"]

print(miLista[:])
print(miLista[0])
print(miLista[1])
print(miLista[2])
print(miLista[3])


print(miLista[-1])
print(miLista[-2])
print(miLista[-3])
print(miLista[-0])


print(miLista[0:3])
print(miLista[:3])
print(miLista[1:3])
print(miLista[2:])


miLista.append("Sandra")
print(miLista[:])
miLista.insert(2,"Camilo")
print(miLista[:])
miLista.extend(["Laura","Camila","Pipe"])
print(miLista[:])


print(miLista.index("Maria"))
print(miLista.index("Sandra"))
print(miLista.index("Camilo"))
print(miLista.index("Camila"))


print("Camila" in miLista)
print("Andres" in miLista)
print("Samanta" in miLista)
print("Marta" in miLista)


miLista.extend(["Fabian","Eduard","Brayan"])
print(miLista[:])
miLista.remove("Eduard")
print(miLista[:])
miLista.pop()
print(miLista[:])


lista2 =[5,34,54.6]
lista1 =[4,234,23,12.3]
lista3 = lista1 + lista2
print(lista3[:])