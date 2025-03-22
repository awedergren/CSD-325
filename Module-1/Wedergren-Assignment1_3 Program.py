# Amanda Wedergren
# March 21, 2025
# Module 1.3 Assignment

# Create the countdown and display the phrase for each iteration of the countdown.
def countdown_beer_bottles(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        bottles -= 1
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall.\n")

# Obtain and validate input for the countdown.
def main():
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles < 1:
            print("Please enter a number greater than 0.")
        else:
            countdown_beer_bottles(bottles)
            print("Time to buy more beer!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()