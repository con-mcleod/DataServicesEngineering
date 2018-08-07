import pandas as pd
import numpy as np
import sqlite3 as db

df = pd.read_csv('ZipCode_dataset.csv')

# print the column headings
# print (df.columns)

# seems to be the same as print (df)
# print (df.iterrows)

# replace spaces in headings with underscores
df.columns = [col.replace(' ', '_') for col in df.columns]

# save dataframe to csv file
# df.to_csv('example.csv')

# name database and connect to it
DATABASE = "test.db"
conn = db.connect(DATABASE)

# save dataframe to sqlite file
df.to_sql("lab1", conn, if_exists='replace')