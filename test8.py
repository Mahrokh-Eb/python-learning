# lecture 61

class user():
    def __init__(self, userName):
        self.userName = "userName"
        self._password ="123"  # it is private, if you hit dot after me, it won't show up

        pass
    #making private function
    def password(self, gotPassWord):
        if self._password == gotPassWord:
            print('Come in ')
        else:
            print('Stop!')


me = user('golbanoo')
print(me.userName)
me.password(input('what is your password? '))
