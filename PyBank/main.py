import os
import csv

# Path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
months = []

#CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) 

    for row in csvreader:
        month = row[0]
        profit_loss = int(row[1])

        total_months += 1
        net_total += profit_loss

        if total_months >1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            months.append(month)

        previous_profit_loss = profit_loss

# average change
average_change = sum(changes) / len(changes)

# greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_month = months[changes.index(greatest_increase)]
greatest_decrease_month = months[changes.index(greatest_decrease)]

# Print to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export to text
output_path = os.path.join('analysis', 'financial_analysis.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")