from app.app_functionality.saving_loading_data import save_to_pickle, load_from_pickle
import pandas as pd

public_library_archive = 'app/data/public_library.pkl'


class Library:
    """
    Class: Library
    Manages a collection of catalogs containing celestial objects.
    
    Attributes:
        catalogs (dict): A dictionary storing catalogs by their object type.
    """

    def __init__(self):
        """Initializes an empty library with a dictionary to hold catalogs."""
        self.catalogs = {}

    def add_to_library(self, catalog):
        """
        Adds a catalog to the library.
        
        Parameters:
        catalog (Catalog): The catalog to be added.
        """
        if catalog.object_type not in self.catalogs:
            self.catalogs[catalog.object_type] = catalog
        else:
            self.catalogs[catalog.object_type].information = pd.concat(
                [self.catalogs[catalog.object_type].information, catalog.get_data()], ignore_index=True
            )

    def remove_from_library(self, object_type, index=None):
        """
        Removes a catalog or an entry from a catalog in the library.
        
        Parameters:
        object_type (str): The type of the object.
        index (int, optional): The index of the entry to be removed. If None, removes the entire catalog.
        """
        if index is not None:
            if object_type in self.catalogs:
                self.catalogs[object_type].delete_from_catalog(index)
        else:
            del self.catalogs[object_type]

    def display_catalogs(self):
        """Displays all catalogs and their data in the library."""
        print("\nPublic Library\n")
        for object_type, catalog in self.catalogs.items():
            print(f"Catalog for {object_type}:")
            print(catalog.get_data())
            print()
    
    def get_catalog(self, name):
        """
        Retrieves a catalog by name.
        
        Parameters:
        name (str): The name of the catalog to retrieve.
        
        Returns:
        Catalog: The catalog object if found, else None.
        """
        return self.catalogs.get(name.lower())

    def list_catalogs(self):
        """
        Lists all catalog names in the library.
        
        Returns:
        list: A list of catalog names.
        """
        return list(self.catalogs.keys())

    def save_lib_to_pickle_pub(self):
        """Saves the public library to a pickle file."""
        save_to_pickle(self, public_library_archive)

    def load_lib_from_pickle_pub(self):
        """Loads the public library from a pickle file."""
        load_from_pickle(public_library_archive)

    def save_lib_to_pickle_self(self, filename):
        """
        Saves the library to a specified pickle file.
        
        Parameters:
        filename (str): The name of the file to save the library.
        """
        save_to_pickle(self.catalogs, filename)

    def load_lib_from_pickle_self(self, filename):
        """
        Loads the library from a specified pickle file.
        
        Parameters:
        filename (str): The name of the file to load the library from.
        """
        load_from_pickle(filename)


__all__ = ['Library']
