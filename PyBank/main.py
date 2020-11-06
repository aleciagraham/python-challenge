import os
import csv


#Assign variable for data on csv file and loop through lists
   
date = []
dates = []
profit_loss = []
all_changes =[]
csvpath = file_to_load = os.path.join("budget_data.csv")

previous=0
change = 0
months=0
sum_change=0
greatest_increase = 0
greatest_month = ""
greatest_decrease = 99999999999999999
decrease_month = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        months+=1
        # Add title
       # date = str(csvreader[0])
        profit_loss.append(int(row[1]))
        # dates.append(row([0]))
        change = int(row[1])-previous
        all_changes.append(change)
        previous=int(row[1])
        if months>1:
         sum_change+=change
        if change >greatest_increase:
            greatest_increase=change
            greatest_month=row[0]
        if change <greatest_decrease:
            greatest_decrease= change
            decrease_month=row[0]

# of months
months = int(len(profit_loss))
print("The total number of months: ", (months))

#Net total amount of Profit and Loss
netamount= sum(profit_loss)
print(f"Total: ${netamount}")

#average change
avg_change = round(sum_change/(months-1),2)
print(f"Average Change:$ {avg_change}")

# The greatest increase
greatest = max(all_changes)
print(f"The Greatest Increase in Profits: {greatest_month} ${greatest}")


# The lowest increase
lowest = min(all_changes)
print(f"The Lowest Decrease in Profits: {decrease_month} ${greatest_decrease}")

