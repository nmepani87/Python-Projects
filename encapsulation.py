
# defining class
class protectedFunc:
    # data member of class to be encapsulated
    def ___init__(self):
        self._protectedAge = 13

#creating object from class
obj = protectedFunc()
# setting new age to be used for protectedAge
obj._protectedAge = 7
# printing result after new age plugged in
print(obj._protectedAge)

# defining class
class privateFunc:
    def __init__(self):
        self.__privateAge = 13

    def getPriv(self):
        print(self.__privateAge)

    def setPriv(self, private):
        self.__privateAge = private

#creating object from class
Private = privateFunc()
# accessing subfunction which prints current privateAge set
Private.getPriv()
# setting new age to be added along side to privateAge  
Private.setPriv(7)
# printing result after new age plugged in via subfunction again
Private.getPriv()
    
