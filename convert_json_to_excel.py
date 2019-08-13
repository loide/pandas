import json
import pandas as pd
from pandas import DataFrame

FILENAME = "ex1.json"

def main():
	with open(FILENAME, 'r') as myfile:
		data = myfile.read()

	# parse file
	obj = json.loads(data)

	# filter only xpto tag
	acc = obj['xpto']

	df = DataFrame(acc)

	# export to a excel file
	export_xls = df.to_excel(r"output.xlsx", index=None, header=True)

if __name__ == "__main__":
	main()
