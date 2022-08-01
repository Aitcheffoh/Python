miTupla= ("Juan",13,1,1995)
print(miTupla[2])

miLista =list(miTupla)
print(miLista[:])
miTupla2 = tuple(miLista)
print(miTupla2[:])


print("Juan" in miTupla)
print(miTupla.count(15))

nombre, dia, mes, agno= miTupla
print(nombre)
print(dia)
print(mes)
print(agno)