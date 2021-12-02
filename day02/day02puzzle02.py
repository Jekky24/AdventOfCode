# Import the .txt input file and save it as a file
with open("input_day02.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove whitespaces
# causing each iteration to output a string 'forward 6'
# The .split method will change the output to a list of strings ['forward', '6']
movements = [(l.strip().split()) for l in lines]

# Set initial forward, depth and aim values
forward = 0
depth = 0
aim = 0

# Iterate through all motiion elements (format: ['direction', 'amount']) in
# the movements list and checks the direction of the motion before adding the
# amount to either forward or depth counters
for motion in movements:
    # If motion is forward:
    #   - Add amount to the forward counter
    #   - Add amount * aim to the depth counter
    if motion[0] == "forward":
        forward += int(motion[1])
        depth += int(motion[1]) * aim
    # If motion if down, add to the aim counter
    elif motion[0] == "down":
        aim += int(motion[1])
    # Otherwise motion must be up, deduct from the aim counter
    else:
        aim -= int(motion[1])

# Print with formatted string literal to display the total forward movement,
# total depth movement and the product of the two as required by the puzzle
print(f"Forward: {forward}. Depth: {depth}. Product: {forward * depth}")
