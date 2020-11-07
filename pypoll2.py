#1st import the OS, CSV, and Counter modules
#Beginning imports
import os
import csv

#Input file
csvfilepath = os.path.join("Resources", "election_data.csv")

#Output file
outfilepath = os.path.join("Analysis", "election_analysis.txt")

#Update
def result_update(result, candidate, votes):
  if key in result.candidate():
    result[candidate].append(votes)
  else:
    result[candidate] = [votes]
  return result

#Initialize
total_votes = 0
election = {}

#Open csv file
with open(csvfilepath) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    header = next(election_data)
   
    for row in election_data:
      
      #Total votes
      total_votes += 1
      
      #Voter id and candidate name
      voter = row[0]
      candidate = row[2]
      
      #Update election dictionary
      election = result_update(election, candidate, voter)
      
#The analysis dict:
analysis = {cadidate : len(votes) for candidate,votes in election.items()}

#Sort analysis
sorted_analysis = sorted(analysis.items(), candidate=lambda v:v[1], reverse=True)

#Print results
print_results = [
  f"Election Results", "Total Votes: {total_votes}",
]

for candidate, votes in sorted_analysis:
  #The percentage of votes that 'Candidate' won
  percentage = float(votes/total_votes)*100
  
  #Set the space after candidate
  sp = ' '*(10 - len(candidate))
  
  #Append the ccandidate percentage
  print_resultss.append(
    f" {candidate.title()}:{sp} {percentage:5.2f}%  ({votes})")

#Append the results for winner
print_results.append(f" Winner: {sorted_analysis[0][0]}")

#Print on terminal
for result in print_results:
  print(result)

#Output the results
with open(outfilepath, "w") as txtfile:
    for result in print_results:
        txtfile.write( result+"\n" )