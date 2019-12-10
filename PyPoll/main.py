import os
import csv

csvpath = 'election_data.csv'

Candidate = {}
voteKey = list(Candidate.keys())
voteCount = list(Candidate.values())

#read with CSV file
with open(csvpath, newline='') as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',')  # split data by commas
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # data = list(csvreader)
    # totalVotes = len(data)
    
    for row in csvreader:
        Candidate[row[2]] = Candidate.get(row[2], 0) + 1

    voteKey = list(Candidate.keys())
    voteCount = list(Candidate.values())    
    sum = 0
    for num in voteCount:
        sum = sum + num


    # print("Total Votes:" + str(sum))

    khanDecimal = ((voteCount[0])/(sum)*100)
    khanPercent = str('{:,.2f}'.format(khanDecimal))
    correyDecimal = ((voteCount[1])/(sum)*100)
    correyPercent = str('{:,.2f}'.format(correyDecimal))
    liDecimal = ((voteCount[2])/(sum)*100)
    liPercent = str('{:,.2f}'.format(liDecimal))
    otDecimal = ((voteCount[3])/(sum)*100)
    otPercent = str('{:,.2f}'.format(otDecimal))

    # print(voteKey[0], khanPercent + "%", voteCount[0])
    # print(voteKey[1], correyPercent + "%", voteCount[1])
    # print(voteKey[2], liPercent + "%", voteCount[2])
    # print(voteKey[3], otPercent + "%", voteCount[3])



    maxValue = max(Candidate.values()) 
    maxKeys = [k for k, v in Candidate.items() if v == maxValue] 
    # print("Winner:" + " " + str(maxKeys))



text_file = open("PyPoll_output_PBL.txt", "w") # create text file in same folder as main.py, assign variable to path
print('Election Results')
text_file.write('Election Results')
print('-------------------------')
text_file.write('-------------------------')
print("Total Votes:" + str(sum))
text_file.write("Total Votes:" + str(sum))
print('-------------------------')
text_file.write('-------------------------')
print(voteKey[0], khanPercent + "%", voteCount[0])
text_file.write(khanPercent + "%")
print('-------------------------')
text_file.write('-------------------------')
print(voteKey[1], correyPercent + "%", voteCount[1])
text_file.write(voteKey[1])
text_file.write(correyPercent + "%")
print('-------------------------')
text_file.write('-------------------------')
print(voteKey[2], liPercent + "%", voteCount[2])
text_file.write(voteKey[2])
text_file.write(liPercent + "%")
print('-------------------------')
text_file.write('-------------------------')
print(voteKey[3], otPercent + "%", voteCount[3])
text_file.write(voteKey[3])
text_file.write(otPercent + "%")
print('-------------------------')
text_file.write('-------------------------')
print("Winner:" + " " + str(maxKeys))
text_file.write("Winner:" + " " + str(maxKeys))
print('-------------------------')
text_file.write('-------------------------')
text_file.close() # if you open it, close it