# The data we need to retrieve 
# 1. Total number of votes casted 
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote 
# --------------------------------------------------

import os
import csv 

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resource", "election_results.csv")

# Assign a varibale to save the file to a path.
file_to_save= os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    print(election_data)
    #headers=next(file_reader)
    #print(headers)
# --------------------------------------------------

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # write on txt file 
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    # or 
    #txt_file.write("Counties in the Election\n---------\nArapahoe\nDenver\nJefferson\n")







