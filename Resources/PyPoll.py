#The data we need to retrieve. C:\Users\Marga\Election_Analysis\Resources\election_results.csv
#Add our dependecies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = 'election_results.csv'

# Assign/ Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

#Declare Candidate Options list
candidate_options = []

#Declare Candidate Votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    #print(str(election_data))-IMPORTANT TO USE LATER IN CODE

    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
        #print(headers)    

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that cadidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to cadidate count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #To do: print out each candidate's name, vote count, and precentage of votes to the terminal. 
    
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
     winning_count = votes
     winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
     winning_candidate = candidate_name
# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#To do: print out the winning candidate, vote count, and precentage to terminal.

    # 4. Print the candidate name and percentage of votes.  
    print(f"{candidate_name}: received {vote_percentage: .1f}% of the vote.\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#print the candidate vote dictionary.
print(candidate_votes)

# Print the candidate list.
print(candidate_options)

# 3. Print the total votes.
print(total_votes)


# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
#write some data to the file.
    #txt_file.write(str("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson"))


#1. The total number of votes cast 
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote
