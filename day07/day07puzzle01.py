# Import the .txt input file and save it as a file
with open("input_day07.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove whitespaces
# causing each iteration to output a string of numbers'123,123,123', then split on "," to return a list
input_list = [l.strip() for l in lines][0].split(",")

# Convert the input_list elements from strings to integers
input_list = [int(i) for i in input_list]

# Sort the list of integers in ascending order
input_list.sort()

# Creates a list of positions from the start of input_list to end of input_list
# incrementing in intervals of 1
positions = range(input_list[0], input_list[-1] + 1)

# Will store the fuel used for each position as a list. The index for that element
# will correspond to the the position the crabs moved towards
fuel_used_at_each_position = []

# Loop through all the possible positions
for position in positions:

    # Reset fuel used to get to this position back to 0 with each iteration
    fuel_used = 0

    # Loop through all the crabs in input_list
    for crab in input_list:
        # Calculate the difference between the crab's position and the final
        # position they are to move towards and add that to the total fuel_used
        fuel_used += abs(crab - position)

    # Add the total fuel_used for this position to the fuel_used_at_each_position list
    fuel_used_at_each_position.append(fuel_used)

# Grab the index value of the position with least fuel used and print this out
print(f"Position with least fuel used: {fuel_used_at_each_position.index(min(fuel_used_at_each_position))}")
# Print the fuel used to get to this position
print(f"Total fuel used to get to this position: {min(fuel_used_at_each_position)}")
