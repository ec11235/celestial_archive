from app.app_functionality.saving_loading_data import save_to_pickle, load_from_pickle
from classes.account_classes.account import Account
from classes.app_classes.homepage import Homepage

class LoginPage:
    """
    Class representing the login page, allowing users to either sign up or log in.
    
    Attributes:
    data (dict): Dictionary holding account data loaded from a pickle file.

    Methods:
    display(): Displays the login/signup options, returns the account and homepage.
    login(username, password): Helper function to handle user login.
    signup(username, password): Helper function to handle user signup.
    check_valid_credentials(username, password): Helper function to validate user credentials.
    """
    
    def __init__(self):
        """
        Initializes the LoginPage object, loading account data from a pickle file.
        """
        self.data = load_from_pickle("app/data/account_data.pkl")

    def display(self):
        """
        Displays the login/signup options, allowing the user to log in or sign up.
        
        Returns:
        Account: The account of the logged-in or signed-up user.
        Homepage: The homepage associated with the logged-in or signed-up user's account.
        """
        account = None
        valid = False
        while valid == False:
            print("Would you like to login or signup?\n")
            option = input()
            if option == 'login':
                print("\nplease enter your username\n")
                username = input()
                print('please enter your password')
                password = input()
                valid = self.login(username, password)
                if valid:
                    account = Account.load_account(username)
            
            elif option == "signup":
                print("\nEnter a Username: ")
                username = input()
                print("\nEnter a Password: ")
                password = input()
                self.signup(username, password)
                account = Account.load_account(username)
                valid = True

            else:
                print("\nOption not valid: enter 'login' or 'signup'\n")

        return account, Homepage(account)
    
    def login(self, username, password):
        """
        Helper function to handle user login.

        Parameters:
        username (str): The username entered by the user.
        password (str): The password entered by the user.

        Returns:
        bool: True if login is successful, False otherwise.
        """
        if self.check_valid_credentials(username, password):
            account = Account.load_account(username)
            if account:
                print("login successful\n")
                return True
            else:
                print("failed to load account\n")
        else:
            print("invalid username or password")
        return False
    
    def signup(self, username, password):
        """
        Helper function to handle user signup.

        Parameters:
        username (str): The username entered by the user.
        password (str): The password entered by the user.
        """
        if username in self.data:
            print("Username already exists. Please choose a different username.")
        else:
            account = Account(username, password)
            self.data[username] = account.get_info()
            account.save_account()
            save_to_pickle(self.data, "app/data/account_data.pkl")
            print("Signup successful. You can now log in.")

    def check_valid_credentials(self, username, password):
        """
        Helper function to validate user credentials.

        Parameters:
        username (str): The username entered by the user.
        password (str): The password entered by the user.

        Returns:
        bool: True if credentials are valid, False otherwise.
        """
        return username in self.data and self.data[username][1] == password
