import random

#do quicksort on entire array to sort by score
def quicksort_score(pscore):
    if len(pscore)<=1:
        return pscore
    pivot = pscore[0]
    less = []
    great = []
    for i in range(1,len(pscore)):
        if pscore[i][1]<pivot[1]:
            less.append(pscore[i])
        else:
            great.append(pscore[i])
    return quicksort_score(great) + [pivot] + quicksort_score(less)

#do quicksort on the portion of array given for username
def quicksort_name(pscore):
    if len(pscore)<=1:
        return pscore
    pivot = pscore[0]
    less = []
    great = []
    for i in range(1, len(pscore)):
        if pscore[i][0]<pivot[0]:
            less.append(pscore[i])
        else:
            great.append(pscore[i])
    return quicksort_name(less) + [pivot] + quicksort_name(great)

#random data generation
def populate(pscore):
    for i in range(0, 5000):
        #random generation of score
        score = random.randint(0, 99999)
        #randomly generates how long the username should be
        user_length = random.randint(1, 10)
        username = ""
        for j in range(0, user_length):
            #randomly picks a integer
            char = random.randint(0, 61)
            #if its between 10-35, convert to ascii lowercase
            if char>9 and char<36:
                char = chr(char+55)
            #if its between 36 and 61, convert to ascii uppercase
            elif char>=36:
                char = chr(char+61)
            #if its a number just add it in
            username+=str(char)
        pscore.append([username, score])
    return pscore

#main
pscore = []

#populate pscore with random data
pscore = populate(pscore)

#sort first by score
pscore = quicksort_score(pscore)

start=0
end=0

#scan through array to take all sub-lists of players with same score
while end<len(pscore):
    #if its a tie, move the end counter to consider next one
    if pscore[start][1]==pscore[end][1]:
        end+=1
    #if not, send the sublist for sorting
    elif pscore[start][1]>pscore[end][1]:
        pscore[start:end]=quicksort_name(pscore[start:end])
        start=end
        end+=1
    #additional case to sort for ties in the lowest score of leaderboard
    if end==len(pscore)-1:
        pscore[start:] = quicksort_name(pscore[start:])
        break

print(pscore)

