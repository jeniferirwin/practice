from fruit import Fruit

class Banana(Fruit):
    def __init__(self, name, color):
        super().__init__(name, color)

    def peel(self):
        return f"{self.name} is being peeled."

    def ripen(self):
        return f"{self.name} is being ripened."
    