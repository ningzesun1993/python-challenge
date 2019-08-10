import os
import csv


def main():
    #open the csv in a file called Rescurces
    csv_path = os.path.join('Resources', 'budget_data.csv')
    with open(csv_path) as csv_files:
        data = [rows for rows in csv.reader(csv_files)]
        template = eval(data[1][1])
    with open(csv_path, newline= "") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        total_month = 0
        total_amount = 0
        total_change = 0
        increase_max = 0
        increase_min = 0
        max_date = ""
        min_date = ""
        for row in csv_reader:
            total_month += 1
            #change the variable type to integer
            secondRow = eval(row["Profit/Losses"])
            change = secondRow - template
            total_change += change
            template = secondRow
            #loop to calculate the total amount
            total_amount += secondRow
            #to calculate the biggest one and smallest one
            if increase_max < change:
                increase_max = change
                max_date = row['Date']
            if increase_min > change:
                increase_min = change
                min_date = row['Date']
    print_out = "Financial Analysis\n----------------------------"
    print_out += "\nTotal Months: " + str(total_month) + "\nTotal: $" + str(total_amount)
    print_out += "\nAverage Change: ${:.2f}".format(total_change / (total_month - 1))
    print_out += "\nGreatest Increase in Profits: {}20{} (${})".format(max_date[0:4], max_date[4:6], increase_max)
    print_out += "\nGreatest Decrease in Profits: {}20{} (${})".format(min_date[0:4], min_date[4:6], increase_min)
    print(print_out)
    file = open("output.txt", 'w')
    file.write(print_out)


main()

