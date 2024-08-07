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
                    return confirmed_password
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
            
        #adding the new customer
        new_customer = Customer(first_name = firstName, last_name = lastName, username = userName, password = passWord)
        existing_customer.append(new_customer)


#Log In
def SignIn():
    #Use while loop to allow user 5 attempst
    #Making sure the users enter their credential correctly.
    attempts = 0
    while (attempts < 5):
        Recent_Username = input("Enter Username: ")
        Recent_Password = input("Enter Password: ")

        for customer in existing_customer:
            if customer.username == Recent_Username and customer.password == Recent_Password:
                print("Access Granted")
                return True
        
        attempts += 1
        print(f"Chances left: {5 - attempts}")
    
    print("Multiple Incorrect Attempt! Apps Locked")
    return False




#Bank Class
class Bank:
    def __init__(self, initial_balance=1000, deposit=0, withdraw=0, total_deposits=0, total_withdrawals=0):
        self.initial_balance = initial_balance
        self.deposit = deposit
        self.withdraw = withdraw
        self.total_deposits = total_deposits
        self.total_withdrawals = total_withdrawals

    def transaction(self):
        
        while True:
        #Allowing users to make as many iteration of transaction they want
            print("[1]Show Balance\n[2]Withdraw\n[3]Deposit\n[4]Print Statement\n[5]Email Statement\n[6]Quit")
            try:
                user_decis = int(input("Enter Choice: "))
            #Catching error so instead of breaking our progra, it's going to raise the problem and 
            #let user redo
            except ValueError:
                print("Invalid Entry")
                continue
            else:
                if user_decis == 1:
                    #Showing the user their initial balance or how much money they have in their bank account
                    print(f"\nCurrent Balance: ${self.initial_balance:.2f}")
                    print(".........................................")
                    print()
                    continue
                elif user_decis == 2:
                    #Giving user the options to decide how much they want to withdraw
                    while True:
                        print("Making Withdraw:\n[1]20\n[2]40\n[3]60\n[4]80\n[5]100\n[6]Custom Amount")
                        try:
                            user_choice = int(input("Choose Amount: "))
                        except ValueError:
                            print("Invalid Entry")
                            continue
                        else:
                            if user_choice == 1:
                                self.initial_balance = self.initial_balance - 20
                                self.withdraw = self.withdraw + 20
                                print(self.initial_balance)
                                try:
                                    wth_drawal_again = int(input("Do you want to withdraw more:\n[1]Yes\n[2]No\nChoose: "))
                                except ValueError:
                                    print("Invalid Entry")
                                else:
                                    if wth_drawal_again == 1:
                                        continue
                                    else:
                                        break
                            elif user_choice == 2:
                                self.initial_balance = self.initial_balance - 40
                                self.withdraw = self.withdraw + 40
                                print(self.initial_balance)
                                try:
                                    wth_drawal_again = int(input("Do you want to withdraw more:\n[1]Yes\n[2]No\nChoose: "))
                                except ValueError:
                                    print("Invalid Entry")
                                else:
                                    if wth_drawal_again == 1:
                                        continue
                                    else:
                                        break
                            elif user_choice == 3:
                                self.initial_balance = self.initial_balance - 60
                                self.withdraw = self.withdraw + 60
                                print(self.initial_balance)
                                try:
                                    wth_drawal_again = int(input("Do you want to withdraw more:\n[1]Yes\n[2]No\nChoose: "))
                                except ValueError:
                                    print("Invalid Entry")
                                    if wth_drawal_again == 1:
                                        continue
                                    else:
                                        break
                            elif user_choice == 4:
                                self.initial_balance = self.initial_balance - 80
                                self.withdraw = self.withdraw + 80
                                print(self.initial_balance)
                                try:
                                    wth_drawal_again = int(input("Do you want to withdraw more:\n[1]Yes\n[2]No\nChoose: "))
                                except ValueError:
                                    print("Invalid Entry")
                                else:
                                    if wth_drawal_again == 1:
                                        continue
                                    else:
                                        break
                            elif user_choice == 5:
                                self.initial_balance = self.initial_balance - 100
                                self.withdraw = self.withdraw + 100
                                print(self.initial_balance)
                                try:
                                    wth_drawal_again = int(input("Do you want to withdraw more:\n[1]Yes\n[2]No\nChoose: "))
                                except ValueError:
                                    print("Invalid Entry")
                                else:
                                    if wth_drawal_again == 1:
                                        continue
                                    else:
                                        break
                            elif user_choice == 6:
                                try:
                                    money_input = int(input("Enter Amount: "))
                                except ValueError:
                                    print("Invalid Entry")
                                else:
                                    if money_input % 20 == 0:
                                        self.initial_balance = self.initial_balance - money_input
                                        #self.withdraw keeps track of money being withdraw
                                        self.withdraw = self.withdraw + money_input
                                        print(self.initial_balance)
                                        try:
                                            wth_drawal_again = int(input("Do you want to withdraw more:\n[1]Yes\n[2]No\nChoose: "))
                                        except ValueError:
                                            print("Invalid Entry")
                                        else:
                                            if wth_drawal_again == 1:
                                                continue
                                            else:
                                                break
                                    else:
                                        print("Invalid Entry! Has to be divisible by $20")
                                        continue
                elif user_decis == 3:
                    #Allowing the users to enter the amount of money they want to deposit
                    while True:
                        try:
                            money_input = int(input("Enter Amount to Deposit: "))
                        except ValueError:
                            print("Invalid Entry")
                        else:
                            self.initial_balance = self.initial_balance + money_input
                            self.deposit = self.deposit + money_input
                            print(self.initial_balance)
                            try:
                                more_deposit = int(input("Do you want to Deposit Again:\n[1]Yes\n[2]No\nChoice: "))
                            except ValueError:
                                print("Invalid Entry")
                            else:
                                if more_deposit == 1:
                                    continue
                                else:
                                    break
                elif user_decis == 4:
                    #Printing out some form of Receipt
                    print()
                    print("               Your Statement                    ")
                    print("*************************************************")
                    print()
                    print("               Lah's Banking                     ")
                    print("*************************************************")
                    print()
                    print(f"      Total Withdrawal:............ ${self.withdraw:.2f}")
                    print(f"      Total Deposit:............... ${self.deposit:.2f}")
                    print()
                    print(f"      Remaining Balance:........... ${self.initial_balance:.2f}")
                    print()
                    print()
                    continue
                    pass
                elif user_decis == 5:
                    #Email Statement by creating another document
                    with open('Email_Statement.docx', 'w') as email_statement:
                        email_statement.write(" \n")
                        email_statement.write("               Your Email Statement                    \n")
                        email_statement.write("*************************************************\n")
                        email_statement.write(" \n")
                        email_statement.write("               Lah's Banking                     \n")
                        email_statement.write("*************************************************\n")
                        email_statement.write(" \n")
                        email_statement.write(f"      Total Withdrawal:............ ${self.withdraw:.2f}\n")
                        email_statement.write(f"      Total Deposit:............... ${self.deposit:.2f}\n")
                        email_statement.write(f"      Remaining Balance:........... ${self.initial_balance:.2f}\n")
                        email_statement.write(" \n")
                    pass
                elif user_decis == 6:
                    #Thanking the customer for Banking with us!
                    print("Thank You for Banking With Us!")
                    break
                    

#Allowing a form of script!
if __name__ == "__main__":
    print("Welcome to Lah's Banking")
    while True:
        try:
            customer_entry = int(input("[1]Log In\n[2]Sign Up\nChoose: "))
        except ValueError:
            print("Invalid Input!")
        else:
            if customer_entry == 1:
                if SignIn():
                    bank_account = Bank()
                    bank_account.transaction()
                break
            
            elif customer_entry == 2:
                SignUp.new_users()
                continue


    


