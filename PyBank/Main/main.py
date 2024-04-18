import os
import csv

print("Financial Analysis")
print()
print("----------------------------")


profit = [] #create a bank to store the profits
total_profit = []
csvpath = os.path.join("..", "Resources", "budget_data.csv") #create path for csv file

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #separate columns with commas

    next(csvreader) #skip the header row

    month_count = sum(1 for row in csvreader) #count the number of months in the dataset
    print("Total Months:  " + str(month_count))
    print()


with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    column_values = [] #create a bank to store profit/loss values
    
   
    column_index = 1  
    
  
    for row in csvreader:
       
        column_value = row[column_index]
        
       
        column_values.append(column_value)



with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    column_values = []
    column_index = 1  
    
    for row in csvreader:
        column_value = row[column_index]
        column_values.append(column_value)
    
    def sum_profit(profit_values):
        total_profit = 0
        for value in profit_values:
            total_profit += float(value)  
        return total_profit #add profits/losses to the bank

    total_profit = sum_profit(column_values)
    print("Total: $" + str(total_profit))
    print()
       

column_index = 1
changes = []
dates = [] 
with open(csvpath, encoding='UTF-8') as csvfile:    

    lines = csvfile.readlines()
    for i in range(2, len(lines)): #find the amount of change in profit/loss for each month
        current_row = lines[i].strip().split(',')
        previous_row = lines[i-1].strip().split(',')
        current_value = float(current_row[column_index]) 
        previous_value = float(previous_row[column_index])  
        change = current_value - previous_value
        changes.append(change)

        date = current_row[0]
        dates.append(date)
        
        
average_change = sum(changes) / len(changes) #divide the total monthly changes by the number of months to get the average
max_change = max(changes)
min_change = min(changes)

max_change_index = changes.index(max_change)
min_change_index = changes.index(min_change)
max_change_date = dates[max_change_index]
min_change_date = dates[min_change_index]

rounded_total = round(total_profit, 0)
rounded_average_change = round(average_change, 2)
rounded_increase = round(max_change, 2) #added float
rounded_decrease = round(min_change, 2)

output = [f"Financial Analysis\n",  #create the lines to be printed in the output report. This was developed n office hours
          f"---------------------------\n",
          f"Total Months: {month_count}\n",
          f"Total : ${rounded_total:.0f}\n", #added int
          f"Average Change: ${rounded_average_change}\n",
          f"Greatest Increase in Profits: {max_change_date} ($ {rounded_increase:.2f})\n",
          f"Greatest Decrease in Profits: {min_change_date} (${rounded_decrease:.2f})\n"]

output_file_path = os.path.join("..", "Analysis", "PyBank_Analysis.txt") #create the path for the output file
with open(output_file_path, "w") as file:
    for line in output:
        file.write(line)

print(f"Average Change: $ {rounded_average_change:.2f}") #print output in the terminal to test
print()
print(f"Greatest Increase in Profits:  {max_change_date} ($ {rounded_increase:.2f})") 
print()
print(f"Greatest Decrease in Profits:  {min_change_date}  (${rounded_decrease:.2f})")




