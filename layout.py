import json
import operator
import string

chars = string.ascii_lowercase[:26]
allCols = []

with open('data.json') as json_file:
    data = json.load(json_file)

    # Create empty trigram dict with all possible cols 
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
    

    # Create empty bigram dict with all possible cols 
    bigrams = {}
    for firstChar in chars:
        for secondChar in chars:
            if firstChar == secondChar:
                continue 
            else:
                bigram = f'{firstChar}{secondChar}'
                sortedCol = "".join(sorted(bigram))
                if sortedCol not in bigrams:
                    bigrams[sortedCol] = 0.00



    # calculate total of all trigrams
    totalTrigrams = 0
    for _,value in data['trigrams'].items():
       totalTrigrams = totalTrigrams + value
    print(totalTrigrams)

    # calculate total of all bigrams
    totalBigrams = 0
    for _,value in data['bigrams'].items():
       totalBigrams = totalBigrams + value



    # FIll empty dict with found values 
    for key,value in data['trigrams'].items():
        share = (value/totalTrigrams) * 100
        sortedCol = "".join(sorted(key))
        if sortedCol in trigrams:
            trigrams[sortedCol] = trigrams[sortedCol] + share

    for key in trigrams:      
        if (trigrams[key] == 0):
            if frozenset(tuple(key)) not in allCols:
                allCols.append(tuple(key))

    for key, value in data['bigrams'].items():
        share = (value/totalBigrams) * 100
        sortedCol = "".join(sorted(key))
        if sortedCol in bigrams:
            bigrams[sortedCol] = bigrams[sortedCol] + share

    sbigrams = sorted(bigrams.items(), key=lambda x: x[1], reverse=True)

    
    for key, value in sbigrams:
        allCols.append(tuple(key))

layouts = []
for col1 in allCols:
    for col2 in allCols[1:]:
        for col3 in allCols[2:]: 
            for col4 in allCols[3:]:
                for col5 in allCols[4:]:
                    for col6 in allCols[5:]:
                        doubles = set(col1).intersection(set(col2)).intersection(set(col3)).intersection(set(col4)).intersection(set(col5)).intersection(set(col6))
                        print(doubles)
                        if len(doubles) > 0:
                            continue
                        candidate = {col1,col2,col3,col4,col5,col6}     
        if frozenset(candidate) not in layouts and len(candidate) ==6:
            layouts.append(candidate)
            print(candidate)
