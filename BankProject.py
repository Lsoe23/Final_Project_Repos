#Creating Customer Class with 4 parameters
class Customer:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    stored_customer_data = {
        "customer_one" : {
            "First Name": "Lah",
            "Last Name": "Soe",
            "Username": "Lsoe",
            "Password": "1738@Lah"},
        "customer_two" : {
            "First Name": "Trans",
            "Last Name": "MathisSin",
            "Username": "TransMath",
            "Password": "CookieN!"
        }
    }

#SignUp
class SignUp:
    def __init__(self, new_user, password):
        pass

#Log In
def SignIn():
    pass

#Bank Class
class Bank:
    def __init__(self, initial_balance, deposit, total_deposits, total_withdrawals):
        pass


