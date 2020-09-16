# C A D E N A S

str = """lorem
ipsum 
dolor 
sit amet"""

print(str)

str = "Hola, ADSI, 2019"

# Extraer Caracter
print("Primer Caracter: " + str[0])

# Extraer Rango Caracteres
print("Rango de Caracteres(6 y 10): " + str[6:10])

# Longitud de Caracteres
print("Longitud de Caracteres: ", len(str))

# Quitar espacios al principio y al final
str = "     Hola, Mundo, Adsi, 2019  "
print("Con Espacios: " + str + " \nSin Espacios: " + str.strip())

str = "Hola, ADSI, 2019"

# Minuscula
print("Minuscula: " + str.lower())

# Mayuscula
print("Mayuscula: " + str.upper())

# Reemplazar Palabra
print("Reemplazar :" + str.replace('ADSI', 'SENA'))

# Separar Palabras
print("Separar Palabras: ")
print(str.split(','))

# Verificar si contiene una palabra
word = "2019" in str
print("Contiene la palabra 2019: ", word)

# Verificar si no contiene una palabra
word = "2019" not in str
print("No Contiene la palabra 2019: ", word)

year = 2020
text = "El presente año es el: {}"
print(text.format(year))


