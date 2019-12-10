import os
import csv


csvpath = os.path.join('.', 'Resources', 'budget_data.csv') 


with open(csvpath, newline='') as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',') #split data with the comma

    print(csvreader)

  
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    data = list(csvreader)
    Total_Months = len(data)

    pAndL = []
    differences = []
    
    diffRange = (len(data))-1
    

    for i in range(diffRange):
            older = data[i+1][1]
            recent = data[i][1]
            diff = (int(older)-int(recent))
            differences.append(diff)
            pAndL.append(int(data[i][1]))

    lastMonth = (data[i+1][1])
    total = (sum(pAndL) + int(lastMonth))
    
    firstMonth = (data[0][1])
    
    avgDiff = ((int(lastMonth)-int(firstMonth))/(i+1))
    avgChange = str(round(avgDiff,2))

    greatestProfit = (max(differences))
    
    monthBefore = differences.index(max(differences))
    
    bestMonth = (data[int(monthBefore)+1][0])     
    
    lowestProfit = (min(differences))

    monthLowBefore = differences.index(min(differences))
    
    worstMonth = (data[int(monthLowBefore)+1][0])     
    
    print("Greatest Decrease in Profits:" + (worstMonth) + " " + (str(lowestProfit)))


text_file = open("PyBank_output_PBL.txt", "w") # create text file in same folder as main.py, assign variable to path
print('Financial Analysis')
text_file.write('Financial Analysis')
print('-------------------------')
text_file.write('-------------------------')
print("Total Months:" + " " + str(Total_Months))
text_file.write("Total Months:" + " " + str(Total_Months))
print('-------------------------')
text_file.write('-------------------------')
print("Total:" + " " + "$" + str(total))
text_file.write("Total:" + " " + "$" + str(total))
print('-------------------------')
text_file.write('-------------------------')
print("Avg Change:" + "" + "$" + str(avgChange))
text_file.write("Avg Change:" + "" + "$" + str(avgChange))
print('-------------------------')
text_file.write('-------------------------')
print("Greatest Increase in Profits:" + (bestMonth) + " " + "$" + (str(greatestProfit)))
text_file.write("Greatest Increase in Profits:" + (bestMonth) + " " + "$" + (str(greatestProfit)))
print('-------------------------')
text_file.write('-------------------------')
print("Greatest Decrease in Profits:" + (worstMonth) + " " + "$" + (str(lowestProfit)))
text_file.write("Greatest Decrease in Profits:" + (worstMonth) + " " + "$" + (str(lowestProfit)))
text_file.close() # if you open it, close it        