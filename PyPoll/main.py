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
    # print("Total Votes:" + str(totalVotes))



    #Candidate = data[row[2]]
    
    for row in csvreader:
        # if row[2] not in Candidate:
        # Candidate.append(int[row[2]]
        
       
        Candidate[row[2]] = Candidate.get(row[2], 0) + 1

        # print(row[2])


# dictionary[key] = dictionary.get(key, default_value)

# candidate_votes =  dictionary.get(key, default_value)
# If the key exists in the dictionary, it will return the key value.
# But if it does not exist, it returns the default value ...
# And if you wanted to add something to the key value ....
# remember, to add a new key/value pair to a dictionary, you just type dictionary[key] = value.

    # for i in range(len(data)):
    #         #print(data[i][1])

    #         Candidate(int(data[i][2]))

    #     print(Candidate)
           
 
  # for row in csvreader:
  #      print(row) pull the file

vote_key = list(Candidate.keys())
vote_count = list(Candidate.values())
print(vote_key)
print(vote_count)

reverse_dict = dict(zip(vote_count, vote_key))
print (reverse_dict)

