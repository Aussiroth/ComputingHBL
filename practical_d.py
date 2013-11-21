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

#binary search, with slight adaptation
def binarysearch(score, pscore, low, high):
    #if the two are equal, see if the new score should be inserted before or after the current valie
    #being looked at
    if low>high:
        low=high
    if high==low:
        if score>pscore[low][1]:
            return low
        else:
            return low+1
    else:
        #else, half search space
        mid = (low+high)//2
        if score>pscore[mid][1]:
            return binarysearch(score, pscore, low, mid-1)
        else:
            return binarysearch(score, pscore, mid+1, high)
        
                
def insert_player(username, score, pscore):
    #find location to insert
    location = binarysearch(score, pscore, 0, len(pscore)-1)
    #shift all later array values back
    pscore[location+1:]=pscore[location:]
    #then add the new value in.
    #if the values were moved, insert into the old location space
    try:
        pscore[location] = [username, score]
    #if they weren't, append it at the back since smallest value
    except:
        pscore.append([username, score])
    #sort by username in case
    start=location
    end = start
    #get start counting back from location inserted
    while start>=0:
        if pscore[start][1]!=score:
            start=start+1
            break
        else:
            start-=1
    #get end counting forward from location inserted
    while end<len(pscore):
        if pscore[end][1]!=score:
            break
        else:
            end+=1
    pscore[start:end]=quicksort_name(pscore[start:end])
    return pscore
    

#random data generation
def populate(pscore):
    #only 7 to easily see insertion
    for i in range(0, 7):
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
#insert new player
pscore = insert_player('Derp', 5000, pscore)
print(pscore)
pscore = insert_player('Alvin', 5000, pscore)
print(pscore)

