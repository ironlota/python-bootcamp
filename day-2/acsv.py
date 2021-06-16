# import csv

import pandas as pd

dataframe = pd.read_csv('adb.csv', delimiter=';')

print(dataframe.head())

# print(dataframe.describe())

# with open('adb.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=';')
#     for row in csv_reader:
#         print(row)