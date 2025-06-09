from fruit import fruit

class Orange(fruit):
	def __init__(self, name, color):
		super().__init__(name, color)

	def peel(self):
		return f"{self.name} is being peeled."

	def crush(self):
		return f"{self.name} is now pulped."