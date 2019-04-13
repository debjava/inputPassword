class GetterSetter:

    def __int__(self):
        self._x = None #_x is the private variable

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    def show(self):
        print("Value of x :::", self.x)

if __name__ == '__main__':
    getterSetter = GetterSetter();
    getterSetter.x = 20;
    getterSetter.show()
