# Program: Count words, lines, and characters in a text file
# Allows user to add new text and view updated counts

# Ask the user for a file name
filename = input("Enter the file name: ")

# Step 1: Try to open the file (create if it doesn't exist)
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    # If file doesn’t exist, create it
    print("File not found — creating a new one.")
    open(filename, 'w').close()
    lines = []

# Step 2: Display initial statistics
num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)
num_chars = sum(len(line) for line in lines)

print("\n📊 Current File Statistics:")
print(f"Lines: {num_lines}")
print(f"Words: {num_words}")
print(f"Characters: {num_chars}")

# Step 3: Ask user to add new lines
print("\n✍️ Enter new lines of text (type 'STOP' to finish):")
with open(filename, 'a') as file:
    while True:
        new_line = input()
        if new_line.strip().upper() == "STOP":
            break
        file.write(new_line + '\n')

# Step 4: Recalculate and display updated statistics
with open(filename, 'r') as file:
    lines = file.readlines()

num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)
num_chars = sum(len(line) for line in lines)

print("\n✅ Updated File Statistics:")
print(f"Lines: {num_lines}")
print(f"Words: {num_words}")
print(f"Characters: {num_chars}")
