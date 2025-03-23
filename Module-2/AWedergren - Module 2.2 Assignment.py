# Amanda Wedergren
# February 15, 2025
# Module 8.2 Assignment

# Create a program that includes a dictionary of stocks.
# Your dictionary should include at least 10 ticker symbols.
# The key should be the stock ticker symbol and the value
# should be the current price of the stock (the values can be fictional).
# Ask the user to enter a ticker symbol. Your program will search the
# dictionary for the ticker symbol and then print the ticker symbol and
# the stock price. If the ticker symbol is not located, print a message
# indicating that the ticker symbol was not found.

# Define the main function.
def main():
    print(' ')
    # Get the ticker symbol to search.
    ticker = input('Enter the ticker symbol: ')

    find_ticker(ticker)

    repeat_search()

# The get_ticker function creates a dictionary of stock ticker symbols and
# their values and checks to see if the user input is in the dictionary.
def find_ticker(ticker):
    # Create a dictionary of stock ticker symbols as keys and their value.
    stock = {'AMZN': '38.34', 'MSFT': '42.56', 'TSLA': '62.32', 'GS': '34.21',
             'GOOGL': '54.64', 'META': '38.26', 'TGT': '49.73', 'LUV': '49.28',
             'KO': '29.75', 'WMT': '39.75', 'WOOF': '32.67', 'HOG': '35.94'}

    # Test if the input is a valid value in the dictionary and print the
    # corresponding key and value, else print the error message.
    if ticker in stock:
        print(ticker, stock[ticker])
    else:
        print('Ticker symbol not found.')

# Function that asks the user if they want to search again. The program ends if N entered.
def repeat_search():
    print(' ')
    again = input('Press any key to search another ticker search or N to quit: ')
    while again == 'N':
        print('Thank you for searching!')
        quit()
    else:
        return main()

# Call the main function.
if __name__ == '__main__':
    main()