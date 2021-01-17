import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

Month = []
Total_dollars = []
Change = []

count = 0
profit = 0
profit_change = 0
start_profit = 0

with open(csvpath, newline= "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        count = count + 1

        Total_dollars.append(row[1])
        profit = profit + int(row[1])

        finish_profit = int(row[1])
        month_change_profit = finish_profit - start_profit

        Change.append(month_change_profit)

        profit_change = profit_change + month_change_profit
        start_profit = finish_profit

        average_profit_change = (profit_change/count)

        greatest_increase = max(Change)
        greatest_decrease = min(Change)

        Month.append(row[0])

        month_increase = Month[Change.index(greatest_increase)]
        month_decrease = Month[Change.index(greatest_decrease)]

print("Financial Analysis")
print("--------------------------")
print("Total Months:" + str(count))
print("Total:" + "$" + str(profit))
print("Average Change:" + "$" + str(int(average_profit_change)))
print("Greatest Increase in Profits:" + str(month_increase) + "($" + str(greatest_increase))
print("Greatest Decrease in Profits:" + str(month_decrease) + "($" + str(greatest_decrease))


f = open("financial_analysis.txt", "x")
f.write("Financial Analysis")
f.write("----------------------")
f.write("Total Months:" + str(count))
f.write("Total:" + str(profit))
f.write("Average Change:" + str(int(average_profit_change)))
f.write("Greatest Increase in Profits:" + str(month_increase) + "($" + str(greatest_increase)) 
f.write("Greatest Decrease in Profits:" + str(month_decrease) + "($" + str(greatest_decrease))

f.close()
