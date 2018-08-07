import pandas as pd
import requests



def make_request(url):
	"""
	:param url: url which holds the data to be retrieved
	:return: JSON format data
	"""
	params = None
	resp = requests.get(url=url, params=params)
	data = resp.json()
	return data



def json_to_df(json_obj):
	"""
	:param json_obj: the data to be converted to a pandas dataframe:
	:return: pandas dataframe
	"""
	json_data = json_obj['data']
	columns = []
	for col in json_obj['meta']['view']['columns']:
		columns.append(col['name'])
	df = pd.DataFrame(data=json_data, columns=columns)
	return df



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
	
	url = 'https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json'

	json_obj = make_request(url)
	df = json_to_df(json_obj)

	# print all column headings
	print_dataframe(df, True, False)

	# print all entries
	# print_dataframe(df, False, True)