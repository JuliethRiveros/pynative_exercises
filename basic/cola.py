class Cola:

	def __init__(self):
		self.lista = []


	def entrar(self, elemento):
		indice = len(self.lista)
		self.lista.insert(indice, elemento)

	def salir(self):
		self.lista.pop(0)


p = Cola()
p.entrar(1)
p.entrar(2)
p.salir()
print(p.lista)


