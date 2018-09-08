'''
Created on 25-Aug-2018

@author: DELL
'''
import pandas

df = pandas.read_csv("Swachh.csv", header=None, encoding="ISO-8859-1")[[0, 1, 2]]
arr = df.values
print(arr)

