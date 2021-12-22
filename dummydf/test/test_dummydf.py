import unittest
from datetime import datetime as dt
import pandas as pd
from numpy import nan
from pandas.testing import assert_frame_equal
from dummydf import DummyDataframe

# Sample config to avoid dependencies on external config files for unit testing
YAML_CONFIG_DICT = {
    'dataframe_rows': 20,
    'length_strings': 30,
    'length_bytes': 15,
    'max_integer': 1000,
    'hex_number_length': 15,
    'rubbish_to_insert':
        {nan: 0.025, None: 0.025, 'NULL': 0.025, 'NONE': 0.025, 'NaN': 0.025, ' ': 0.025},
    'datetime_start': dt(year=2020, month=1, day=1),
    'datetime_end': dt(year=2030, month=12, day=31),
    'example_columns':
        {'CACONT_ACC': 'ACCOUNT', 'PROFORMA_GUID': 'BYTE', 'CALL_ATTEMPTS': 'INTEGER', 'BALANCE': 'FLOAT',
         'CALL_DATE': 'DATETIME', 'EXHAUSTED_REASON': 'STRING', 'GUID_HEX': 'HEX'}
}

# Borken sample config to avoid dependencies on external config files for unit testing
YAML_CONFIG_DICT_BROKEN = {}


