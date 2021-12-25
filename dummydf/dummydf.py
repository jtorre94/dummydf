# Depending on the randomise parameter, this module generates a dataframe with different
# column types that can be used for unit testing if randomise = False or for experimenting
# with random real world data if randomise = True.
# for unit testing.
# The columns to display must be specified upon instantiating the class, via
# the parameter columns_to_display. A dictionary must be passed as an argument,
# with keys the column names that will display in the output dataframe and the
# values, the existing built-in types.
#
# The available types are:
#     'ACCOUNT': simulates account numbers
#     'BYTE': bytearray simulating importing hex values in byte format by mistake.
#     'INTEGER': between two config values.
#     'FLOAT': between 0 and 1.
#     'DATETIME': in string type, as it's common to find like this in the files.
#     'STRING': including undesirable special characters intended to break the tests.
#     'HEX': simulates hexadecimal values such as proforma GUIDs from SAP.
#
# Example of class instantiation:
# dummy = DummyDataframe(
#   columns_to_display=
#   {
#       'CONTRACT_ACCOUNT': 'ACCOUNT',
#       'PROFORMA_GUID': 'HEX',
#       'BALANCE': 'FLOAT',
#       'CALL_DATE': 'DATETIME'
#   }
# )
#
# Finally, the the dataframe can be accessed via the df attribute of the instance:
# dummy.df
#
# The resulting dataframe will have NaN, None and rubbish strings inserted to add
# more realism to it.

"""
Dummy Dataframe
"""

import string
import random
import numpy as np
import pandas as pd
import yaml
from datetime import datetime
from typing import Union
import os


