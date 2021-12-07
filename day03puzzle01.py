# Import the Counter class from collections library
from collections import Counter

# Import the .txt input file and save it as a file
with open("input_day03.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove whitespaces
# causing each iteration to output a string of numbers'000110011011'
input_list = [l.strip() for l in lines]

# Create a list of empty strings
# Number of empty strings in the list is set to input_list's first element's length
combined_string = ["" for a in range(len(input_list[0]))]

# Iterate through input_list with the iteration times set to input_list's first element's length
for i in range(len(input_list[0])):
    # Each iteration, iterate through each element of input_list
    for y in range(len(input_list)):
        # Append the i'th number of each element in input_list to the combined_string's i'th string
        combined_string[i] += input_list[y][i]

# Set the gamma_rate and epsilon_rate as blank strings
gamma_rate = ""
epsilon_rate = ""

# Iterate through combined_string with the iteration times set to input_list's first element's length
for i in range(len(input_list[0])):
    # Initialise the Counter class and store in count
    count = Counter(combined_string[i])
    # gamma_rate is set to the most common number in the combined_string's i'th element
    gamma_rate += count.most_common(2)[0][0]
    # epsilon_rate is set to the least common number in the combined_string's i'th element
    epsilon_rate += count.most_common(2)[1][0]

# Convert the binary string values of gamma_rate and epsilon_rate to integer values
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

# Print with formatted string literal to display the gamma_rate, epsilon_rate and the product of the two as required by the puzzle
print(f"Gamma rate: {gamma_rate}\nEpsilon Rate: {epsilon_rate}\nPower Consumption: {gamma_rate*epsilon_rate}")
