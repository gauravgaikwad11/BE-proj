'''
Created on 29-Aug-2018

@author: DELL
'''
'''
words = ""
list1 = []
with open('Gaurav.txt','r') as r:
    for line in r:
        print(line)
        words = line
        
        list1.append(words)
        
    print(list1)

'''
file  = open("stopWords.txt","a")

while 1:
    word = str(input("Enter word : "))
    file.write("{}\n".format(word))