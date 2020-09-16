#  D I C C I O N A R I O S

pk = {
	"name": "Pikachu",
	"type": "Electric",
	"weak": "Ground"
}

print(pk)

# Mostrar atributo especifico
print("El tipo es: ", pk["type"])

# Obtener valor especifico
print("La Debilidad es: ", pk.get("weak"))

# Mostrar todos los valores
for v in pk:
	print(v, ": ", pk[v])
