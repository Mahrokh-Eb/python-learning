class car():
    def __init__(self, name, ndoor, color):
        self.name = name
        self.ndoor = ndoor
        self.color =  color

    def showCarInfo(self):
        return f'car name is {self.name} car color is {self.color}'


benz = car('cls', 2, 'pink')
print(benz.showCarInfo())