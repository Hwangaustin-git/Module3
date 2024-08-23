import os
import csv

# Path 
csvpath = os.path.join('Resources', 'election_data.csv')

# variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read CSV 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        candidate = row[2]
        
        # Count the total number of votes
        total_votes += 1
        
        # Track the votes each candidate received
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Determine the winner and calculate the percentage of votes each candidate won
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export to text
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for result in results:
        txtfile.write(result + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
