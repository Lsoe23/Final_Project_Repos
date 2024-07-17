#Creating Customer Class with 4 parameters
class Customer:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    def existing_customer(self):
        store_customer_data = {"First Name": self.first_name,
                "Last Name": self.last_name,
                "Username": self.username,
                "Password": self.password}
        
        return store_customer_data
    
    def adding_customer(self):
        add_customer = {"First Name": self.first_name,
                "Last Name": self.last_name,
                "Username": self.username,
                "Password": self.password}
        #Wanting to append something here
        return add_customer



if __name__ == "__main__":
    var_name = Customer("Lah", "Soe", "Lsoe", 1738)
    print(Customer.existing_customer(var_name))

    



#Create a dictionary of existing customers 
#Add two existing customers


#Sign Up
