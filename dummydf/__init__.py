from dummydf.dummydf import DummyDataframe

test_df = DummyDataframe(randomise=False).df
test_df_random = DummyDataframe(randomise=True).df

print('Welcome to dummydf')
