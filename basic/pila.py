class Pila:
	def __init__(self):
		self.lista = []

	def entrar(self,elemento):
		indice = len(self.lista)
		self.lista.insert(indice, elemento)

	def salir(self):
		indice = len(self,lista)
		self.lista.pop(indice)





p = Pila()
p.entrar(1)
p.entrar(2)
print(p.lista)

q = Pila()
q.entrar("julieth")
q.entrar("riveros")
print(q.lista)