# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resource", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
candidate_counties=[]
candidate_dict={}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = -float("inf")
winning_percentage = -float("inf")

# 2: Track the largest county and county voter turnout.
largest_CountyName=""
largest_CountyCount=-float("inf")
largest_CountyPerc= -float("inf")
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        largest_CountyName=row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
        
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if largest_CountyName not in candidate_counties:

            # 4b: Add the existing county to the list of counties.
            candidate_counties.append(largest_CountyName)

            # 4c: Begin tracking the county's vote count.
            candidate_dict[largest_CountyName] = 0 
        # 5: Add a vote to that county's vote count.
        candidate_dict[largest_CountyName] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)
    # 6a: Write a repetition statement to get the county from the county dictionary.
    for county_name in candidate_dict:
        # 6b: Retrieve the county vote count.
        county_vote=candidate_dict[county_name]
        # 6c: Calculate the percent of total votes for the county.
        county_percentage= float(county_vote / float(total_votes)) *100
         # 6d: Print the county results to the terminal.
        county_results=(
        f'{county_name}: {county_percentage:.1f}% ({county_vote:,})')
        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write a decision statement to determine the winning county and get its vote count.
        if (county_vote > largest_CountyCount) and (county_percentage > largest_CountyPerc):
            largest_CountyCount=county_vote
            largest_CountyName=county_name
            largest_CountyPerc= county_percentage 
    # 7: Print the county with the largest turnout to the terminal.
    largestCounty= (
        f'----------------------------------------------\n'
        #f'Largest County Count= {largest_CountyCount:,}\n'
        f'Largest County Voter Turnout= {largest_CountyName}\n'
       # f'Largest Count Percentage= {largest_CountyPerc:.1f}%\n'
        f'----------------------------------------------\n')
    print(largestCounty)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largestCounty)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
