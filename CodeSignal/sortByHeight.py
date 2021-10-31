def sortByHeight(a):
    b = [i for i in sorted(a) if i != -1]
    j = 0
    
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = b[j]
            j += 1
            
    
    return a
