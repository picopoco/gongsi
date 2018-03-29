import csv
import json
import pandas as pd
csvfile = open ('output_last.csv','r')
reader = csv.DictReader(csvfile)
result = []
for row in reader:
    result.append(row)
result = json.dumps(result)
result = json.loads(result)
keys = ('Entity' ,'Year','SO2 emissions- Clio Infra')
keys = ('company_code', 'company_name', 'url', '구분', '이전_분기', '이전_분기_누적', '최근_분기', '최근_분기_누적')

print(result)