class DummyDataframe:
    """
    Class used to generate the dataframe for tests.

    """

    # This is the default file that will be used if not specified otherwise.
    YAML_FILE_DEFAULT = os.path.join(os.path.dirname(__file__), 'config', 'config_dummydf.yml')

    def __init__(self, yaml_config: dict = None, columns_to_display: dict = None, randomise: bool = False) -> None:
        """
        1. Fetch the config to avoid harcoding values in the code.
        2. Determine if stuff should be randomised for experimenting or rigged for unit testing.
        3. Create the dataframe.
        4. Insert values such as np.nan, None or 'NONE' to simulate real life rubbish.
        5. Determine what columns should be displayed in the output dataframe and what types should be those
        columns of.

        Args:
            yaml_config (dict): dictionary to use. If not specified, it will take it from the YAML config file.
            columns_to_display (dict): what columns should be displayed.
            randomise (bool): default False.
        """
        # Load config dictionary from yaml file
        self.cfg = yaml_config or self.fetch_yaml_config()
        # Determine if the output needs to be randomised or rigged.
        self.randomise = randomise
        # If no columns are specified, take the default example columns from the YAML file.
        self.columns_to_display = columns_to_display or self.cfg['example_columns']

        # Create the dataframe without rubbish values
        self.df = self.create_dataframe()
        # Insert the rubbish
        self.df = self.insert_rubbish_to_df(self.df)
        # Display only the specified column types with the specified names
        self.df = self.select_columns_to_display(self.df)
        self.df = self.change_column_names(self.df)

    @staticmethod
    def fetch_yaml_config(yaml_file: str = YAML_FILE_DEFAULT) -> dict:
        """
        Provides yaml config dictionary

        Args:
            yaml_file (str): path to the .yml file

        Returns: dict
        """
        with open(yaml_file, 'r') as ymlfile:
            return yaml.safe_load(ymlfile)

    def initialise_seed(self) -> None:
        """
        Rig Both random and np.random seeds to produce always the same outputs. It must be
        called before each method that uses either of the above modules.

        Returns: None

        """
        if not self.randomise:
            random.seed(10)
            np.random.seed(10)

    def generate_list_with_random_strings(self) -> list:
        # Randomise if argument randomise was passed as True
        self.initialise_seed()
        characters_to_choose_from = \
            string.ascii_lowercase + string.ascii_uppercase + '1234567890' + r'+_#@ñó´,' r'aq´ç+¡|@#~€¬ '
        return [''.join(random.choices(characters_to_choose_from, k=self.cfg['length_strings']))
                for _ in range(self.cfg['dataframe_rows'])]

    def generate_list_with_random_bytes(self) -> list:
        self.initialise_seed()
        return [bytearray(random.getrandbits(8) for _ in range(self.cfg['length_bytes']))
                for _ in range(self.cfg['dataframe_rows'])]

    def add_hour_minute_second_to_date(self, datetime_var: datetime) -> datetime:
        """
        Given a datetime object, it sets the hour, minute and second to random values.
        This is useful because datetime ranges perform poorly if they need to be generated
        second by second, so I generate one date per year and then add random hour/minute/
        second to simulate randomness.

        Args:
            datetime_var (datetime): original date.

        Returns: datetime
             with randomised hour, minute and second.

        """
        self.initialise_seed()
        datetime_var = datetime_var.replace(
            hour=random.randint(0, 23),
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )
        return datetime_var

    def adapt_datetime_to_format(self, datetime_var: datetime) -> str:
        """
        1. Add random hour/minute/second to given date.
        2. Convert to string with format '%d.%m.%Y %H:%M:%S'

        Args:
            datetime_var (datetime): to be adapted as string with random H, m, s

        Returns: str
            formatted string.

        """
        datetime_var = self.add_hour_minute_second_to_date(datetime_var)
        return datetime_var.strftime('%d.%m.%Y %H:%M:%S')

    def generate_list_with_random_datetimes(self) -> list:
        self.initialise_seed()
        daterange_to_choose = pd.date_range(self.cfg['datetime_start'], self.cfg['datetime_end'], freq='M')
        return list(map(self.adapt_datetime_to_format, [random.choice(daterange_to_choose)
                                                        for _ in range(self.cfg['dataframe_rows'])]))

    def generate_list_with_random_accounts(self) -> list:
        self.initialise_seed()
        return [random.randrange(1, 999999999999, 1) for _ in range(self.cfg['dataframe_rows'])]

    def generate_list_with_random_floats(self) -> np.ndarray:
        self.initialise_seed()
        return np.array(np.random.randn(self.cfg['dataframe_rows']), dtype=float)

    def generate_list_with_random_integers(self) -> np.ndarray:
        self.initialise_seed()
        # Return type must be int64
        return np.array(np.random.randint(0, self.cfg['max_integer'], self.cfg['dataframe_rows']), dtype=np.int64)

    def generate_list_with_random_hexadecimal_digits(self) -> list:
        self.initialise_seed()
        HEXDIGITS = '0123456789ABCDEF'
        return [''.join([HEXDIGITS[random.randint(0, 0xF)] for _ in range(self.cfg['hex_number_length'])]) for __ in
                range(self.cfg['dataframe_rows'])]

    def create_dataframe(self) -> pd.DataFrame:
        """
        Using the random lists generated, create a dataframe.

        Returns: pd.DataFrame
            with the different column types.

        """
        array_strings = self.generate_list_with_random_strings()
        array_bytes = self.generate_list_with_random_bytes()
        array_datetimes = self.generate_list_with_random_datetimes()
        array_accounts = self.generate_list_with_random_accounts()
        array_floats = self.generate_list_with_random_floats()
        array_integers = self.generate_list_with_random_integers()
        array_hex = self.generate_list_with_random_hexadecimal_digits()

        return pd.DataFrame(
            {
                'STRING': array_strings,
                'DATETIME': array_datetimes,
                'FLOAT': array_floats,
                'INTEGER': array_integers,
                'BYTE': array_bytes,
                'ACCOUNT': array_accounts,
                'HEX': array_hex
            }
        )

    def insert_random_values_to_df(self, df: pd.DataFrame, value_to_insert: Union[float, str, None] = np.nan,
                                   probability: float = 0.05) -> pd.DataFrame:
        """
        To simulate a real life dataframe, insert a value randomly into the dataframe.

        Args:
            df (pd.DataFrame): original dataframe.
            value_to_insert (Union[float, str, None]): value to insert randomly.
            probability (float): likelihood of a value to be inserted in a certain cell.

        Returns: pd.DataFrame
            input dataframe with the random rubbish values inserted.

        """
        self.initialise_seed()
        mask = np.random.random(df.shape) < probability
        return df.where(~mask, other=value_to_insert)

    def insert_rubbish_to_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Based on the config dictionary, insert config values with config probability.

        Args:
            df (pd.DataFrame): dataframe in which random values are to be inserted.

        Returns: pd.DataFrame


        """
        for value, prob in self.cfg['rubbish_to_insert'].items():
            df = self.insert_random_values_to_df(df, value_to_insert=value, probability=prob)
        return df

    def select_columns_to_display(self, df: pd.DataFrame) -> pd.DataFrame:
        # Return only the configured column names.
        return df[self.columns_to_display.values()]

    def change_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        # Change to the configured column names.
        return df.set_axis(self.columns_to_display.keys(), axis=1)


if __name__ == '__main__':
    pass
