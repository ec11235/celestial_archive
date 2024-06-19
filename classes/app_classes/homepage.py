from app.app_functionality.saving_loading_data import save_to_pickle, load_from_pickle

public_library_archive = 'app/data/public_library.pkl'

class Homepage:
    """
    Class representing the homepage for an account, allowing interaction with the public library and personal library.
    """

    def __init__(self, account=None): 
        """
        Initializes the Homepage object.

        Parameters:
        account (Account): The account associated with this homepage.
        """
        self.account = account
        self.public_library = load_from_pickle(public_library_archive) 

    def search_main_library(self, name):
        """
        Placeholder for a method to search the main public library.
        """
        pass

    def get_catalog_from_pub_lib(self, name):
        """
        Retrieves a catalog from the public library by name.

        Parameters:
        name (str): The name of the catalog to retrieve.

        Returns:
        Catalog: The requested catalog from the public library.
        """
        return self.public_library.get_catalog(name)

    def add_to_personal_library(self, catalog):
        """
        Adds a catalog to the personal library of the account.

        Parameters:
        catalog (Catalog): The catalog to add.
        """
        self.account.add_to_personal_library(catalog)

    def delete_from_personal_library(self, catalog):
        """
        Deletes a catalog from the personal library of the account.

        Parameters:
        catalog (Catalog): The catalog to delete.
        """
        self.account.remove_from_personal_library(catalog)

    def publish_catalog(self, catalog):
        """
        Publishes a catalog to the public library.

        Parameters:
        catalog (Catalog): The catalog to publish.
        """
        self.public_library.add_to_library(catalog)

    def display(self):
        """
        Displays the account username, public library catalogs, and personal library catalogs.
        """
        print("Account: ", self.account.username)
        self.public_library.display_catalogs()
        self.account.display_personal_library()

