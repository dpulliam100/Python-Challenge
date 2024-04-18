import os
import csv

print("Election Results")
print()
print("--------------------------------------")
print()

csvpath = os.path.join("..", "Resources", "election_data.csv") #create path for csv file

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #read the csv and set the delimeter

    next(csvreader) #skip the header row 

    vote_count = sum(1 for row in csvreader) #count the votes
    print("Total Votes:  " + str(vote_count))
    print()
    print("--------------------------------------")
    print()

Charles_Total = 0
Diana_Total = 0
Raymon_Total = 0

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

 
    column_index = 2  
    
    
    for row in csvreader:
        
        column_value = row[column_index]
        
        if column_value == "Charles Casper Stockham": #count the votes for individual candidates
            Charles_Total += 1 
        elif column_value == "Diana DeGette":
            Diana_Total += 1
        elif column_value == "Raymon Anthony Doane":
            Raymon_Total += 1

    Charles_Pct = (Charles_Total/vote_count) * 100 #set the individual vote counts to a percentage of the total
    Diana_Pct = (Diana_Total/vote_count) * 100
    Raymon_Pct = (Raymon_Total/vote_count) * 100
    print(f"Charles Casper Stockham: {Charles_Pct:.3f}% ({Charles_Total})") #pint the vote percentages and round to 3 decimal places
    print(f"Diana DeGette: {Diana_Pct:.3f}% ({Diana_Total})")
    print(f"Raymon Anthony Doane: {Raymon_Pct:.3f}% ({Raymon_Total})")
    print()
    print("--------------------------------------")

    winner = max(Charles_Total, Diana_Total, Raymon_Total) #find the winner using the max of each of their votes

    if winner == Charles_Total:
        winner_name = "Charles Casper Stockham"
        print("Winner: Charles Casper Stockham")
    
    elif winner == Diana_Total:
        winner_name = "Diana DeGette"
        print("Winner: Diana DeGette")

    else:
        winner_name = "Raymon Anthony Doane"
        print("Winner: Raymon Anthony Doane")

    print()
    print("--------------------------------------")




output = [f"Election Results\n", #create the ouput for the analysis. This process was derived in the PyBank project
          f"---------------------------\n",
          f"Total Votes: {vote_count}\n",
          f"Charles Casper Stockham: {Charles_Pct:.3f}%\n",
          f"Diana DeGette: {Diana_Pct:.3f}%\n",
          f"Raymon Anthony Doane: {Raymon_Pct:.3f}%\n",
          f"---------------------------\n",
          f"Winner: {winner_name}\n"]

output_file_path = os.path.join("..", "Analysis", "PyPoll_Analysis.txt") #set the path to write the output analysis to.
with open(output_file_path, "w") as file:
    for line in output:
        file.write(line)






