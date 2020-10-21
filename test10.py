# lecture 61

class user:
    def __init__(self, userName):
        self.userName = userName
        self._email = 'test@test.com'
        self._passWord = 'pass'
        self.__message = 'love you'

    def login(self, gotPassword):
        if self._passWord == gotPassword:
            print('let him in')
        else:
            print('wrong password')

insta = user('mahi')
print(insta.userName)
print(insta._email)
insta.login("pass")