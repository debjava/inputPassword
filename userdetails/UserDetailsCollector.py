'''
Created on Apr 11, 2019

@author: PIKU
'''
import getpass

from userdetails.UserEntity import UserEntity


class UserDetailsCollector(object):

    def __init__(self):
        print("Default constructor ...")
        
    def collectUserName(self):
        while True:
            userName = input("Enter user name : ");
            userName = userName.strip()
            if not userName:
                continue
            else:
                print("Entered User Name : ", userName)
                break
        return userName
    
    def collectPassword(self):
        while True:
            password = getpass.getpass(prompt="Enter password : ", stream=None)
            if not password:
                continue
            else:
                print("You have entered password as : ", password)
                break
            
        return password
    
    def collectUserDetails(self):
        userName = self.collectUserName()
        password = self.collectPassword()
        userEntity = UserEntity();
        userEntity.password = password
        userEntity.userName = userName
        print("User Entity : ", userEntity)
        print("User Entity as toString() : ", str(userEntity.__dict__))


if __name__ == '__main__':
    user = UserDetailsCollector()
    user.collectUserDetails()
