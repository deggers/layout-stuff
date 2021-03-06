import json
import operator
import string

chars = string.ascii_lowercase[:26]

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
            print(f'{key}: {trigrams[key]:.20f} ')


    for key, value in data['bigrams'].items():
        share = (value/totalBigrams) * 100
        sortedCol = "".join(sorted(key))
        if sortedCol in bigrams:
            bigrams[sortedCol] = bigrams[sortedCol] + share

    sbigrams = sorted(bigrams.items(), key=lambda x: x[1], reverse=True)
#    for key, value in sbigrams:      
#     print(f'{key}: {value:.2f} ', end='\n')

