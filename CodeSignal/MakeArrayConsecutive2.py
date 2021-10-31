def makeArrayConsecutive2(statues):
    mins = min(statues)
    maxs = max(statues)
    list = []
    for i in range(mins, maxs):
        if i not in statues:
            list.append(i)
    return len(list)

