# O B J E T O S (Clases, Atributos, Métodos)

class Product:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def result(self):
		print('El Producto es: ', self.num1*self.num2)

prod = Product(74, 16)
#prod.num2 = 0
prod.result()
