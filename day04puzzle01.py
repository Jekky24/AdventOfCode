# Import the .txt input file and save it as a file
with open("input_day04_numbers.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove whitespaces
# causing each iteration to output a string of numbers'000110011011'
numbers = lines[0].strip().split(",")

with open("input_day04_boards.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

boards = [l.strip().split() for l in lines]
print(boards)
