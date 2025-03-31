# Amanda Wedergren
# March 31, 2025
# Module 4.2 Assignment

import csv
from datetime import datetime

from matplotlib import pyplot as plt

import sys


# Create a menu.
def display_menu():
    print("Menu:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")


def highs():
    print("You selected Highs.")
    # Get dates and high temperatures from this file.
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, highs = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)

    # Plot the high temperatures.
    # plt.style.use('seaborn')

    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def lows():
    print("You selected Lows.")
    # Get dates and low temperatures from this file.
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, lows = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            low = int(row[6])
            lows.append(low)

    # Plot the low temperatures.
    # plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    # Format plot.
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Get user's choice from the menu.
def main():
    while True:
        display_menu()
        choice = input("Please choose daily temperatures to plot or exit (1-3): ")

        if choice == '1':
            highs()
        elif choice == '2':
            lows()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()