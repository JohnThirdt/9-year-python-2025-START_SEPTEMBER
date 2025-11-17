class Fruit:

    def __init__(self, weight, parameter):
        self.weight = weight
        self.parameter = parameter
        self.id = 0

    def __len__(self):
        return len(str(self.parameter))

    def __str__(self):
        return f"Fruit's weight is {self.weight} and parameter is equal to {self.parameter}"




a = Fruit(weight=125, parameter=15)

print(str(a), len(a))