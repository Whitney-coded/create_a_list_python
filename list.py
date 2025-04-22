# Step 1: Create an empty list
my_list = []  # This initializes an empty list called my_list

# Step 2: Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)  # Adds 10 to the end of the list
my_list.append(20)  # Adds 20 to the end of the list
my_list.append(30)  # Adds 30 to the end of the list
my_list.append(40)  # Adds 40 to the end of the list

# Now my_list = [10, 20, 30, 40]

# Step 3: Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Inserts 15 at index 1 (second position)

# Now my_list = [10, 15, 20, 30, 40]

# Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])  # Adds all elements of the second list to the end of my_list

# Now my_list = [10, 15, 20, 30, 40, 50, 60, 70]

# Step 5: Remove the last element from my_list
my_list.pop()  # Removes the last item (70) from the list

# Now my_list = [10, 15, 20, 30, 40, 50, 60]

# Step 6: Sort my_list in ascending order
my_list.sort()  # Sorts the list in increasing order

# Now my_list = [10, 15, 20, 30, 40, 50, 60]

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)  # Finds the index of 30
print("The index of 30 is:", index_of_30)  # Prints the index






