#Creating Customer Class with 4 parameters
class Customer:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    #Instead of printing out object the address of the function, this functin provide a more descriptive inside
    def __repr__(self):
        return f"Customer(first_name='{self.first_name}, last_name='{self.last_name}', username='{self.username}, password='{self.password}')"

#We're storing existing customer data here and uploading new customer data here
existing_customer = [
    Customer(first_name = "Lah", last_name = "Soe", username = "Lsoe", password = "1738@lsoe"),
    Customer(first_name = "Anita", last_name = "Kiss", username = "AnitaKiss", password = "Crispybacon")
    ]
    
    #Two existing customers
#SignUp
class SignUp:
    def new_users():
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        password = input("Enter Password: ")

        return f"Full Name:{firstName} {lastName}"
        pass

    def password():
        newPassword = input("Enter New Password: ")
        reEnterPassword = input("Re-enter Password: ")

        pass


#Log In
def SignIn():
    #Use while loop to allow user 5 attemps
    Recent_Username = input("Enter Username: ")
    Recent_Password = input("Enter Password: ")

    pass

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


