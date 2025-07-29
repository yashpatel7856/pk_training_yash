
# start time : 3:50
#  end time :  5:05
def makeArrangment(groupSize,swordHolder=1):
    tempGroupList=[x for x in range(1,groupSize+1)]
    tempList=[]
    count=0
 
    while True:
        if len(tempGroupList)==1:
            return tempGroupList[0]
        tempList=tempGroupList[swordHolder+1:]+tempGroupList[0:swordHolder]
        swordHolder=1
        tempGroupList=tempList
        

print(makeArrangment(8,3))