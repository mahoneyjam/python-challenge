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
    
    diffRange = (len(data))-1
    #print(diffRange)

    for i in range(diffRange):
            #print(data[i][1])
            older = data[i+1][1]
            recent = data[i][1]
            diff = (int(older)-int(recent))
            differences.append(diff)
            pAndL.append(int(data[i][1]))
           
      #      if i ==1 and i<85:
     #              differences.append(pAndL[i+1]-pAndL[i])

    lastMonth = (data[i+1][1])
   # print (lastMonth)

    total = (sum(pAndL) + int(lastMonth))
    print("Total:" + " " + str(total))
    #print (differences)


    firstMonth = (data[0][1])
    #print (firstMonth)

    avgChange = ((int(lastMonth)-int(firstMonth))/(i+1))
    print("Avg Change:" + "" + str(avgChange))

    greatestProfit = (max(differences))
    #print(greatestProfit)
    monthBefore = differences.index(max(differences))
    #print(monthBefore)
    bestMonth = (data[int(monthBefore)+1][0])     
    #+1 since the index starts at 0, rather than 1
    #print(bestMonth)
    print("Greatest Increase in Profits:" + (bestMonth) + " " + (str(greatestProfit)))
    
    
    lowestProfit = (min(differences))
    #print(lowestProfit)
    monthLowBefore = differences.index(min(differences))
    #print(monthLowBefore)
    worstMonth = (data[int(monthLowBefore)+1][0])     
    #+1 since the index starts at 0, rather than 1
    #print(worstMonth)
    print("Greatest Decrease in Profits:" + (worstMonth) + " " + (str(lowestProfit)))



    #for row in csvreader:
           # print(row) testing to make sure I pulled the file correctly
         