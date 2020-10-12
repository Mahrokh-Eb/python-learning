# lecture 60
from test5 import car
class user():
    userName = 'mahi'
    def __init__(self, gotUsename, gotUserfamily):
        self.userName = gotUsename
        self.userFamily = gotUserfamily
    def buyCourse(self):
        return f"{self.userName} can buy  all courses"



perid = car('perid', 2, 'redveie')
print(perid.showCarInfo())

mahi = user('Mahrokh ', 'Ebrahimi')
print(mahi.userName)
print(mahi.userFamily)
print(mahi.buyCourse())