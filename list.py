#Aqui vamos a trabajar con listas

#Lista de frutas
frutas=["Manzanas","Peras","Melon"]
print(frutas)
numeros=[10,20,30,40]
print(numeros)

#acceder a un elemento de la lista
print(frutas[0])
print(frutas[1])
print(frutas[2])
#print(frutas[3])

#Agregar elementos
frutas.append("Banana") #Agrega al final de la lista
print(frutas)

frutas.insert(1,"Naranja") #Agrega en la posicion que le indiquemos
print(frutas)

#Modificar elementos
frutas[0]="Fresas" #Modifica el elemento en la posicion indicada
print(frutas)

#eliminar elementos
frutas.remove("Melon") #Elimina el elemento indicado    
print(frutas)
frutas.pop(2) #Elimina el elemento en la posicion indicada
print(frutas)