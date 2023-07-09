import os
import csv
from collections import Counter

#open csv
csvpath = os.path.join(".", "Resources", "election_data.csv")

#read csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

        #store the csv headers
    election_csv_header = next(csvreader) 
    
    print(f'Election Results')
    print(f'-----------------------------')
    print 
    #variables
    total_votes = 0
    count = 0
    candidates = []   #number of different variables (candidates) in column 3
    candidate_votes = []
    #percent_votes =[]
   
#### The total number of votes cast (either column)
    for row in csvreader:
        #total_votes= len(candidates)
        total_votes += 1
        #candidate_votes = 0  

        if row[2] not in candidates: 
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)  #number of times each variable appears

        else:
            index = candidates.index(row[2])
            #candidate_votes = candidate_votes + 1
            candidate_votes[index] += 1

#find percentage of votes for each candidate
percent_votes = []
for votes in candidate_votes:
    percentage = round(((votes/total_votes) * 100), 3)
    percent_votes.append(percentage)
    
#and the winner is
winner = max(candidate_votes)
index = candidate_votes.index(winner)
winning_cand = candidates[index]

print(f'Total Votes: ', total_votes)
print(f'-----------------------------')    
#print(row[2], candidate_votes)
#print(f'-----------------------------')


#assign amounts to candidates per x
for x in range(len(candidates)):
    print(f"{candidates[x]}: {str(percent_votes[x])}% ({str(candidate_votes[x])}) ")
    print(f'-----------------------------')
print(f"Winner: {winning_cand}")
 #{str(percent_votes)}%



#create text file
new_txt_path = r'C:\Users\rodne\python-challenge\Pypoll\Analysis'
text_file1 = "PyPoll Analysis.text"
name= os.path.join(new_txt_path, text_file1)
if os.path.exists (new_txt_path):
    # create the file
    with open(name, "a") as f:
        print("ELECTION RESULTS", file=f)
        print("----------------------------", file=f)
        print("Total Votes: ", total_votes , file=f)
        print("----------------------------", file=f)
        #print("Candidate Totals :", candidates , candidate_votes, file=f)
        for x in range(len(candidates)):
            print(candidates[x],":" , str(percent_votes[x]),"%  (", (str(candidate_votes[x])) ,")", file = f)
            print('-----------------------------', file = f)
        print("Winner: ", winning_cand, file=f)
        print('-----------------------------', file = f)

