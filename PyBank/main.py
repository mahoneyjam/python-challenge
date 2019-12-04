import os
import csv


csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


#read with CSV file
with open(csvpath, newline='') as csvfile:
   
    #split data by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

  
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    data = list(csvreader)
    Total_Months = len(data)
    print("Total_Months:" + " " + str(Total_Months))

    

    #for row in csvreader:
           # print(row) testing to make sure I pulled the file correctly
         
 

    
  
