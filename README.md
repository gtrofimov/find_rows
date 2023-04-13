# Find Rows in Excel
As a test automtion engineer I may have tests that are parameterized to a data source like an Excel spreadsheet. I may then use column like "ids" to only run a subset of the data source based on the values in teh column.
The following example shows how we can use python to get the exact rows numbers in an excel file and run only a subset of data rows.

The example uses the `pandas` and `argparse` libraries

```python
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

# Print the row numbers as a comma-separated list
print(f'{",".join([str(x) for x in matches])}')
```

To run this script use:
```sh
python find_rows.py /path/to/excel/file.xlsx column_name value1,value2,value3
```

or as a shell script:
```sh
#!/bin/bash
file="book.xls"
column="id"
values="1,y"
rows=$(python3 find_rows.py $file $column $values)
echo $rows
```

This can be used in conjunction with `soatestcli -dataSourceRow $rows`