import random
with open("members.txt") as f:
    textFile = f.readlines()
dataMaster = [_.strip() for _ in textFile]
latecomers = []
data1 = dataMaster.copy()
data2 = dataMaster.copy()
session1 = []
session2 = []
pair = []

def getTotalGroups(dataSet):
    membersCount = len(dataSet)
    groupSize = 2
    totalGroups = membersCount // groupSize
    return totalGroups

def getOddMember(dataSet):
    if len(dataSet) == 0:
        print("\nThere are an even number of members :)")
    else:
        print("\nUh oh! " + dataSet.pop(0) + " is all alone :(")

def selectRandomMember(dataSet):
    return random.randint(0, (len(dataSet) - 1))

for _ in range(getTotalGroups(data1)):
    session1.append([data1.pop(0), data1.pop(selectRandomMember(data1))])

print("Session 1:")
count = 0
for line in session1:
    count += 1
    print(str(count) + ". ", end='')
    print(line[0] + " and " + line[1])
getOddMember(data1)

print("\nAdd latecomers, separated by line. Enter 0 once finished.")

while True:
    entry = input(" > ")
    if entry == "0":
        break
    else:
        latecomers.append(entry)
    
data2 += latecomers

for _ in range(getTotalGroups(data2)):
    left = data2.pop(0)
    while True:
        randomIndex = selectRandomMember(data2)
        pair = [left, data2[randomIndex]]
        pairInverted = [data2[randomIndex], left]
        if (pair not in session1) and (pairInverted not in session2):
            session2.append([left, data2.pop(randomIndex)])
            break;
        else:
            continue;

print("\nSession 2:")
count = 0
for line in session2:
    count += 1
    print(str(count) + ". ", end='')
    print(line[0] + " and " + line[1])
getOddMember(data2)
