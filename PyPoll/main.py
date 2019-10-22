'''
Jean-Paul Mitterhofer
10/21/2019

PyPoll:
'''

import os
import csv

#variables
votes = 0
ids = []
county = []
names = []
k_total = 0
c_total = 0
l_total = 0
o_total = 0


#path to collect data from csv file
pypoll_csv = os.path.join('.','Resources','election_data.csv')

#Reading in the csv file
with open (pypoll_csv, 'r') as csvfile:

    #Split the data by comma deliminator
    csvreader = csv.reader(csvfile, delimiter = ',')

    #header row
    header = next(csvreader)

    #for loop for ids, county, and name
    for row in csvreader:
        votes += 1
        ids.append(row[0])
        county.append(row[1])
        names.append(row[2])

    #Total number of votes each canadate has
    for i in range(len(names)):
        if "Khan" == names[i]:
            k_total += 1
        elif "Correy" == names[i]:
            c_total += 1
        elif "Li" == names[i]:
            l_total += 1
        elif "O'Tooley" == names[i]:
            o_total += 1

    #Determining the winner
    if k_total > c_total and k_total > l_total and k_total > o_total:
        winner = "Khan"
    elif c_total > k_total and c_total > l_total and c_total > o_total:
        winner = "Correy"
    elif l_total > k_total and l_total > c_total and l_total > o_total:
        winner = "Li"
    elif o_total > k_total and o_total > c_total and o_total > l_total:
        winner = "O'Tooley"

    #perctage of votes
    k_per = k_total / votes
    c_per = c_total / votes
    l_per = l_total / votes
    o_per = o_total / votes

    #format to percentage function
    def pe(amount):
        if amount >= 0:
            return '{:.2%}'.format(amount)
        else:
            return '-{:.2%}'.format(-amount)

    #format number
    def nu(amount):
        if amount >= 0:
            return '{:,}'.format(amount)
        else:
            return '-{:,}'.format(-amount)

#prints to terminal
print("Election Results\n--------------------------------------\n")
print(f"Total Votes: {nu(votes)}")
print("--------------------------------------")
print(f"Khan: {pe(k_per)} {nu(k_total)}")
print(f"Correy: {pe(c_per)} {nu(c_total)}")
print(f"Li: {pe(l_per)} {nu(l_total)}")
print(f"O'Tooley: {pe(o_per)} {nu(o_total)}")
print("--------------------------------------")
print(f"Winner: {winner}")

#export to a text file
with open("Poll_data.txt", "a+") as f:
    f.write("Election Results\n--------------------------------------\n")
    f.write(f"Total Votes: {nu(votes)}\n")
    f.write("--------------------------------------\n")
    f.write(f"Khan: {pe(k_per)} {nu(k_total)}\n")
    f.write(f"Correy: {pe(c_per)} {nu(c_total)}\n")
    f.write(f"Li: {pe(l_per)} {nu(l_total)}\n")
    f.write(f"O'Tooley: {pe(o_per)} {nu(o_total)}\n")
    f.write("--------------------------------------\n")
    f.write(f"Winner: {winner}")



    