import os
import csv

# csvpath = os.path.join('.', 'Resources', 'election_data.csv')

csvpath = 'election_data.csv'

Candidate = {}

#read with CSV file
with open(csvpath, newline='') as csvfile:
   
    # split data by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # data = list(csvreader)
    # totalVotes = len(data)
    
    for row in csvreader:
        Candidate[row[2]] = Candidate.get(row[2], 0) + 1

    
# print("Total Votes:" + str(totalVotes))      
 
  # for row in csvreader:
  #      print(row) pull the file

voteKey = list(Candidate.keys())
#print(voteKey)
voteCount = list(Candidate.values())
#print(voteCount)

sum = 0
for num in voteCount:
    sum = sum +num
#print(sum)

print("Total Votes:" + str(sum))

khanDecimal = ((voteCount[0])/(sum))
# print "{0:.0%}".format(khanDecimal)
khanPercent = khanDecimal*100
# print(khanPercent)

correyDecimal = ((voteCount[1])/(sum))
correyPercent = correyDecimal*100
liDecimal = ((voteCount[2])/(sum))
liPercent = liDecimal*100
otDecimal = ((voteCount[3])/(sum))
otPercent = otDecimal*100
#print(khanDecimal)


print(voteKey[0], khanPercent, voteCount[0])
print(voteKey[1], correyPercent, voteCount[1])
print(voteKey[2], liPercent, voteCount[2])
print(voteKey[3], otPercent, voteCount[3])



maxValue = max(Candidate.values()) 
maxKeys = [k for k, v in Candidate.items() if v == maxValue] 
print("Winner:" + " " + str(maxKeys))
