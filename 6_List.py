values = [1, 2, "rahul", 5.67, 22] # Can contain different data type values
print(values) # [1, 2, 'rahul', 5.67, 22]

print(values[0]) # 1
print(values[-1]) # Last Index Value 22
values.append("End") # at the last
values.append(2025) # at the last
print(values) # [1, 2, 'rahul', 5.67, 22, 'End', 2025]
values.insert(3, "sharma")
print(values) # [1, 2, 'rahul', 'sharma', 5.67, 22, 'End', 2025]
values[2] = "RAHUL" # Update value
values[3] = "SHARMA" # Update value
print(values) # [1, 2, 'RAHUL', 'SHARMA', 5.67, 22, 'End', 2025]

del values[-1]
del values[0]
print(values) # [2, 'RAHUL', 'SHARMA', 5.67, 22, 'End']
print(values[1:4]) # ['RAHUL', 'SHARMA', 5.67] - Subset of given list from 1 to 4-1 = 3