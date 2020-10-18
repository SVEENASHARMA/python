import os
import csv

wrestling_csv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

def print_percentages(wrestler_data):
    name = str(wrestler_data[0])
    wins = int(wrestler_data[1])
    losses = int(wrestler_data[2])
    draws = int(wrestler_data[3])

    total_matches = wins + losses + draws

    win_percent = (wins / total_matches) * 100

    loss_percent = (losses / total_matches) * 100

    draw_percent = (draws / total_matches) * 100


    print(f"Stats for {name}")
    print(f"WIN PERCENT: {win_percent}")
    print(f"LOSS PERCENT: {loss_percent}")
    print(f"DRAW PERCENT: {draw_percent}")

with open(wrestling_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    name_to_check = input("What wrestler do you want to look for? ")

    for row in csvreader:

        if name_to_check == row[0]:
            print_percentages(row)