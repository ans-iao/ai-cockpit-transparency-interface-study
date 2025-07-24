"""
Script to combine questionnaire data from multiple subject directories into a single CSV file.

This script:
1. Reads individual questionnaire CSV files from subject directories under 'data/'
2. Combines all questionnaire responses into a single dictionary
3. Writes combined data to 'questionnaire_data.csv' with subjects as rows and questions as columns
4. Handles cases where subjects may have different numbers of responses by filling empty cells
"""

import os
import glob
import csv

subj_path = "data"

subjects = os.listdir(subj_path)

q_dict = {"subject": []}

for subj in subjects:
    csv_file = glob.glob(os.path.join(subj_path, subj, "*questionnaires*"))[0]
    q_dict["subject"].append(subj)
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=";")

        for i, row in enumerate(reader):
            if i == 0:
                continue

            if row[0] in q_dict:
                q_dict[row[0]].append(row[1])
            else:
                q_dict[row[0]] = [row[1]]

with open("questionnaire_data.csv", mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=";")

    writer.writerow(q_dict.keys())
    max_rows = max(len(v) for v in q_dict.values())

    # Write the rows, iterating over the index of each value list
    for i in range(max_rows):
        row = [q_dict[key][i] if i < len(q_dict[key]) else '' for key in q_dict]
        writer.writerow(row)
