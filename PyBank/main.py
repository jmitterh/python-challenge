'''
Jean-Paul Mitterhofer
10/21/2019

PyBank:
'''

import os
import csv

#variables
count_month = 0
months = []
bank_amount = []
p_change = []

#path to collect data from csv file
pybank_csv = os.path.join('.','PyBank','Resources','budget_data.csv')

#Reading in the csv file
with open (pybank_csv, 'r') as csvfile:

    #Split the data by comma deliminator
    csvreader = csv.reader(csvfile, delimiter = ',')

    #header row
    header = next(csvreader)

    #for loop to define columns months, and bank amount
    for row in csvreader:
        count_month += 1
        months.append(row[0])
        bank_amount.append(float(row[1]))

    #the average change last month - first month/ total months-first month
    first_v = bank_amount[0]
    last_v = bank_amount[-1]
    avg_value = (last_v - first_v)/(count_month-1)

    # for loop to get the monthly change in profit
    # by subtracting the months
    # make sure to subtract the len of the bank amount so you
    # don't iterate past your last index when subtracting
    for k in range(len(bank_amount)-1):
        p_change.append(bank_amount[k+1]-bank_amount[k])
    
    #min value
    minBankValue = min(p_change)

    #max value
    maxBankValue = max(p_change)

    # finding the min month and the max month
    # since we subtract the first month with second month
    # and so on within the for loop, the p_change month index
    # is not insync with the month list. Adding one to the
    # increment resolves this problem
    for i in range(len(p_change)):

        if minBankValue == p_change[i]:
            minMonth = months[i + 1]
        elif maxBankValue == p_change[i]:
            maxMonth = months[i + 1]

#format floats to currency by creating a function
def cur(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

#prints to terminal
print("Financial Analysis\n--------------------------------------\n")
print(f"Total Months: {count_month}")
print(f"Total: {cur(sum(bank_amount))}")
print(f"Average Change: {cur(avg_value)}")
print(f"Greatest Increase in Profits: {maxMonth} {cur(maxBankValue)}")
print(f"Greatest Decrease in Profits: {minMonth} {cur(minBankValue)}")

#export to a text file
with open("Bank_data.txt", "a+") as f:
    f.write("\nFinancial Analysis\n--------------------------------------\n")
    f.write(f"Total Months: {count_month}\n")
    f.write(f"Total: {cur(sum(bank_amount))}\n")
    f.write(f"Average Change: {cur(avg_value)}\n")
    f.write(f"Greatest Increase in Profits: {maxMonth} {cur(maxBankValue)}\n")
    f.write(f"Greatest Decrease in Profits: {minMonth} {cur(minBankValue)}\n")