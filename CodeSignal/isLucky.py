def isLucky(n):
    m = str(n)
    fhalf = shalf = 0
    
    for i in range(len(m)//2):
        fhalf += int(m[i])
    for i in range(len(m)//2, len(m)):
        shalf += int(m[i])
    return True if fhalf == shalf else False
