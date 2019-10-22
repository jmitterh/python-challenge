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

#path to collect data from csv file
pybank_csv = os.path.join('.','Resources','budget_data.csv')

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
        
    #min value
    minBankValue = min(bank_amount)

    #max value
    maxBankValue = max(bank_amount)

    #finding the min month and the max month
    for i in range(len(bank_amount)):

        if minBankValue == bank_amount[i]:
            minMonth = months[i]
        elif maxBankValue == bank_amount[i]:
            maxMonth = months[i]

    #the average value
    avg_value = sum(bank_amount)/count_month

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
print(f"Average  Change: {cur(avg_value)}")
print(f"Greatest Increase in Profits: {minMonth} {cur(maxBankValue)}")
print(f"Greatest Decrease in Profits: {maxMonth} {cur(minBankValue)}")

#export to a text file
with open("Bank_data.txt", "a+") as f:
    f.write("Financial Analysis\n--------------------------------------\n")
    f.write(f"Total Months: {count_month}\n")
    f.write(f"Total: {cur(sum(bank_amount))}\n")
    f.write(f"Average  Change: {cur(avg_value)}\n")
    f.write(f"Greatest Increase in Profits: {minMonth} {cur(maxBankValue)}\n")
    f.write(f"Greatest Decrease in Profits: {maxMonth} {cur(minBankValue)}\n")