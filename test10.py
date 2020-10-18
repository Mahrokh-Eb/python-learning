# lecture 61

class user:
    def __init__(self, userName):
        self.userName = userName
        self._email = 'test@test.com'

insta = user('mahi')
print(insta.userName)
print(insta._email)