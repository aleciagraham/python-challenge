#PyBank

import os
import csv

#setting a variable for csv file
csvpath = file_to_load = os.path.join("..","Resources", "budget_data.csv")

with open("budget_data.csv") as financial_data:

  csvreader = csv.reader(csvfile, delimiter=",")
  
  for row in csvreader:
    months= str(row[0])
    profitloss= int(row[1])
  print(row[0])

 
# of months
total_months = int(len(months))
print("The total number of months: ", (total_months))

#Net total amount of Profit and Loss
netamount= int(sum([1)])

print("The net total is: $",(netmount))

# average of profit and loss
average = float(netamount/months)
return avg
print("Profit and Loss Average: $",(average))

# The greatest increase
greatest = max(row[1])
print("The Greatest Increase:", row[0],greatest)

# The lowest increase
lowest = min(row[1)
print("The Greatest Increase:",row([0], greatest)