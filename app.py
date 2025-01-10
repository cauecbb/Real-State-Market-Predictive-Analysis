import pandas as pd

dataframe = pd.read_csv('data/ZHVI-dataset.csv')

dataframe_ny = dataframe[dataframe['StateName'] == 'NY']

print(dataframe_ny.isnull().sum())

dataframe_ny = dataframe_ny.dropna()

dataframe_ny.to_csv('data/ZHVI-NY-dataset.csv', index= False)