class TestFinalDataframe(unittest.TestCase):

    def setUp(self) -> None:
        self.expected_df = \
            pd.DataFrame(
                {'CACONT_ACC': {0: 36813893844.0, 1: ' ', 2: 15367785145.0, 3: 507691326081.0, 4: 540364100186.0,
                                5: 308479965304.0, 6: 891864873414.0, 7: 35047919088.0, 8: 539107169880.0,
                                9: 83012152132.0, 10: 820136103699.0, 11: 399417170928.0, 12: 459752868893.0,
                                13: 154018218884.0, 14: 389137740586.0, 15: 461200485898.0, 16: 907456230416.0,
                                17: 290661760782.0, 18: 190940635886.0, 19: ' '},
                 'PROFORMA_GUID': {0: bytearray(b'\x92\x08m{\x93\x034v\xd0}\xd2G\xa7\xcf)'),
                                   1: bytearray(b'\x08\x85}S\x13?\xf3\xf3\xbe\xff\\\x0bk\xdc#'),
                                   2: bytearray(b'\x9aZakH\xd3\xacCt,\xafM\xa9\\"'),
                                   3: bytearray(b't\xc4\xdc\xfb=\xf8p\x9d`\x0b\x95\x01<"1'),
                                   4: bytearray(b'\xf0\xe8M\x89]\xc5\xe5=P\xaa\x8csox\x10'),
                                   5: bytearray(b'\xa7\x95S\xd8\x80(\xd79\xf8i=\t\x08\x7fM'),
                                   6: bytearray(b'\xd1\x9b\xa8\x12\x88\xec\xda\x14&b\x91\xf2_\xe9\x99'),
                                   7: bytearray(b'&\x1c\xf6\xc6\xc5\x18q*\xfb\xce0\xf2Yn\xf8'),
                                   8: bytearray(b'jr>\xaeF$\x9e\x85-\xdd\x1eDtM*'),
                                   9: bytearray(b'\xa9\xa6\xf1\xd2,\xc7-z\xc5XSo9\x01\x8b'),
                                   10: bytearray(b'\xb6\x0bT\xe5Q>\x14Crg\x95(c\xeb\xde'),
                                   11: bytearray(b'~\xac\xe4=\xbc\x86\xfe\xe9E\x85{\x9a\x7f\x10*'),
                                   12: bytearray(b'}\xacv\xe5f"k\x8a\x95Y\x89c}\xb3*'),
                                   13: bytearray(b'\x8fp\x19\xf7\xf9j\xd4\t\xdf\x00p\x89\x10\x0cY'),
                                   14: bytearray(b'\x17&\x1b\x9bt\xd5\xfe\xcc|#u\xdco\xc6\x80'),
                                   15: bytearray(b'\xecrW\xb9B\xe5\xc9\xb2ulT\xa6\x85\xe8\x85'),
                                   16: bytearray(b"\'\xbd<R\x9e\x08\xaf2\xa4\xe7\x96\x93\xd4\xa0z"),
                                   17: bytearray(b'\x06\xce\x1d\xf6Ko\xd9\xdb?\xb7J\xe3\x16\x0b\x98'),
                                   18: bytearray(b'\xe9\x8c\xc4\xfb\xf6\x1b\xfb\xd1I)\xabz$\\\x98'),
                                   19: bytearray(b'f\xeb\xc91\xfcY.\x14\x971m5\xfc\x18\xaf')},
                 'CALL_ATTEMPTS': {0: 265, 1: 125, 2: 996, 3: 527, 4: 320, 5: 369, 6: 123, 7: 156, 8: 985, 9: 733,
                                   10: 496, 11: 925, 12: 881, 13: 8, 14: 73, 15: 256, 16: 490, 17: 40, 18: 502,
                                   19: 420},
                 'BALANCE': {0: 1.331586504129518, 1: 0.7152789743984055, 2: -1.5454002921112682,
                             3: -0.008383849928522256, 4: 0.6213359738904805, 5: -0.7200855607188968,
                             6: 0.2655115856921195, 7: 0.10854852571496944, 8: 0.004291430934033236,
                             9: -0.17460021059294129, 10: 0.433026189953598, 11: 1.203037373812212,
                             12: -0.9650656705167633, 13: 1.028274077982704, 14: 0.2286301301246597,
                             15: 0.44513761283034786, 16: -1.1366022118310442, 17: 0.1351368784486355,
                             18: 1.4845370018365822, 19: -1.079804885785276},
                 'CALL_DATE': {0: ' ', 1: '28.02.2029 18:02:27', 2: '30.04.2030 18:02:27', 3: '30.04.2020 18:02:27',
                               4: '31.05.2024 18:02:27', 5: '30.11.2029 18:02:27', 6: '30.06.2030 18:02:27',
                               7: '31.12.2025 18:02:27', 8: '30.06.2023 18:02:27', 9: '30.09.2020 18:02:27',
                               10: '30.06.2030 18:02:27', 11: '31.12.2026 18:02:27', 12: '31.08.2021 18:02:27',
                               13: '30.04.2025 18:02:27', 14: '30.09.2027 18:02:27', 15: '31.12.2020 18:02:27',
                               16: '31.12.2028 18:02:27', 17: '31.12.2022 18:02:27', 18: '31.07.2027 18:02:27',
                               19: '29.02.2028 18:02:27'},
                 'EXHAUSTED_REASON': {0: 'VJVró´3nRBu~ dqYFx5L53l_¬€Ydal', 1: '#zE+ATKfWamsIdPó3SamVFXj#inó#J',
                                      2: 'IuwZojLn2´#NCKa8BAgLWG´4uR¡RXf', 3: 'OMHIWSOnK€IcaSehjL OMKPL9+6J2¡',
                                      4: 'mtZ62W´Nó~Kq8çd¡_~¬x4lX|pDgqrh', 5: ' çM06RJ4UwE11rY´´3fJhevL_1x6QQ',
                                      6: 'vKC9OLNN68ñH@€ 8fa,bBA0Yxpnh@@', 7: 's0#pVK€´bqaVRó_~Bd6eUqGXonYq c',
                                      8: '|QCGVCmq7Y8¬o´´CUMqJm@p1V€@DFe', 9: 'ez#eo1Dp#dXJCqnH+M#´oçWIQçGh~j',
                                      10: 'i8zy2çC¡ZYSbn56i1NVHsD€pqSgób,', 11: 'C|9DZ¬ory´uuZWITcace_¬kFbK3Z+T',
                                      12: 'eFMBc1O7EfwoMmgRlij7ñóV1+JQ81Y', 13: '2Srz6IqF4jyaoZcYL+´#C4mOGMwrR3',
                                      14: 'U~Um2A@kL4€RF#@¡8k @K3,|9hfELz', 15: '+_H6p#umFqX5óG~¬S+aXk3LaraooFr',
                                      16: 'BWmODa4P#´d8M´j,JhM´gFga´TV+h#', 17: '+aóGb 186y3LsPMz+¡XbT1óztFn#cU',
                                      18: ',cn z_cMdub5LDI5vmd34tQ€N_DT#6', 19: 'XyeO8D9NfWTAq¬W9d9nOGG@q#aO´T|'},
                 'GUID_HEX': {0: '1DF06EF851FA27B', 1: '1D4BCD98E59B4E7', 2: 'EC107469B7AEDF2', 3: 'A57D711F9224CB4',
                              4: '33E56BDDE784538', 5: 'E9555FBAD701AA7', 6: '28EC5CF78FF25FE', 7: 'C4DBCF5E3D10E21',
                              8: 'B243EF4EDEA8EDA', 9: '47A16F039D79213', 10: '95F4BC6B526D639', 11: 'EDE68B306DDC62D',
                              12: '21B8BED69E9F8CE', 13: 'AB8FEFF2BC5D290', 14: 'AA2CB957593172D',
                              15: '6E0C6A6A111BCA5', 16: '53B50B2CEB14EFE', 17: 'E5BDAEC63D4156D',
                              18: 'BC11597153B591C', 19: 'D2B6F55CEA155D4'}
                 }
            )

    def test_final_dataframe_output_ok_if_not_randomised(self):
        actual_df = DummyDataframe(yaml_config=YAML_CONFIG_DICT, randomise=False).df
        assert_frame_equal(self.expected_df, actual_df)

    def test_raise_assertion_error_if_randomised_dataframe(self):
        actual_df = DummyDataframe(yaml_config=YAML_CONFIG_DICT, randomise=True).df
        with self.assertRaises(AssertionError):
            assert_frame_equal(self.expected_df, actual_df)


class TestAuxiliaryFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy = DummyDataframe(yaml_config=YAML_CONFIG_DICT)

    def test_first_string_generated_correctly_generated(self):
        expected_string = r'VJVró´3nRBu~ dqYFx5L53l_¬€Ydal'
        actual_string = self.dummy.generate_list_with_random_strings()[0]
        self.assertEqual(expected_string, actual_string)

    def test_first_bytearray_generated_correctly_generated(self):
        expected_bytearray = bytearray(b'\x92\x08m{\x93\x034v\xd0}\xd2G\xa7\xcf)')
        actual_bytearray = self.dummy.generate_list_with_random_bytes()[0]
        self.assertEqual(expected_bytearray, actual_bytearray)

    def test_add_hour_minute_second_to_date(self):
        expected_datetime = dt(year=2015, month=6, day=28, hour=18, minute=2, second=27)
        actual_datetime = self.dummy.add_hour_minute_second_to_date(dt(year=2015, month=6, day=28))
        self.assertEqual(expected_datetime, actual_datetime)

    def test_adapt_datetime_to_format(self):
        expected_string = '28.06.2015 18:02:27'
        actual_string = self.dummy.adapt_datetime_to_format(dt(year=2015, month=6, day=28))
        self.assertEqual(expected_string, actual_string)

    def test_first_datetime_correctly_generated(self):
        self.dummy.cfg['datetime_start'] = dt(year=2020, month=1, day=1)
        self.dummy.cfg['datetime_end'] = dt(year=2030, month=12, day=31)
        expected_string = '30.09.2020 18:02:27'
        actual_string = self.dummy.generate_list_with_random_datetimes()[0]
        self.assertEqual(expected_string, actual_string)

    def test_first_account_correctly_generated(self):
        expected_account = 36813893844
        actual_account = self.dummy.generate_list_with_random_accounts()[0]
        self.assertEqual(expected_account, actual_account)

    def test_first_float_correctly_generated(self):
        expected_float = 1.331586504129518
        actual_float = self.dummy.generate_list_with_random_floats()[0]
        self.assertEqual(expected_float, actual_float)

    def test_first_integer_correctly_generated(self):
        expected_integer = 265
        actual_integer = self.dummy.generate_list_with_random_integers()[0]
        self.assertEqual(expected_integer, actual_integer)

    def test_first_hexadecimal_value_correctly_generated(self):
        expected_hex_digit = '1DF06EF851FA27B'
        actual_hex_digit = self.dummy.generate_list_with_random_hexadecimal_digits()[0]
        self.assertEqual(expected_hex_digit, actual_hex_digit)

    def test_dataframe_head_correctly_created(self):
        expected_df = pd.DataFrame(
            {'STRING': {0: 'VJVró´3nRBu~ dqYFx5L53l_¬€Ydal', 1: '#zE+ATKfWamsIdPó3SamVFXj#inó#J',
                        2: 'IuwZojLn2´#NCKa8BAgLWG´4uR¡RXf', 3: 'OMHIWSOnK€IcaSehjL OMKPL9+6J2¡',
                        4: 'mtZ62W´Nó~Kq8çd¡_~¬x4lX|pDgqrh'},
             'DATETIME': {0: '30.09.2020 18:02:27', 1: '28.02.2029 18:02:27', 2: '30.04.2030 18:02:27',
                          3: '30.04.2020 18:02:27', 4: '31.05.2024 18:02:27'},
             'FLOAT': {0: 1.331586504129518, 1: 0.7152789743984055, 2: -1.5454002921112682, 3: -0.008383849928522256,
                       4: 0.6213359738904805}, 'INTEGER': {0: 265, 1: 125, 2: 996, 3: 527, 4: 320},
             'BYTE': {0: bytearray(b'\x92\x08m{\x93\x034v\xd0}\xd2G\xa7\xcf)'),
                      1: bytearray(b'\x08\x85}S\x13?\xf3\xf3\xbe\xff\\\x0bk\xdc#'),
                      2: bytearray(b'\x9aZakH\xd3\xacCt,\xafM\xa9\\"'),
                      3: bytearray(b't\xc4\xdc\xfb=\xf8p\x9d`\x0b\x95\x01<"1'),
                      4: bytearray(b'\xf0\xe8M\x89]\xc5\xe5=P\xaa\x8csox\x10')},
             'ACCOUNT': {0: 36813893844, 1: 530123041873, 2: 15367785145, 3: 507691326081, 4: 540364100186},
             'HEX': {0: '1DF06EF851FA27B', 1: '1D4BCD98E59B4E7', 2: 'EC107469B7AEDF2', 3: 'A57D711F9224CB4',
                     4: '33E56BDDE784538'}}
        )
        actual_df = self.dummy.create_dataframe().head(5)
        assert_frame_equal(expected_df, actual_df)


