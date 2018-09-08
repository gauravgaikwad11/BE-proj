'''
Created on 26-Aug-2018

@author: DELL
'''

import json
import re 
from stemming.porter2 import stem
#from collections import Counter


names = []
data = []
words = ['to','the','|']
topics = []
try :
    with open('jsonFile.json', encoding = 'utf-8') as f:
        data = json.loads(f.read())
        #c = Counter(k[4:] for d in data for k, v in d.items() if k.startswith('has_') and v)
        #for line in f:
            #data.append(json.loads(line))
    #print(len(data))
    
    
    
    for i in range(0,len(data)):
        names.append(data[i]['Tweet Text'].encode())
        
        #print(data[i]['Full Name'])
    #print(names)
    
    
    stop_words = ['to','her','a','an','the','how','what','when','am','is','are','was','where','all','anybody','for','and','on','of']
    #preposition = re.compile()
    #for i in names:
    #    print(i)
    #print(words.__contains__('|'))
    for i in range(0,len(names)):
        names[i] = names[i].decode()
        names[i] = re.sub(r"http\S+","",names[i])
        #names[i] = re.sub(preposition," ",names[i])
        words = names[i].split(' ')
        for word in words:
            if word in stop_words:
                names[i] = re.sub(" {} ".format(word)," ",names[i])
            word = stem(word)
            #elif word[0] == '#':
                #print(word)
                #topics.append(word[1:])
            #   pass
        
    for i in range(0,len(data)):
        data[i]['Tweet Text'] = names[i]
    ''' 
    print(names[1])
    words = names[1].split(' ')
    for word in words:
        if word in stop_words:
            print(word)
            
    '''
        
    #for i in range(0,len(data)):
    #    print(data[i]['Tweet Text'])
    #for i in names:
    #    print(i)
    with open("jsonFile1.json","w") as f:
        json.dump(data, f)
    
    
    
except Exception as e:
    print(e)
