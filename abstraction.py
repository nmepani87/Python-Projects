
# importing needed modules
from abc import ABC, abstractmethod

# defining class and passing in ABC's attributes
class legal(ABC): 
    # asking method to print statement with our parameter
    def question(self, age):
        print("Your ID says you are: ",age)
    # Decorator to define an abstract method
    @abstractmethod
    def drink(self, age):
        pass

# defining new class and passing in attritutes from class legal
class countryLegal(legal):
    # matching method to ABC's name and gettin to print statement
    def drink(self, age):
        print('You are {} and so can drink in this country where the legal minimum age is 18'.format(age))

# creating object
obj= countryLegal()
# setting age into question method
obj.question("19")
# setting age into drink method
obj.drink("19")
