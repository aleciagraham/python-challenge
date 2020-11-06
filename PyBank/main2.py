#PyBank

import os
import csv


#setting a variable for csv file
csvpath = file_to_load = os.path.join("budget_data.csv")

with open(csvpath) as financial_data:

  csvreader = csv.reader(financial_data, delimiter= ",")
  
  for row in csvreader:
    header = next(csvreader)
    row1 = next(csvreader)
  
  print(row[0])

 
# of months
total_months = int(len(months))
print("The total number of months: ", (total_months))

#Net total amount of Profit and Loss
netamount= sum(profitloss)
print(f"Total: netamount")

# average of profit and loss
average = float(netamount/months)
# return avg
print(f"Profit and Average Change: ${average, round,2}")

# The greatest increase
greatest = max(row[1])
print(f"The Greatest Increase in Profits:  (row[0],greatest)")

# The lowest increase
lowest = min(row[1])
print(f"The Greatest Decrease in Profits: ({row([0]), greatest})")


#--------------------------------------

#setting a variable for csv file
csvpath = file_to_load = os.path.join("budget_data.csv")

with open(csvpath) as financial_data:

  csvreader = csv.reader(financial_data, delimiter= ",")
  
  for row in csvreader:
    header = next(csvreader)
    row1 = next(csvreader)
  
  print(row[0])

 
# of months
total_months = int(len(months))
print("The total number of months: ", (total_months))

#Net total amount of Profit and Loss
netamount= sum(profitloss)
print(f"LOSS PERCENT: netamount")

# average of profit and loss
average = float(netamount/months)
# return avg
print(f"Profit and Loss Average: ${average}")

# The greatest increase
greatest = max(row[1])
print(f"The Greatest Increase:  (row[0],greatest)")

# The lowest increase
lowest = min(row[1])
print(f"The Greatest Increase: ({row([0]), greatest})")