# L I S T A S

lista = ["python", "ruby", "c++", "java", "c#"]
print("Lista Inicial: ", lista)

# Mostrar valor de la Lista
print("Valor 1: ", lista[1])

# Mostrar rango de la Lista
print("Valores entre 2 y 4: ", lista[2:4]) 

# Todos los valores antes
print("Antes de c++: ", lista[:2])

# Todos los valores despues
print("Despues de c++:", lista[3:])

# Reemplazar valor
lista[2] = "PHP"
print("Nueva Lista: ", lista)

# Longitud de elementos
print("Longitud de la lista: ", len(lista))


# Recorrer Lista
print("Elementos de la Lista:")
for l in lista:
	print(l)

# Verificar valor en la lista

if "PHP" in lista:
	print("PHP si esta en la lista.")


# Agregar un valor al final
lista.append('Razor')
print(lista)

# Agregar en posicion determinada
lista.insert(2, "Flutter")
print(lista)

# Remover valor determinado
lista.remove("Razor")
print(lista)

# Remover del final
lista.pop() 
lista.pop(2)
print(lista)


# Eliminar elemento determinado
del lista[3]
print(lista)


# Copiar lista
lista2 = lista.copy()
print(lista2)

# Revertir lista
lista.reverse()
print(lista)

# Ordenar lista
lista.sort()
print(lista)

# Vaciar lista
lista.clear()
