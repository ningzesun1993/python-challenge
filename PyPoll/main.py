import csv
import os


def main():
    csv_path = os.path.join('Resources', 'election_data.csv')
    with open(csv_path, newline="") as csvfile:
        name_list = []
        vote_list = []
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            name = row['Candidate']
            exist_not = True
            for i in range(len(name_list)):
                if name_list[i] == name:
                    vote_list[i] += 1
                    exist_not = False
                    break
            if exist_not:
                name_list.append(name)
                vote_list.append(1)
        total = 0
        winner = 0
        for i in range(len(name_list)):
            total += vote_list[i]
            if vote_list[winner] < vote_list[i]:
                winner = i
    print_out = "Election Results\n-------------------------\nTotal Votes: " + str(total)
    print_out += '\n-------------------------\n'
    for i in range(len(name_list)):
        percentage = vote_list[i] / total * 100
        print_out += "{}: {:.3f}% ({})\n".format(name_list[i], percentage, vote_list[i])
    print_out += "-------------------------\nWinner: " + name_list[winner] + '\n-------------------------'
    print(print_out)
    file = open("output.txt", 'w')
    file.write(print_out)


main()

