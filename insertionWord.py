'''
Created on 03-Sep-2018

@author: DELL
'''

while 1:

    with open("stopWords.txt","r") as f:
        file = open("stopWords.txt","a")
        word = str(input("Enter Word : "))
        contents = f.read().split('\n')
        
        if word in contents:
            print("Word is there")
        else:
            file.write("{}\n".format(word))
            print("Inserted")
