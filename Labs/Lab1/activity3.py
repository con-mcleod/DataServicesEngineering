import pandas as pd
from pymongo import MongoClient
import json



def read_csv(csv_file):
	"""
	:param csv_file: the path of the csv file
	:return: A dataframe to represent csv data
	"""
	return pd.read_csv(csv_file)



def write_in_mongodb(df, mongo_host, mongo_port, db_name, collection):
	"""
	:param df: pandas dataframe to be stored
	:param mongo_host: mongodb server address
	:param mongo_port: mongodb server port number
	:param db_name: name of the database
	:param collection: name of the collection inside database
	"""
	client = MongoClient(host=mongo_host, port=mongo_port)
	db = client[db_name]
	c = db[collection]
	records = json.loads(df.T.to_json()).values()
	c.insert(records)



def read_from_mongodb(mongo_host, mongo_port, db_name, collection):
	"""
	:param mongo_host: mongodb server address
	:param mongo_port: mongodb server port number
	:param db_name: name of the database
	:param collection: name of the collection inside the database
	"""
	client = MongoClient(host=mongo_host, port=mongo_port)
	db = client[db_name]
	c = db[collection]
	return pd.DataFrame(list(c.find()))



def print_dataframe(dataframe, print_column, print_rows):
	"""
	:param dataframe: pandas dataframe to be printed
	:param print_column: True if columns to be printed
	:param print_rows: True is rows to be printed
	"""
	if print_column:
		print(",".join([col for col in dataframe]))
	if print_rows:
		for index, row in dataframe.iterrows():
			print(",".join([str(row[col]) for col in dataframe]))



if __name__ == '__main__':
	
	db_name = 'comp9321'
	mongo_port = 27017
	mongo_host = 'localhost'
	csv_file = 'ZipCode_dataset.csv'
	df = read_csv(csv_file)
	collection = 'Demographic_Statistics'

	# replace spaces in headings with underscores
	df.columns = [col.replace(' ', '_') for col in df.columns]

	print ("Writing into the mongodb")
	write_in_mongodb(df, mongo_host, mongo_port, db_name, collection)

	print ("Querying the database")
	df = read_from_mongodb(mongo_host, mongo_port, db_name, collection)

	# print all column headings
	print_dataframe(df, True, False)

	# print all entries
	print_dataframe(df, False, True)