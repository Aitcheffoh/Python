miDiccionario ={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)
miDiccionario["Italia"]="Roma"
print(miDiccionario)
del miDiccionario["Reino Unido"]
print(miDiccionario)
miDiccionario ={"Alemania":"Berlin","Jordan":23,"Mosqueteros":3,}
print(miDiccionario)
miTupla= ("España","Francia","Reino Unido","Alemania")
miDiccionario ={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Berlin"}
print(miDiccionario["Francia"])