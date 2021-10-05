import json
import csv

with open('covid_cases.json','r') as json_file:
    Ourjson = json.load(json_file)

Covid_Data = Ourjson['records']
Data_File = open('Data_File.csv','w')
csv_w = csv.writer(Data_File)

#Count
c = 0
for r in Covid_Data:
    if c == 0:
        header = r.keys()
        csv_w.writerow(header)
        c += 1
    csv_w.writerow(r.values())
Data_File.close()