# Cleaning columns

import pandas as pd


if __name__ == '__main__':
	df = pd.read_csv("dataset.csv")

	print (df['Place of Publication'])
	print ("\nChanging London typos and dashes to spaces:\n\n")
	df['Place of Publication'] = df['Place of Publication'].apply(
		lambda x: 'London' if 'London' in x else x.replace('-', ' ')
	)
	print (df['Place of Publication'])

	print (df['Date of Publication'])
	print ("\nRemoving all but first four digits:\n\n")
	df['Date of Publication'] = df['Date of Publication'].apply(
		lambda x: float(str(x)[0:4])
	)
	print (df['Date of Publication'])

	print ("\nChanging NaN values to 0\n\n")
	df['Date of Publication'] = df['Date of Publication'].fillna(0)
	print (df['Date of Publication'])

	