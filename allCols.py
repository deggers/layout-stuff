import json
import operator
import string

chars = string.ascii_lowercase[:26]

with open('data.json') as json_file:
    data = json.load(json_file)

    # Create empty dict with all possible cols 
    trigrams = {}
    for firstChar in chars:
        for secondChar in chars:
            if firstChar == secondChar:
                continue 
            for thirdChar in chars:
                if secondChar == thirdChar or firstChar == thirdChar:
                    continue
                trigram = f'{firstChar}{secondChar}{thirdChar}'
                sortedCol = "".join(sorted(trigram))
                if sortedCol not in trigrams:
                    trigrams[sortedCol] = 0.00
    
    # calculate total of all trigrams
    total = 0
    for _,value in data['trigrams'].items():
       total = total + value

    # FIll empty dict with found values 
    for key,value in data['trigrams'].items():
        share = (value/total) * 100
        sortedCol = "".join(sorted(key))
        if sortedCol in trigrams:
            sortedCol = "".join(sorted(key))
            trigrams[sortedCol] = trigrams[sortedCol] + share
        else:
            print(f'Col: {sortedCol} not found')
    for key in trigrams:      
        if (trigrams[key] == 0):
            print(f'{key}: {trigrams[key]:.20f} ', end='\n')

