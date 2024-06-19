import pandas as pd
from app.app_functionality.saving_loading_data import save_to_pickle, load_from_pickle

class Catalog:
    """
    Class to manage a collection of celestial objects.
    """

    def __init__(self):
        """
        Initializes the Catalog object with default values.
        """
        self.object_type = None
        self.information = pd.DataFrame()

    def add_to_catalog(self, obj):
        """
        Adds an object to the catalog.

        Parameters:
        obj (object): The object to add to the catalog.
        """
        if self.object_type is None:
            self.object_type = obj.o_type  
        elif obj.o_type != self.object_type:
            print(f"New entry type: {obj.o_type} must be the same as catalog: {self.object_type}")
            return
        new_entry = pd.DataFrame([obj.__dict__])
        if self.information.empty:
            self.information = new_entry
        else:
            self.information = pd.concat([self.information, new_entry], ignore_index=True)

    def delete_from_catalog(self, index):
        """
        Deletes an entry from the catalog by index.

        Parameters:
        index (int): The index of the entry to delete.
        """
        if index in self.information.index:
            self.information = self.information.drop(index)

    def valid_name(self, name):
        """
        Placeholder for a method to validate object names.
        """
        pass

    def get_data(self):
        """
        Returns the data in the catalog as a DataFrame.
        """
        return self.information

    def filter_catalog(self, column):
        """
        Filters the catalog by a specified column.

        Parameters:
        column (str): The column to filter by.

        Returns:
        DataFrame: The filtered DataFrame.
        """
        if column in self.information.columns:
            return self.information[column]
        else:
            print(f"Column '{column}' does not exist.")
            return None

    def sort_catalog(self, column):
        """
        Sorts the catalog by a specified column.

        Parameters:
        column (str): The column to sort by.

        Returns:
        DataFrame: The sorted DataFrame.
        """
        if column in self.information.columns:
            return self.information.sort_values(by=column)
        else:
            print(f"Column '{column}' does not exist.")
            return None

    def save_cat_to_pickle(self, filename):
        """
        Saves the catalog to a pickle file.

        Parameters:
        filename (str): The name of the file to save the catalog to.
        """
        save_to_pickle(self.information, filename)

    def load_cat_from_pickle(self, filename):
        """
        Loads the catalog from a pickle file.

        Parameters:
        filename (str): The name of the file to load the catalog from.
        """
        load_from_pickle(filename)

