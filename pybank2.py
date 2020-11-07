#imports 
import os
import csv

#Set path for "budget_data" CSV file
budget_data_path = os.path.join("Resources", "budget_data.csv")

#Open the "budget_data" file
with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    #Skip the Header Row
    next(csvreader)

    #Assign variables
    change = 0
    net_total = 0
    total_months = 0
    previous = 0
    difference_list = []

    #Read through data
    for x in csvreader:
        
        #Total months 
        total_months = total_months + 1

        #Net total of profits and losses
        net_total = net_total + int(x[1])

        #Find the difference between rows in column 2 
        change = int(x[1]) - previous
        previous = int(x[1])
        difference_list.append(change)
    
        #Calculate the differences month to month
        length = len(difference_list) - 1

    #Calculate the average change in profits and losses
    average = round((sum(difference_list[1:])/length),2)

    #Calculate the max increase and decrease in profits
    maxincrease = int(max(difference_list))
    minincrease = int(min(difference_list))

    #Print statements
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: ${maxincrease}")
    print(f"Greatest Decrease in Profits: ${minincrease}")