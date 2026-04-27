rows = int(input("Enter no of rows: "))
array = []

for i in range(1, rows + 1):
    arr = []
    for j in range(1, i + 1):
        a = int(input(f"Enter element for row {i}, col {j}: "))
        arr.append(a)
    array.append(arr)

for i in range(rows - 2, -1, -1):
    for j in range(len(array[i])):
        array[i][j] += max(array[i+1][j], array[i+1][j+1])

print("The largest path sum is:", array[0][0])
