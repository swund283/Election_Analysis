# # Add our dependencies.
# import csv
# import os

# # Assign a variable to load a file from a path.
# election_results_source = os.path.join("Resources/election_results.csv")
# # Assign a variable to save the file to a path.
# election_analysis_output = os.path.join("Resources", "election_analysis.txt")

# # Open the election results and read the file.
# with open(election_results_source) as election_data_open:
#     csv_file_reader = csv.reader(election_data_open)

#     with open(election_analysis_output, 'w') as election_output:
#         csv_file_writer = csv.writer(election_output)

#      # Read and print the header row.
#     headers = next(csv_file_reader)
#     csv_file_writer.writerow(headers)

#      #   # Read and print the next row after reader
#      # first_row = next(csv_file_reader)
#     # print(first_row)

#     # # Print each row in the CSV file.
#     #    for row in csv_file_reader:
#     #        print(row)

import os
import csv
source_data = os.path.join("Resources", "election_results.csv")
output_data = os.path.join("Resources", "election_analysis.txt")
with open(source_data) as csv_file:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csv_file, delimiter=',')
    # Nested session with the output file
    with open(output_data, "w") as output_file:
        # Initialize csv.writer
        csvwriter = csv.writer(output_file, delimiter=',')
        # Transfer the rows from input file to output file
        for row in csvreader:
            csvwriter.writerow(row)