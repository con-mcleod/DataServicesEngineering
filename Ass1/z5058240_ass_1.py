"""
COMP9321
Assignment 1
Author: Connor McLeod
zID: z5058240

Note to assessor:
Some key things to look out for:
	- I have removed the "totals" row from the dataframe 
	- I have renamed each team by removing all bracketed strings and all
	 leading/trailing white space
	- I have renamed all of the column headings
	- Removing the 'Rubish' column was a permanent change
	- Removing rows containing a NaN value was a permanent change
	- My matplotlib errors on my OS without the additional line below the import 
		- please remove this line if it bugs out your machine (line 19)
"""

import pandas as pd
import matplotlib as mpl
mpl.use('TkAgg')					# may need to remove this line
import matplotlib.pyplot as plt






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
			

def convert_to_int(df, columns_to_convert):
	"""
	Function to convert specified columns from object datatype to int64 datatype
	:param df: the dataframe to be modified
	:param columns_to_convert: list of columns to be modified
	:return df: the modified dataframe
	"""
	for column in columns_to_convert:
		df[column] = [int(val.replace(',','')) for val in df[column]]
	return df


def question_1(df1, df2):
	"""
	Merge two dataframes and print first five rows of result
	:param df1: the first dataframe
	:param df2: the second dataframe
	:return merged_df: the merged dataframe
	"""
	merged_df = pd.merge(df1, df2, how='left', left_on='Team', right_on='Team')
	# remove the total row
	merged_df = merged_df[:-1]
	# remove unnecessary characters from Team
	merged_df['Team'] = [val.split('(')[0].lstrip().strip() for val in merged_df['Team']]
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
	df = df.drop(columns=columns_to_drop)
	print_df(df,True,True,5)
	return df


def question_4(df):
	"""
	Removes any rows containing NaN values and prints the last 10 rows
	:param df: the dataframe
	:return df: the updated dataframe
	"""
	df = df.dropna()
	df_4 = df.tail(10)
	print_df(df_4,True,True,False)
	return df


def question_5(df):
	"""
	Prints the row which has the team with the highest number of Summer gold medals
	:param df: the dataframe
	"""
	df = df.sort_values('S_Gold', ascending=False)
	print_df(df,True,True,1)


def question_6(df):
	"""
	Prints the row with Team having highest difference in Summer and Winter gold medals
	:param df: the dataframe
	"""
	df['Gold_Difference'] = abs(df['S_Gold'] - df['W_Gold'])
	df = df.sort_values('Gold_Difference', ascending=False)
	print_df(df,True,True,1)


def question_7(df):
	"""
	Prints 10 Team's which have the highest and lowest combined total medals
	:param df: the dataframe
	:return df: returns the reordered dataframe
	"""
	df = df.sort_values('C_Total', ascending=False)
	print_df(df,True,True,5)
	df_7 = df.tail(5)
	print_df(df_7,False,True,False)
	return df


def question_8(df):
	"""
	Plots the Summer/Winter medal split for 10 highest medal winners
	:param df: the dataframe
	"""
	df_8 = df.set_index('Team')
	df_8 = df_8.head(10)

	df_8[['W_Total','S_Total']].plot(kind='barh', stacked=True)
	plt.xlabel('Total Medal Tally')
	plt.ylabel('Country')
	plt.title('Summer/Winter Medal Split for 10 Highest Medal Winners')
	plt.tight_layout()
	plt.show()


def question_9(df):
	"""
	Plots 5 Teams' Winter gold/silver/bronze splits
	:param df: the dataframe
	"""
	
	df_9 = df
	df_9 = df_9.loc[df_9['Team'].isin(['United States','Australia','Great Britain','Japan','New Zealand'])]
	df_9 = df_9.set_index('Team')

	df_9[['W_Gold','W_Silver','W_Bronze']].plot(kind='bar')
	plt.xlabel('Country')
	plt.ylabel('Medal Tally')
	plt.title('Winter Gold/Silver/Bronze Split for 5 Countries')
	plt.tight_layout()
	plt.show()
	plt.show()




if __name__ == '__main__':

	# define the csv files as variables
	csv1 = "Olympics_dataset1.csv"
	csv2 = "Olympics_dataset2.csv"

	# read in the csv files
	df1 = pd.read_csv(csv1, skiprows=1)
	df2 = pd.read_csv(csv2, skiprows=1)

	# rename the columns in df1 and df2
	df1.columns = [
		'Team',
		'Rubbish',
		'Summer_NumGames',
		'S_Gold',
		'S_Silver',
		'S_Bronze',
		'S_Total'
	]
	df2.columns = [
		'Team',
		'Winter_NumGames',
		'W_Gold',
		'W_Silver',
		'W_Bronze',
		'W_Total',
		'Combined_NumGames',
		'C_Gold',
		'C_Silver',
		'C_Bronze',
		'C_Total'
	]

	# Q1
	print ("\n***********")
	print ("Question 1:\n")
	df = question_1(df1, df2)

	# Q2
	print ("\n***********")
	print ("Question 2:\n")
	question_2(df)

	# Q3
	print ("\n***********")
	print ("Question 3:\n")
	df = question_3(df)

	# Q4
	print ("\n***********")
	print ("Question 4:\n")
	df = question_4(df)

	# intermediary step to convert medal tally columns from object to int datatype
	columns_to_convert = [
		'S_Gold',
		'S_Silver',
		'S_Bronze',
		'S_Total',
		'W_Gold',
		'W_Silver',
		'W_Bronze',
		'W_Total',
		'C_Gold',
		'C_Silver',
		'C_Bronze',
		'C_Total'
	]
	df = convert_to_int(df, columns_to_convert)

	# Q5
	print ("\n***********")
	print ("Question 5:\n")
	question_5(df)

	# Q6
	print ("\n***********")
	print ("Question 6:\n")
	question_6(df)

	# Q7
	print ("\n***********")
	print ("Question 7:\n")
	df = question_7(df)

	# Q8
	print ("\n***********")
	print ("Question 8:\n")
	print ("See Matlab figure pop-up")
	question_8(df)

	# Q9
	print ("\n***********")
	print ("Question 9:\n")
	print ("See Matlab figure pop-up")
	question_9(df)

	# end
	print ("\n***********")
	print ("End of Assignment. Thanks!\n")

	

	