"""
COMP9321
Assignment 1
Author: Connor McLeod
zID: z5058240

Note to assessor:
Some key things to look out for:
	- I have removed the "totals" row from the dataframe 
	- I have renamed all of the column headings
	- Removing the 'Rubish' column is a permanent change
	- Removing rows containing a NaN value is a permanent change

"""

import pandas as pd




def merge_dfs(df1, df2, join_type, df1_key, df2_key):
	"""
	Merge two dataframes given specific constraints
	:param df1: the first dataframe
	:param df2: the second dataframe
	:param join_type: 'left', 'right', 'outer' or 'inner' type of join
	:param df1_key: the key of df1 to join on
	:param df2:key: the key of df2 to join on
	"""
	merged_df = pd.merge(df1, df2, how=join_type, left_on=[df1_key], right_on=[df2_key])
	return merged_df

def read_csv(csv_file):
	"""
	Read in the provided csv file to a Pandas dataframe
	:param csv_file: the file to be read into a dataframe
	:return: the Pandas dataframe
	"""
	df = pd.read_csv(csv_file, skiprows=1)

	return df

def print_df(dataframe, print_cols, print_rows, numRows):
	"""
	Print the columns and/or rows of the given dataframe
	:param dataframe: the dataframe of interest
	:param print_cols: a boolean that if true prints the dataframe's columns
	:param print_rows: a boolean that if true prints the dataframe's rows
	:param numRows: a count for how many rows will be printed
	"""
	if print_cols:
		print(",".join([column for column in dataframe]))
	if print_rows:
		if not numRows:
			for index, row in dataframe.iterrows():
				print(",".join([str(row[column]) for column in dataframe]))
		else:
			for index, row in dataframe.iterrows():
				if (numRows > 0):
					print(",".join([str(row[column]) for column in dataframe]))
				else:
					break
				numRows -= 1
				

def drop_columns(dataframe, columns_to_drop):
	"""
	:param dataframe: the dataframe to drop columns from
	:param columns_to_drop: the columns to be removed from the dataframe
	:return: the updated dataframe
	"""
	df = dataframe.drop(columns=columns_to_drop)
	return df








def question_1(df1, df2):
	"""
	Merge two dataframes and print first five rows of result
	:param df1: the first dataframe
	:param df2: the second dataframe
	:return merged_df: the merged dataframe
	"""
	merged_df = merge_dfs(df1, df2, 'left','Team','Team')
	# remove the total row
	merged_df = merged_df[:-1]
	print_df(merged_df,True,True,5)
	return merged_df


def question_2(df):
	"""
	Creates a new dataframe where 'Team' is the index and prints first country
	:param df: the dataframe
	"""
	df_q2 = df.set_index('Team')
	print (df_q2.iloc[0])


def question_3(df):
	"""
	Removes the 'Rubbish' column and prints the first five rows
	:param df: the dataframe
	:return df: the udpated dataframe
	"""
	columns_to_drop = "Rubbish"
	df = drop_columns(df, columns_to_drop)
	print_df(df,True,True,5)
	return df


def question_4(df):
	"""
	Removes any rows containing NaN values and prints the last 10 rows
	:param df: the dataframe
	:return df: the updated dataframe
	"""
	df = df.dropna()
	# temporary dataframe containing the 10 last rows
	df_4 = df.tail(10)
	print_df(df_4,True,True,False)
	return df


def question_5(df):
	# remove commas from summer gold medal tally and convert to integers
	df['S_Gold'] = [int(val.replace(',','')) for val in df['S_Gold']]
	df = df.sort_values('S_Gold', ascending=False)
	print_df(df,True,True,1)


def question_6(df):
	# remove commas from winter gold medal tally and convert to integers
	df['W_Gold'] = [int(val.replace(',','')) for val in df['W_Gold']]
	df['Gold_Difference'] = abs(df['S_Gold'] - df['W_Gold'])
	df = df.sort_values('Gold_Difference', ascending=False)
	print_df(df,True,True,1)


def question_7(df):
	pass


def question_8():
	pass


def question_9():
	pass





if __name__ == '__main__':

	# define the csv files as variables
	csv1 = "Olympics_dataset1.csv"
	csv2 = "Olympics_dataset2.csv"

	# read in the csv files
	df1 = read_csv(csv1)
	df2 = read_csv(csv2)

	# rename the columns in df1 and df2
	df1.columns = ["Team","Rubbish","Summer_NumGames","S_Gold","S_Silver","S_Bronze","S_Total"]
	df2.columns = ["Team","Winter_NumGames","W_Gold","W_Silver","W_Bronze","W_Total",
					"Combined_NumGames","C_Gold","C_Silver","C_Bronze","C_Total"]

	# Q1
	print ("\nQuestion 1:\n")
	df = question_1(df1, df2)

	# Q2 
	print ("\nQuestion 2:\n")
	question_2(df)

	# Q3
	print ("\nQuestion 3:\n")
	df = question_3(df)

	# Q4
	print ("\nQuestion 4:\n")
	df = question_4(df)

	# Q5
	print ("\nQuestion 5:\n")
	question_5(df)

	# Q6
	print ("\nQuestion 6:\n")
	question_6(df)

	# Q7
	print ("\nQuestion 7:\n")
	question_7(df)

	# Q8
	print ("\nQuestion 8:\n")

	# Q9
	print ("\nQuestion 9:\n")

	

	