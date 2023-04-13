import pandas as pd
import argparse

# Set up the command line argument parser
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='The path to the Excel file.')
parser.add_argument('column', type=str, help='The name of the column to search.')
parser.add_argument('values', type=str, help='A comma-separated list of values to search for.')

# Parse the command line arguments
args = parser.parse_args()

# Load the Excel file into a Pandas dataframe
df = pd.read_excel(args.file, index_col=None, header=0)

# Convert the values to a list of strings
values = args.values.split(',')

# Find the row numbers where the column matches the provided values
matches = df[df[args.column].astype(str).isin(values)].index.tolist()

# Adjust the row numbers to match Excel row numbers
matches = [x+1 for x in matches]

# Print the complete Pandas dataframe
# print(df)

# Print the row numbers as a comma-separated list
#print(f'\nRows where "{args.column}" matches: {",".join([str(x) for x in matches])}')
print(f'{",".join([str(x) for x in matches])}')