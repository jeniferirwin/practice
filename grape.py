from fruit import Fruit

class Grape(Fruit):
    def __init__(self, name, color):
        super().__init__(name, color)

    def peel(self):
        return f"{self.name} is being peeled."

    def microwave(self):
        return f"{self.name} has turned into plasma."