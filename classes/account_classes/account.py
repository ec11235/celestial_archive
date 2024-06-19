import os
import pandas as pd
from app.app_functionality.saving_loading_data import save_to_pickle, load_from_pickle

account_file = "app/data/account_data.pkl"
data_folder = "app/data"

class Account:
    """
    Class: Account
    Manages user account details and personal library.
    
    Attributes:
        a_type (str): Account type, default is 'user'.
        username (str): Username of the account.
        password (str): Password of the account.
        library (Library): Personal library of the user.
    """

    def __init__(self, username, password, a_type="user"):
        """
        Initializes an Account with username, password, and library.
        
        Parameters:
        username (str): Username of the account.
        password (str): Password of the account.
        a_type (str): Type of the account, default is 'user'.
        """
        self.a_type = a_type
        self.username = username
        self.password = password
        self.library = self.create_library()

    def create_library(self):
        """
        Creates a personal library for the account.
        
        Returns:
        Library: An instance of the Library class.
        """
        from ..app_classes.library import Library
        return Library()

    def delete_account(self):
        """Placeholder for future implementation of account deletion."""
        pass

    def change_password(self, new_password):
        """
        Changes the account password.
        
        Parameters:
        new_password (str): The new password.
        """
        self.password = new_password
    
    def add_to_personal_library(self, catalog):
        """
        Adds a catalog to the personal library.
        
        Parameters:
        catalog (Catalog): The catalog to be added.
        """
        if catalog.object_type not in self.library.catalogs:
            self.library.catalogs[catalog.object_type] = catalog
            self.save_account()
        else:
            self.library.catalogs[catalog.object_type].information = pd.concat(
                [self.library.catalogs[catalog.object_type].information, catalog.get_data()], ignore_index=True)
            self.save_account()

    def remove_from_personal_library(self, object_type, index=None):
        """
        Removes a catalog or an entry from the personal library.
        
        Parameters:
        object_type (str): The type of the object.
        index (int, optional): The index of the entry to be removed. If None, removes the entire catalog.
        """
        if index is not None:
            if object_type in self.library.catalogs:
                self.library.catalogs[object_type].delete_from_catalog(index)
        else:
            del self.library.catalogs[object_type]

    def get_info(self):
        """
        Retrieves account information.
        
        Returns:
        list: A list containing account type, password, and library.
        """
        return [self.a_type, self.password, self.library]
    
    def display_personal_library(self):
        """Displays the personal library."""
        print("\nPersonal Library\n")
        for object_type, catalog in self.library.catalogs.items():
            print(f"Catalog for {object_type}:")
            print(catalog.get_data())
            print()

    def get_library(self):
        """
        Retrieves the personal library.
        
        Returns:
        Library: The personal library of the account.
        """
        return self.library
    
    def save_account(self):
        """
        Saves the account details to a pickle file.
        """
        user_file = os.path.join(data_folder, f"{self.username}.pkl")
        save_to_pickle(self, user_file)
    
    @staticmethod
    def load_account(username):
        """
        Loads an account from a pickle file.
        
        Parameters:
        username (str): The username of the account to load.
        
        Returns:
        Account: The loaded account object if found, else None.
        """
        user_file = os.path.join(data_folder, f"{username}.pkl")
        if os.path.exists(user_file):
            return load_from_pickle(user_file)
        else:
            print("Account not found.")
            return None


__all__ = ['Account']

