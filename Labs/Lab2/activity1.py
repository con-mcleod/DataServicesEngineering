# Dropping columns

import pandas as pd

def read_csv(csv_file):
	"""
	:param csv_file: the file to be read into a dataframe
	:return: the Pandas dataframe
	"""
	df = pd.read_csv(csv_file)
	return df

def check_NaN(dataframe):
	"""
	:param dataframe: the dataframe to be checked for NaN values
	:return: list of NaN values in each column
	"""
	NaN_values = dataframe.isnull().sum()
	return NaN_values

def drop_columns(dataframe, columns_to_drop):
	"""
	:param dataframe: the dataframe to drop columns from
	:param columns_to_drop: the columns to be removed from the dataframe
	:return: the updated dataframe
	"""
	df = dataframe.drop(columns=columns_to_drop)
	return df

def print_df(dataframe, print_cols=True, print_rows=True):
	"""
	:param dataframe: the dataframe to be printed
	:param print_cols: if true print columns
	:param print_rows: if true print rows
	"""
	if print_cols:
		print(",".join([column for column in dataframe]))
	if print_rows:
		for index, row in dataframe.iterrows():
			print(",".join([str(row[column]) for column in dataframe]))


if __name__ == '__main__':

	df = read_csv("dataset.csv")

	NaN_values = check_NaN(df)
	print (NaN_values)

	columns_to_drop = ['Edition Statement',
						'Corporate Author',
						'Corporate Contributors',
						'Former owner',
						'Engraver',
						'Contributors',
						'Issuance type',
						'Shelfmarks']

	df = drop_columns(df, columns_to_drop)

	# print the column headings
	print_df(df, print_rows=False)

	# print the rows of data
	# print_df(df, print_cols=False)