
# Creating class of communicator(parent class)
class communicator:
    # Defining the attributes of clothing
    frequency = ""
    manufacturer = ""
    communication_type = ""
    
# Creating class of Shorts and plugging in communicator(parent) to
# inherit its attributes too
class cellphone(communicator):
    #Defining the attributes to add to inherited ones
    form_factor = "Flip"
    os = "Android"

# Creating class of Shorts and plugging in communicator(parent) to
# inherit its attributes too
class nic(communicator):
    #Defining the attributes to add to inherited ones
    typeOf = "Wireless"
    speed = "150Mbps"


