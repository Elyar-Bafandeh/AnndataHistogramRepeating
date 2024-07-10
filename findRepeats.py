import pandas as pd
def findRepeats(fileDir):
    df = pd.read_csv(fileDir, sep='\t', header=None)
    grouped = df.groupby(3)
    repeatsList = list(grouped.size())
    return list(filter(lambda n : n > 1 , repeatsList))

def createRepeatsDict(repeatsList):
    repeats_dict = {i:0 for i in range(2,max(repeatsList)+1)}
    for repeats in repeats_dict.keys():
        repeats_dict[repeats] = repeatsList.count(repeats)
    return repeats_dict

    
