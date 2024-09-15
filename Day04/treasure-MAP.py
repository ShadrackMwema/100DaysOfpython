# Grid setup
Row1 = ["0", "3", "6"]
Row2 = ["4", "5", "6"]
Row3 = ["7", "8", "9"]

Map = [Row1, Row2, Row3]

# Display grid
print(f"{Row1}\n{Row2}\n{Row3}")

# Get position input (assuming user enters something like "12" for row 1, column 2)
position = input("Where do you want to place your marker (enter as row, column e.g. 12): ")

# Convert input into row and column indices
row = int(position[0]) - 1  # Adjust for 0-based indexing
col = int(position[1]) - 1  # Adjust for 0-based indexing

# Place the "X" at the specified position
Map[row][col] = "X"

# Display updated grid
print(f"{Row1}\n{Row2}\n{Row3}")
