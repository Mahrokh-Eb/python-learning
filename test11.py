#lecture 62
class user():
    def __init__(self, gotName, gotFamily, gotAge):
        self.name = gotName
        self.family = gotFamily
        self.age = gotAge
    def showFullName(self ):
        return f"{self.name} {self.family} {self.age}"
    def userAgeStatus(self):
        return f'{self.name} " "' if self.age>40 else f'{self.name} "not adult"'

me = user('mahi', 'golkhand', 32)
print(me.showFullName())
she = user('sara', 'golbahani', 82)
print(she.showFullName())
print(me.userAgeStatus())