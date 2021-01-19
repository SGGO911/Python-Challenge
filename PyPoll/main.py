import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    candidates = []
    poll_dict = { }
    for row in csvreader:
        name = row[2]
        poll_dict[name] = poll_dict.setdefault(name, 0 ) + 1

    print(poll_dict)

    total_votes = 0
    winner = ""
    last_votes = 0
    for name, votes in poll_dict.items():
        total_votes = total_votes + votes 
        if votes > last_votes:
            winner = name 
            last_votes = votes


    print("Election Results")
    print("-" * 25)
    print(f'Total Votes: {total_votes}')
    print("-" * 25)
    for name, votes in poll_dict.items():
        print(f'{name}: {votes / total_votes * 100:.3f}% ({votes})')
    print("-" * 25)
    print(f'Winner: {winner}')

    with open('./Analysis/output.txt', 'w') as f:
        f.write("Election Results\n")
        f.write("---------------------------\n")
        f.write(f'Total Votes: {total_votes}\n')
        f.write("---------------------------\n")
        for name, votes in poll_dict.items():
            f.write(f'{name}: {votes / total_votes * 100:.3f}% ({votes})\n')
        f.write("---------------------------\n")
        f.write(f'Winner: {winner}\n')
        f.write("---------------------------\n")