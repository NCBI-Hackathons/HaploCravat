#!/usr/bin/env python3

import sqlite3
import sys

columns = [
	['col1','text'],
	['col2','integer'],
	['col3','real']
]

table_name = 'table1'

col_toks = [' '.join([cname,ctype]) for cname,ctype in columns]
create_stmt = 'create table {tname} ({cols});'.format(
	tname = table_name,
	cols = ', '.join(col_toks)
)
print(create_stmt)
insert_template = 'insert into {tname} ({cols}) values ({vals});'.format(
	tname = table_name,
	cols = ', '.join([x[0] for x in columns]),
	vals = ', '.join(['?']*len(columns))
)
print(insert_template)

fpath = sys.argv[1]
dbpath = sys.argv[2]
with open(fpath) as f, sqlite3.connect(dbpath) as dbconn:
	cursor = dbconn.cursor()
	cursor.execute('pragma synchronous=0;')
	cursor.execute('pragma journal_mode=memory;')
	cursor.execute(create_stmt)
	for l in f:
		toks = l.strip('\r\n').split('\t')
		print(toks)
		cursor.execute(insert_template, toks)
	dbconn.commit()
	cursor.execute('pragma synchronous=1;')
	cursor.execute('pragma journal_mode=delete;')
		
