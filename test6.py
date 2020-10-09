class flower():
    def __init__(self, kind, color, number):
        self.kind = kind
        self.color = color
        self.number = number

    def showFlowerInfo(self):
        return f'the folwer name is {self.kind} and the flower color is {self.color}'


rose = flower('rose', 'red', 6)
print(rose.kind)
print(rose.showFlowerInfo())