'''
Jean-Paul Mitterhofer
10/21/2019

PyPoll:
'''

import os
import sys
import csv
from collections import defaultdict

#path to collect data from csv file
pypoll_csv = os.path.join('.','PyPoll','Resources','election_data.csv')

#Reading in the csv file
with open (pypoll_csv, 'r') as csvfile:

    #Split the data by comma deliminator and store it as dict_list
    csvreader = csv.DictReader(csvfile, delimiter = ',')

    #header row is skipped
    header = next(csvreader)

    # this dictionary provides a defualt value for each key. 
    # The value is going to be an int defined as 0
    poll_dict = defaultdict(int)

    #Find how many candidates there are within the csv
    #Each candidate shall be defined as a key
    #The increment is defined as a value
    for row in csvreader:
        poll_dict[row['Candidate']] += 1
    print(poll_dict)

    #Finding the winner key and value
    v_max = max(poll_dict.values())
    k_max = max(poll_dict, key=poll_dict.get)

    #Sum votes
    votes = sum(poll_dict.values())

#format number
def nu(amount):
    if amount >= 0:
        return '{:,}'.format(amount)
    else:
        return '-{:,}'.format(-amount)
    
#format to percentage function
def pe(amount):
    if amount >= 0:
        return '{:.2%}'.format(amount)
    else:
        return '-{:.2%}'.format(-amount)

#Display results in terminal
print("\nElection Results\n--------------------------------------\n")
print(f"Total Votes: {nu(votes)}")
print("--------------------------------------")
for key, value in poll_dict.items():
    print(f"{key}: {pe(value/votes)} ({nu(value)})")

print("--------------------------------------")
print(f"Winner: {k_max} with {nu(v_max)} votes!")

#Create a new text file if one is none existing
with open("Poll_data.txt", "a+") as f:
    f.write("\nElection Results\n--------------------------------------\n")
    f.write(f"Total Votes: {nu(votes)}\n")
    f.write("--------------------------------------\n")
    for key, value in poll_dict.items():
        f.write(f"{key} {pe(value/votes)} ({nu(value)})\n")
    f.write("--------------------------------------\n")
    f.write(f"Winner: {k_max} with {nu(v_max)} votes!\n")