# Import the Counter class from collections library
from collections import Counter

# Import the .txt input file and save it as a file
with open("input_day06.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove whitespaces
# causing each iteration to output a string of numbers'123,123,123', then split on "," to return a list
input_list = [l.strip() for l in lines][0].split(",")

# Convert the input_list elements from strings to integers
input_list = [int(i) for i in input_list]

# Initialise the Counter class on input_list so the number of lanternfish of each life cycle day
# can be calculated
count = Counter(input_list)

# Create a dictionary to group the total number of lanternfish at each life cycle day
# A "temp" grouping is needed as each group of lanternfish is shuffled down a life cycle day
lanternfish_grouped = {"temp": 0, 0: 0, 1: count[1], 2: count[2], 3: count[3], 4: count[4], 5: count[5], 6: 0, 7: 0, 8: 0}

# Iterate through the loop a total of 256 days
for i in range(256):
    # Shuffle each group of lanternfish down 1 life cycle day, storing the day 0 group in the
    # "temp" group before moving this value to day 8 to reflect new lanternfish being created.
    # The original day 0 group is then also added to the day 6 groups as they restart their
    # life cycle.
    lanternfish_grouped["temp"] = lanternfish_grouped[0]
    lanternfish_grouped[0] = lanternfish_grouped[1]
    lanternfish_grouped[1] = lanternfish_grouped[2]
    lanternfish_grouped[2] = lanternfish_grouped[3]
    lanternfish_grouped[3] = lanternfish_grouped[4]
    lanternfish_grouped[4] = lanternfish_grouped[5]
    lanternfish_grouped[5] = lanternfish_grouped[6]
    lanternfish_grouped[6] = lanternfish_grouped[7]
    lanternfish_grouped[7] = lanternfish_grouped[8]
    lanternfish_grouped[8] = lanternfish_grouped["temp"]
    lanternfish_grouped[6] += lanternfish_grouped["temp"]

# Create total_lanternfish to add all the lanternfish groupings together
total_lanternfish = 0

# Iterate through the lanternfish_grouped dictionary from key values 1 to 8
for i in range(9):
    # Add the number of lanternfish in each life cycle day grouping to the total
    total_lanternfish += lanternfish_grouped[i]

# Print the total number of lanternfish on day 256
print(f"The total number of fish on day 256 is {total_lanternfish}")
