# Merging Two Dataframes

import pandas as pd



def clean_df(df):
	"""
	This function applies activity 2's cleaning process to the given df
	:param dataframe: the dataframe to be cleaned
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

def merge_dfs(df1, df2, join_type, df1_key, df2_key):
	"""
	This function merges two dataframes given specific constraints
	:param df1: the first dataframe
	:param df2: the second dataframe
	:param join_type: 'left', 'right', 'outer' or 'inner' type of join
	:param df1_key: the key of df1 to join on
	:param df2:key: the key of df2 to join on
	"""
	merged_df = pd.merge(df1, df2, how=join_type, left_on=[df1_key], right_on=[df2_key])
	return merged_df


if __name__ == '__main__':
	books_df = pd.read_csv("dataset.csv")
	city_df = pd.read_csv("city_country.csv")

	books_df = clean_df(books_df)
	books_df = replace_col_spaces(books_df)


	merged_df = merge_dfs(books_df,city_df,'left','Place_of_Publication','City')

	country_distribution = merged_df.groupby(['Country'], as_index=False)['City'].count()

	print (country_distribution)





