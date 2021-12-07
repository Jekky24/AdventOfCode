# Import the .txt input file and save it as a file
with open("input_day06.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove whitespaces
# causing each iteration to output a string of numbers'123,123,123', then split on "," to return a list
input_list = [l.strip() for l in lines][0].split(",")

# Convert the input_list elements from strings to integers
input_list = [int(i) for i in input_list]

# Iterate through the loop for a total of 80 days
for day in range(80):
    # Iterate through each fish in input_list
    for i in range(len(input_list)):
        # If the fish is at life cycle day 0
        if input_list[i] == 0:
            # Change it back to day 6
            input_list[i] = 6
            # Also add a new lanternfish at life cycle day 8
            input_list.append(8)
        else:
            # Otherwise reduce life cycle by 1 day
            input_list[i] -= 1

# Print the total number of lanternfish in input_list on day 80
print(f"On day 80, there are a total of {len(input_list)} fish")
