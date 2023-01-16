import os, csv
from pathlib import Path

input_file = Path("PyPoll", "Resources", "election_data.csv")

# variables
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0 

with open(input_file, newline="", encoding = "utf-8") as elections:

    csvreader = csv.reader(elections, delimiter = ",")

    header = next(csvreader)

    for row in csvreader:
            total_votes += 1

            if row[2] == "Charles Casper Stockham":
                charles_votes +=1
            elif row[2] == "Diana DeGette":
                diana_votes +=1 
            elif row[2] == "Raymon Anthony Doane":
                raymon_votes +=1 


candidates = ["Charles", "Diana", "Raymon"] 
votes = [charles_votes, diana_votes, raymon_votes]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key = dict_candidates_and_votes.get)

# percentages
charles_percent = (charles_votes/total_votes) * 100
diana_percent = (diana_votes/total_votes) * 100
raymon_percent = (raymon_votes/total_votes) * 100

print(f"Election Results")
print(f"--------------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------------")
print(f"Charles Casper Stockham: {charles_percent:3f}% ({charles_votes})")
print(f"--------------------------------")
print(f"Diana DeGette: {diana_percent:3f}% ({diana_votes})")
print(f"--------------------------------")
print(f"Raymon Anthony Doane: {raymon_percent:3f}% ({raymon_votes})")
print(f"--------------------------------")
print(f"Winner: {key}")
print(f"--------------------------------")


#output files

output_file = Path("PyPoll", "Election_Results.txt")

with open(output_file, "w") as file:


    file.write(f"Election Results")
    file.write("\n")
    file.write(f"------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"------------------------")
    file.write(f"Charles Casper Stockham: {charles_percent:3f}% ({charles_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {diana_percent:3f}% ({diana_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {raymon_percent:3f}% ({raymon_votes})")
    file.write("\n")
    file.write(f"------------------------")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"------------------------")