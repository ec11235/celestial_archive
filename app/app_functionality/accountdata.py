from app.app_functionality.saving_loading_data import save_to_pickle, load_from_pickle

account_file = "app/data/account_data.pkl"
data_folder = "app/data"

class AccountData:
    def __init__(self):
        self.data = self.load_user_data()

    def add_to_user_data(self, account):
        if account.username not in self.data:
            self.data[account.username] = account.get_info()

    def load_user_data(self):
        return load_from_pickle(account_file)

    def save_user_data(self):
        save_to_pickle(self.data, account_file)
    
    def load_user_data(self):
        load_from_pickle(account_file)

    def check_valid_credentials(self, username, password):
        if username in self.data and self.data[username][1] == password:
            return True
        else:
            return False