import csv
import re

def clean_text(text):
    # Remove non-printable characters
    return re.sub(r'[^\x20-\x7E]', '', text)

input_file = '/Users/bryanfinkel/Desktop/PROGRAM/LEARNING/PROJECTS/djangotest3/mymap/stages_table.csv'
output_file = '/Users/bryanfinkel/Desktop/PROGRAM/LEARNING/PROJECTS/djangotest3/mymap/CLEANED_stages_table.csv'

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        clean_row = [clean_text(cell) for cell in row]
        writer.writerow(clean_row)
