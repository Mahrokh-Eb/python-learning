class user:
    firstName = "Mahrokh"
    lastName = "Ebrahimi"
    age = 34
    def showFullName(self):
        pass
#print(type('python'))   # <class 'str'>
#numbers = list()
nemune = user()
print(nemune.firstName)
print(nemune.lastName)
print(nemune.age)

# making a new class:
class car():
    name = 'BMW'
    model = 2020
    manufacture = 'karkhune bmw sazi'
    def carIn(self):
        pass
carNemune = car()
print(carNemune.name)