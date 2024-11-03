import csv

# specify paths for input and output
input_file = 'data/spelling_errors.dat'
output_file = 'data/spelling_errors.csv'

correct_word = None
data = []

with open(input_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('$'):
            correct_word = line[1:]
        elif correct_word:
            data.append([correct_word, line])

# write to csv file with two columns
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['correct_spelling', 'wrong_spelling'])
    csvwriter.writerows(data)

print(f'Data saved as .csv in: {output_file}')