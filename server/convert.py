import pandas as pd
import json

trans = json.load(open('transactions.json'))
keys = [item[0] for item in trans[0].items()]
keys = (",").join(keys)

lines = [f'insert into transactions ({keys}) values ({str([item[1] for item in row.items()]).split("[")[1].split("]")[0]})' for row in trans]
f = open("trans.sql", "w")
for line in lines:

	f.write(line+';\n')
f.close()
