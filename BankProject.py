#Creating Customer Class with 4 parameters
class Customer:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    def existing_customer(self):
        existing_customer_data = {"First Name": self.first_name,
                "Last Name": self.last_name,
                "Username": self.username,
                "Password": self.password}
        
        return existing_customer_data

new_customer = Customer("Lah", "Soe", "Lsoe", 1738)
print(new_customer.existing_customer())

    



#Create a dictionary of existing customers 
#Add two existing customers


#Sign Up
