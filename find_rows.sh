#!/bin/bash
file="book.xls"
column="id"
values="1,y"
rows=$(python3 find_rows.py $file $column $values)
echo $rows
