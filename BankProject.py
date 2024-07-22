#Creating Customer Class with 4 parameters
class Customer:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    #instead of accessing the memory of the object, return the properties within
    def __repr__(self):
        return f"Customer(first_name={self.first_name}, last_name={self.last_name}, username={self.username}, password={self.password})"
#We're storing existing customer data here and uploading new customer data here
existing_customer = [
    Customer(first_name = "Lah", last_name = "Soe", username = "Lsoe", password = "L@hsoe21"),
    Customer(first_name = "Anita", last_name = "Kiss", username = "AnitaKiss", password = "Kis#la11")
    ]
    
    #Two existing customers
#SignUp
class SignUp:

    def password():
        special_char = ["[", "]", "!", "@", "#", "$", "%", "-", "&", "*", "=", "_"]

        while True:

            passWord = input("Enter Password: ")
            
            if len(passWord) < 6 or len(passWord) > 12:
                print("Error: password must be between 6 and 12 character")
                continue
            
            #function any() return boolean
            #if not true, then we continue

            if not any(char.islower() for char in passWord):
                print("Error: Password must contain at least one lower case letter.")
                continue
            
            #the for loop will iterate until the function any is true
            if not any(char.isupper() for char in passWord):
                print("Error: Password must contain at least one upper case letter.")
                continue
            
            if not any(char.isdigit() for char in passWord):
                print("Error: Password must contain at least one digit")
                continue
            
            if not any(char in special_char for char in passWord):
                print("Error: password must contain at least one special character: [", "]", "!", "@", "#", "$", "%", "-", "&", "*", "=", "_")
                continue
            
            while True:
                confirmed_password = input("Re-enter Password: ")
                if confirmed_password == passWord:
                    print("Password confirmed.")
                    break
                else:
                    print("Passwords do not match. Please try again.")
                    continue

            break
    #To access the password function, I had to change which function comes first
    
    def new_users():

        firstName = input("Enter First Name: ").title().strip()
        lastName = input("Enter Last Name: ").title().strip()

        userName = input("Enter Username: ").strip()
        passWord = SignUp.password()
            
        new_customer = Customer(first_name = firstName, last_name = lastName, username = userName, password = passWord)
        existing_customer.append(new_customer)

SignUp.new_users()
print(existing_customer)


#Log In
def SignIn():
    #Use while loop to allow user 5 attemps
    attempts = 0
    while (attempts < 5):
        Recent_Username = input("Enter Username: ")
        Recent_Password = input("Enter Password: ")

        for customer in existing_customer:
            if customer.username == Recent_Username and customer.password == Recent_Password:
                return "Access Granted"
            break
        
        attempts += 1
        print(f"{5 - attempts}")
    
    return("Multiple Incorrect Attempt!\nDevice Locked")



#Bank Class
class Bank:
    def __init__(self, initial_balance = 1000, deposit = 0, total_deposits = 0, total_withdrawals = 0):
        self.initial_balance = initial_balance
        self.deposit = deposit
        self.total_deposits = total_deposits
        self.total_withdrawals = total_withdrawals

    def transaction():
        print("[1]Show Balance\n[2]Deposit\n[3]Withdrawal\n[4]Print Statement\n[5]Email Statement\n[6]Quit")
        pass