class TestInsertRubbishIntoDataframe(unittest.TestCase):

    def setUp(self) -> None:
        self.dummy = DummyDataframe(yaml_config=YAML_CONFIG_DICT)
        self.df_to_use = pd.DataFrame(
            {'COLUMNA1': ['VALOR1', 'VALOR2', 'VALOR3', 'VALOR4', 'VALOR5', 'VALOR6'],
             'COLUMNA2': ['VALOR1', 'VALOR2', 'VALOR3', 'VALOR4', 'VALOR5', 'VALOR6'],
             'COLUMNA3': ['VALOR1', 'VALOR2', 'VALOR3', 'VALOR4', 'VALOR5', 'VALOR6']}
        )

    def test_values_inserted_in_df(self):
        expected_df = pd.DataFrame(
            {'COLUMNA1': {0: 'VALOR1', 1: 'VALOR2', 2: 'VALOR3', 3: 'VALOR4', 4: nan, 5: 'VALOR6'},
             'COLUMNA2': {0: nan, 1: 'VALOR2', 2: 'VALOR3', 3: 'VALOR4', 4: 'VALOR5', 5: 'VALOR6'},
             'COLUMNA3': {0: 'VALOR1', 1: 'VALOR2', 2: 'VALOR3', 3: 'VALOR4', 4: 'VALOR5', 5: 'VALOR6'}}
        )
        actual_df = self.dummy.insert_random_values_to_df(self.df_to_use)
        assert_frame_equal(expected_df, actual_df)

    def test_rubbish_is_correctly_inserted_in_df(self):
        expected_df = pd.DataFrame(
            {'COLUMNA1': {0: 'VALOR1', 1: 'VALOR2', 2: 'VALOR3', 3: 'VALOR4', 4: ' ', 5: 'VALOR6'},
             'COLUMNA2': {0: ' ', 1: 'VALOR2', 2: 'VALOR3', 3: 'VALOR4', 4: 'VALOR5', 5: 'VALOR6'},
             'COLUMNA3': {0: 'VALOR1', 1: 'VALOR2', 2: 'VALOR3', 3: 'VALOR4', 4: 'VALOR5', 5: 'VALOR6'}}
        )
        actual_df = self.dummy.insert_rubbish_to_df(self.df_to_use)
        assert_frame_equal(expected_df, actual_df)

    def test_columns_to_display_selected_correctly(self):
        self.dummy.columns_to_display = {'COL1': 'COLUMNA1', 'COL2': 'COLUMNA2'}
        expected_df = pd.DataFrame(
            {'COLUMNA1': ['VALOR1', 'VALOR2', 'VALOR3', 'VALOR4', 'VALOR5', 'VALOR6'],
             'COLUMNA2': ['VALOR1', 'VALOR2', 'VALOR3', 'VALOR4', 'VALOR5', 'VALOR6']}
        )
        actual_df = self.dummy.select_columns_to_display(self.df_to_use)
        assert_frame_equal(expected_df, actual_df)

    def test_column_names_changed_raises_error_if_incorrect_number_of_elements_in_input_dictionary(self):
        self.dummy.columns_to_display = {'COL1': 'COLUMNA1', 'COL2': 'COLUMNA2'}
        with self.assertRaises(ValueError):
            self.dummy.change_column_names(self.df_to_use)

    def test_column_names_correctly_changed_if_correct_input(self):
        self.dummy.columns_to_display = {'COL1': 'COLUMNA1', 'COL2': 'COLUMNA2', 'COL3': 'COLUMNA3'}
        expected_df = pd.DataFrame(
            {'COL1': ['VALOR1', 'VALOR2', 'VALOR3', 'VALOR4', 'VALOR5', 'VALOR6'],
             'COL2': ['VALOR1', 'VALOR2', 'VALOR3', 'VALOR4', 'VALOR5', 'VALOR6'],
             'COL3': ['VALOR1', 'VALOR2', 'VALOR3', 'VALOR4', 'VALOR5', 'VALOR6']}
        )
        actual_df = self.dummy.change_column_names(self.df_to_use)
        assert_frame_equal(expected_df, actual_df)


if __name__ == '__main__':
    unittest.main()
