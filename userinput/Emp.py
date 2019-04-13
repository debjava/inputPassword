'''
Created on Apr 11, 2019

@author: PIKU
'''

class Emp(object):

    def __init__(self, fName=None, lName=None):
        self._fName = fName
        self._lName = lName
        
    @property
    def fName(self):
        return self._fName
    
    @fName.setter
    def fName(self, firstName):
        self._fName = firstName

    @property
    def lName(self):
        return self._lName
    
    @lName.setter
    def lName(self,lastName):
        self._lName = lastName
        
    def showDetails(self):
        print("First Name : ",self.fName)
        print("Last Name : ",self.lName)
        
if __name__ == '__main__':
    emp = Emp()
    emp.fName= "Ram"
    emp.lName = "Ramesh"
    emp.showDetails()
        
        
        
