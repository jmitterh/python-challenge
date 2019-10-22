'''
Jean-Paul Mitterhofer
10/21/2019

PyPoll:
In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''

import os
import csv

#variables
votes = 0
ids = []
county = []
names = []
k_per = 0
k_total = 0
c_per = 0
c_total = 0
l_per = 0
l_total = 0
o_per = 0
o_total = 0
winner = 0

#path to collect data from csv file
#pybank_csv = os.path.join('.','Resources','budget_data.csv')

#os path call does not work on my cpu so I had to use the file path of my file
pypoll_csv = "C:/DataAnalyticsBootCamp/WEEK_3/python-challenge/PyPoll/Resources/election_data.csv"

#Reading in the csv file
with open (pypoll_csv, 'r') as csvfile:

    #Split the data by comma deliminator
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    #for loop
    for row in csvreader:
        votes += 1
        ids.append(row[0])
        county.append(row[1])
        names.append(row[2])

    #canidates: Khan, Correy, Li, O'Tooley

    #counties: Marsh,Queen,Trandee, Bamoo, Raffah


    #format to percentage

#prints to terminal
print("Election Results\n--------------------------------------\n")
print(f"Total Votes: {votes}")
print("--------------------------------------")
print(f"Khan: {k_per} {k_total}")
print(f"Correy: {c_per} {c_total}")
print(f"Li: {l_per} {l_total}")
print(f"O'Tooley: {o_per} {o_total}")
print("--------------------------------------")
print(f"Winner: {winner}")

#export to a text file
with open("Poll_data.txt", "a+") as f:
    f.write("Election Results\n--------------------------------------\n")
    f.write(f"Total Votes: {votes}")
    f.write("--------------------------------------")
    f.write(f"Khan: {k_per} {k_total}")
    f.write(f"Correy: {c_per} {c_total}")
    f.write(f"Li: {l_per} {l_total}")
    f.write(f"O'Tooley: {o_per} {o_total}")


    