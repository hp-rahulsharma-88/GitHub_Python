values = (1, 3, "Rahul", "Sharma", 22.01)
print(values) # (1, 3, 'Rahul', 'Sharma', 22.01)
print(values[1]) # 3
#values[2] = "RAHUL" - Can't update that's why Tuple is immutable compare to List
print(values[4]) # 22.01
print(values[-1]) # 22.01 - last value
print(values[2:4]) # ('Rahul', 'Sharma') - Subset of given Tuple

# del values[-1] - doesn't support item deletion
# values.insert(4,"Tester") - 'tuple' object has no attribute 'insert'
# values.append(2025) - 'tuple' object has no attribute 'append'
print(values) # (1, 3, 'Rahul', 'Sharma', 22.01)
