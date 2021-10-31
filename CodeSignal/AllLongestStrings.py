def allLongestStrings(inputArray):
    result = []
    maxlen = 0
    
    for i in inputArray:
        if maxlen < len(i):
            maxlen = len(i)
    
    for j in inputArray:
        if len(j) == maxlen:
            result.append(j)
            
    return result
