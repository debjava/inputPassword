class UserEntity:

    def __init__(self, userName = None, password = None):
        self._userName = userName
        self._password = password

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self, uName):
        self._userName = uName

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = pwd


if __name__ == '__main__':
    user = UserEntity();
    user.userName = "DD"
    user.password = "abcd"
    print(user.password + "--------" + user.userName)

    user1 = UserEntity("Ram","Shyam")
    print(user1.userName+"----"+user1.password)
