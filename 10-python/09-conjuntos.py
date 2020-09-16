# C O N J U N T O S

oss = {"Windows", "Linux", "macOSX"}
print(oss)

# Imprimir valores
for os in oss:
	print(os)

# Adicionar un valor
oss.add("iOS")
print(oss)

# Actualizar valores del conjunto
oss.update(["Android", "Windows Phone"])
print(oss)

# Quitar un valor
oss.discard("Windows Phone")
print(oss)


