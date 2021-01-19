import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print(csvpath)
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    months = 0
    profit_losses = 0
    profits = 0
    losses = 0
    rows = []
    months_list = []

    for row in csvreader:
        print(row[0],row[1])
        months = months + 1
        pl = int(row[1])
        profit_losses = profit_losses + pl
        rows.append(pl)
        months_list.append(row[0])
        
    count = 0
    changes = []
    
    for item in rows :
        if count != 0: 
            change =  item - rows[count - 1]
            changes.append(change)
        count = count + 1

    max_changes = max(changes)
    min_changes = min(changes)
    max_month = changes.index(max_changes) + 1
    min_month = changes.index(min_changes) + 1 



    print("Financial Analysis")
    print("-------------------")
    print(f'Total Months: {months}')
    print(f'Total: {profit_losses}')
    print(f'Average Change: ${sum(changes) / len(changes)}')
    print(f'Greatest Increase in Profit: {months_list[max_month]} (${max_changes})')
    print(f'Greatest Decrease in Profit: {months_list[min_month]} (${min_changes})')




    
    
