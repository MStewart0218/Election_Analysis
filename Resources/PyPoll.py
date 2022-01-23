#The data we need to retrieve. C:\Users\Marga\Election_Analysis\Resources\election_results.csv
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = 'election_results.csv'

# Assign/ Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    #print(str(election_data))_IMPORTANT TO USE LATER IN CODE

    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    print(headers)    

# Print each row in the CSV file.
    #for row in file_reader:
        #print(row[0])


# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
#write some data to the file.
    txt_file.write(str("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson"))


#1. The total number of votes cast 
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote
