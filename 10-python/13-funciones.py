# F U N C I O N E S

def showNames(firstn, lastn = "Simpson"):
	print(firstn +" "+ lastn)

showNames("Jeremias", "Springfield")
showNames("Homero")


def showPower(*pks):
	print("El pokemon mas poderoso es: " + pks[1])
showPower("Pikachu", "Charmander", "Bulbasour")
