'''
Created on 25-Aug-2018

@author: DELL
'''
import csv
import json

csvFile = open("Swachh.csv", "r", encoding='utf-8')
jsonFile = open("jsonFile.json ", "w")

fieldNames = ('Date', 'Screen Name', 'Full Name', 'Tweet Text')

reader = csv.DictReader(csvFile, fieldNames)
jsonFile.write('[')
for row in reader:
    if reader.line_num == 1:
        continue
    elif reader.line_num == 2:
        json.dump(row, jsonFile)
    else:
        jsonFile.write(',\n')
        json.dump(row, jsonFile)

jsonFile.write(']')
print("successful")

