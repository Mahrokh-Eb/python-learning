
#class 59, sare --init--
class user:
    firstName = "Mahrokh"
    lastName = "Ebrahimi"
    age = "34"
    def showFullName(self):
        return self.firstName + '  ' + self.lastName
    def showFullInfo(self):
        return self.firstName + ' ' + self.lastName + ' ' + self.age + ' sale'
        pass
#print(type('python'))   # <class 'str'>
#numbers = list()
nemune = user()
print(nemune.firstName)
print(nemune.lastName)
print(nemune.age)
print(nemune.showFullName())
print(nemune.showFullInfo())

# making a new class:
class car():
    name = 'BMW'
    model = 2020
    manufacture = 'karkhune bmw sazi'
    def carIn(self):
        pass
carNemune = car()
print(carNemune.name)

print('done')