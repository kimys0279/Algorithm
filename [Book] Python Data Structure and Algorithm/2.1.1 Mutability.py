myList = [1, 2, 3, 4]
newList = myList[:]
newList2 = list(myList)

people = {"버피", "에인절", "자일스"}
slayers = people.copy()
slayers.discard("자일스")
slayers.remove("에인절")

myDict = {"안녕", "세상"}
newDict = myDict.copy()

import copy
myObj = "다른 어떤 객체"
newObj = copy.copy(myObj)
newObj2 = copy.deepcopy(myObj2)
