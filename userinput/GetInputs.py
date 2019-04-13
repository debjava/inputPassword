import getpass


class GetInputs:
    userName = None
    password = None

    def __init__(self):
        print("Constructor invoked ...")

    def getUserName(self):
        while True:
            userName = input("Enter name : ")
            if not userName:
                continue
            else:
                print("Entered User Name : [", userName, "]")
                self.userName = userName
                break

    def getpassword(self):
        while True:
            password = getpass.getpass()
            if not password:
                continue
            else:
                print("Actual Password : ", password)
                self.password = password
                break

    def test1(self):
        try:
            p = getpass.getpass(prompt="Enter Password:")
        except Exception as error:
            print('ERROR', error)
        else:
            print('Password entered:', p)


if __name__ == '__main__':
    testInput = GetInputs()
    testInput.getUserName()
    testInput.getpassword()
