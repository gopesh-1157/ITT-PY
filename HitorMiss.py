# Take input from user
my = input("my string: ")
guess = input("guess string: ")

# h → count of exact matches (same position)
# n → count of near matches (difference of 1)
h = 0
n = 0

# To avoid counting duplicates
arr = []

# Loop through each character
for i in range(len(my)):
    
    # Check for exact match (same position)
    if my[i] == guess[i]:
        h = h + 1
    
    # Check if digits differ by 1 (near match)
    elif (int(my[i]) - int(guess[i])) == 1 or (int(my[i]) - int(guess[i])) == -1:
        
        # Ensure we don't count duplicates
        if my[i] not in arr:
            arr.append(my[i])
            n = n + 1
    
    else:
        continue  # skip if no condition matches

# Print result
print(h, 'H', n, 'N')
