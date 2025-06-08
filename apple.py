from fruit import Fruit

class Apple(Fruit):
    def __init__(self, name, color):
        super().__init__(name, color)

    def slice(self):
        return f"{self.name} is being sliced."