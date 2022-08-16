
# Creating class of communicator(parent class)
class communicator:
    # Defining the attributes of clothing
    frequency = ""
    manufacturer = ""
    communication_type = ""
    clearance_level = 3
    # Creating method for parent class
    def getDetails(self):
        # Asking user to input a couple of details which will be used in if statements and print results based on that outcome
        employeeName = input("Enter your full name: ")
        employeeLevel = int(input("Enter your clearance level: "))
        if (employeeLevel<self.clearance_level):
            return "Hello {}! I hope you\'re enjoying the day so far".format(employeeName)
        else:
            print("{} unfortunately you are not cleared to use this part of the system.".format(employeeName))
            print('Goodbye')
            quit()  
    
# Creating class of Shorts and plugging in communicator(parent) to
# inherit its attributes too
class cellphone(communicator):
    #Defining the attributes to add to inherited ones
    form_factor = "Flip"
    os = "Android"
    # Asking user to input a couple of details which will be used in if statements and print results based on that outcome
    def getDetails(self):
        employeeName = input("Enter your full name: ")
        employeeLevel = int(input("Enter your clearance level: "))
        brand = input("Enter manufacturer of product you want to order: ")
        if (employeeLevel<self.clearance_level and (brand == "Google" or brand == "Samsung")):
            print("Hello {}! I hope you\'re enjoying the day so far".format(employeeName))
            return "We can order from the chosen brand!"
        elif (brand != "Google" or brand != "Samsung"):
            return "Unfortunately we don't have an account to order from that company."
        else:
            print("{} unfortunately you are not cleared to use this part of the system.".format(employeeName))
            print('Goodbye')
            quit()
                        
   
# Creating class of Shorts and plugging in communicator(parent) to
# inherit its attributes too
class nic(communicator):
    #Defining the attributes to add to inherited ones
    typeOf = "Wireless"
    speedMbps = 150
    # Asking user to input a couple of details which will be used in if statements and print results based on that outcome
    def getDetails(self):
        employeeName = input("Enter your full name: ")
        employeeLevel = int(input("Enter your clearance level: "))
        fast = int(input("Please enter the minimum speed(in Mbps) you will be needing the card to handle: "))
        if (employeeLevel<self.clearance_level and fast > self.speedMbps):
            print("Hello {}! I hope you\'re enjoying the day so far".format(employeeName))
            return "We can certainly get a hold of NIC that can handle that requirement"
        elif (fast < self.speedMbps):
            return "Unfortunately those speeds are a bit primative, you may have to go a reseller for that"
        else:
            print("{} unfortunately you are not cleared to use this part of the system.".format(employeeName))
            print('Goodbye')
            quit()
        
    

if __name__ == "__main__":
    #Invoking the method within cellphone/nic class and also from into parent class too
    Communicator = communicator()
    print(Communicator.getDetails())
    Cellphone = cellphone()
    print(Cellphone.getDetails())
    NIC = nic()
    print(NIC.getDetails())


