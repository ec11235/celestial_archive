from app.app_functionality.saving_loading_data import save_to_pickle, load_from_pickle
from classes.app_classes.loginpage import LoginPage

public_library_archive = 'app/data/public_library.pkl'


class App:
    """
    Class: App
    Main application class that manages user accounts, homepage, and public library interactions.
    
    Attributes:
        account (Account): The currently logged in user account.
        homepage (Homepage): The homepage associated with the account.
        loginpage (LoginPage): The login page for user authentication.
        public_library (Library): The public library containing datasets.
    """

    def __init__(self, account=None, homepage=None, loginpage=None, library=None):
        """
        Initializes the App class with optional parameters for account, homepage, loginpage, and library.
        
        Parameters:
        account (Account, optional): The currently logged in user account.
        homepage (Homepage, optional): The homepage associated with the account.
        loginpage (LoginPage, optional): The login page for user authentication.
        library (Library, optional): The library containing datasets.
        """
        self.account = account
        self.homepage = homepage
        self.loginpage = loginpage
        self.public_library = load_from_pickle(public_library_archive)  # Load the public library from a pickle file

    def display_homepage(self):
        """Displays the homepage."""
        pass

    def display_loginpage(self):
        """Displays the login page."""
        self.loginpage.display()

    def run_app(self):
        """Main function to run the application, handling user interactions."""
        exit_app = False
        login = LoginPage()
        account, account_homepage = login.display()
        while not exit_app:
            account_homepage.display()
            print("What would you like to do?\n")
            print("Options:\n (q) Add catalog from public library to personal library\n (p) Publish to the public library\n (o) Operate on a catalog in your personal library\n (e) Exit app")
            choice = input().strip().lower()
            match choice:
                case "q":
                    print("Available catalogs in public library:", self.public_library.list_catalogs())
                    print("What is the title of the catalog you wish to add?")
                    cat_selection = input().strip().lower()
                    cat = self.public_library.get_catalog(cat_selection)
                    if cat:
                        account.add_to_personal_library(cat)
                        print(f"Catalog '{cat_selection}' added to personal library.")
                    else:
                        print(f"Catalog '{cat_selection}' not found in public library.")
                case "p":
                    print("Available catalogs in personal library:", account.library.list_catalogs())
                    print("What is the title of the catalog you wish to publish?")
                    cat_selection = input().strip().lower()
                    cat = account.library.get_catalog(cat_selection)
                    if cat:
                        self.public_library.add_to_library(cat)
                        print(f"Catalog '{cat_selection}' published to public library.")
                    else:
                        print(f"Catalog '{cat_selection}' not found in personal library.")
                case "o":
                    print("Available catalogs in personal library:", account.library.list_catalogs())
                    print("What is the title of the catalog you wish to operate on?")
                    cat_selection = input().strip().lower()
                    catalog = account.library.get_catalog(cat_selection)
                    if catalog:
                        operation_exit = False
                        while not operation_exit:
                            print("What would you like to do with this catalog? (filter(f), delete(d), sort(s), add(a), return to homepage(r))")
                            o_choice = input().strip().lower()
                            match o_choice:
                                case "f":
                                    print("Filter by which column?")
                                    column = input().strip()
                                    filtered = catalog.filter_catalog(column)
                                    if filtered is not None:
                                        print(filtered)
                                case "d":
                                    print("Delete catalog (d) or entry at index(e)?")
                                    del_choice = input().strip().lower()
                                    if del_choice == "d":
                                        account.library.remove_from_library(cat_selection)
                                        print(f"Catalog '{cat_selection}' deleted from personal library.")
                                        operation_exit = True
                                    elif del_choice == "e":
                                        print("Delete which index?")
                                        index = int(input().strip())
                                        catalog.delete_from_catalog(index)
                                        print(f"Entry at index {index} deleted.")
                                case "s":
                                    print("Sort by which column?")
                                    column = input().strip()
                                    sorted_df = catalog.sort_catalog(column)
                                    if sorted_df is not None:
                                        print(sorted_df)
                                case "a":
                                    print("Enter details for the new entry:")
                                    pass
                                case "r":
                                    operation_exit = True
                        account.save_account()  # Save changes to the personal library
                    else:
                        print(f"Catalog '{cat_selection}' not found in personal library.")
                case "e":
                    exit_app = True


__all__ = ['App']
