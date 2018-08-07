# Filtering rows

import pandas as pd

def clean_df(df):
	"""
	This function applies activity 2's cleaning process to the given df
	:param df: the dataframe to be cleaned
	:return: cleaned dataframe
	"""
	df['Place of Publication'] = df['Place of Publication'].apply(
		lambda x: 'London' if 'London' in x else x.replace('-', ' ')
	)
	df['Date of Publication'] = df['Date of Publication'].apply(
		lambda x: float(str(x)[0:4])
	)
	df['Date of Publication'] = df['Date of Publication'].fillna(0)
	return df

def replace_col_spaces(dataframe):
	"""
	This function replaces all spaces in column headings with underscores
	:param dataframe: the dataframe to be altered
	:return: altered dataframe
	"""
	dataframe.columns = [c.replace(' ', '_') for c in dataframe.columns]
	return dataframe

def query_df(dataframe, query):
	"""
	This function applies the given query to the dataframe and returns the result
	:param dataframe: the dataframe to be queried
	:param query: the query to be made of the dataframe
	:return: result of query
	"""
	query_result = dataframe.query(query)
	return query_result

if __name__ == '__main__':

	df = pd.read_csv("dataset.csv")

	df = clean_df(df)

	print (df.columns)
	print ("\nReplace spaces in column headings with underscores\n\n")
	df = replace_col_spaces(df)
	print (df.columns)

	query_result = query_df(df, 'Place_of_Publication == "London" and Date_of_Publication > 1886')
	print (query_result)