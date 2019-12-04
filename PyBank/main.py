import os
import csv


csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


#read with CSV file
with open(csvpath, newline='') as csvfile:
   
    #split data by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

  
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    data = list(csvreader)
    Total_Months = len(data)
    print("Total Months:" + " " + str(Total_Months))

    pAndL = []
    differences = []
    
    for i in range(len(data)):
            #print(data[i][1])
            #older = data[i+1][1]
            #recent = data[i][1]
            #diff = (int(older)-int(recent))
            #differences.append(diff)
            pAndL.append(int(data[i][1]))
           
      #      if i ==1 and i<85:
     #              differences.append(pAndL[i+1]-pAndL[i])
            
    total = sum(pAndL)
    print("Total:" + " " + str(total))
    #print (differences)

    lastMonth = (data[i][1])
    #print (lastMonth)

    firstMonth = (data[0][1])
    #print (firstMonth)

    avgChange = ((int(lastMonth)-int(firstMonth))/i)
    print("Avg Change:" + "" + str(avgChange))


    #for row in csvreader:
           # print(row) testing to make sure I pulled the file correctly
         
 

    
  
