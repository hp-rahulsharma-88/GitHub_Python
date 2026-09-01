obj = [1, 2, 4, "rahul", 6.89] # List - can have different data types values

# For loop
for i in obj: #Iterate i for each value in given list obj
    print(i) # print each value of i
    print(i*2) # print each value of i multiply by 2

summ = 0
for j in range(1, 11): # Iterating j value from 1 to 11-1 i.e. 10 with by default increment of +1
    summ = summ + j
print("The sum of first ten natural number is",summ)

print("******************************")

for k in range(1, 11, 3): # jump with +3, Iterating from 1 to 10 (11-1)
    print(k)

print("******************************")
for m in range(10): # Iterating from 0 (by default) to 10-1 i.e. 9 with by default increment of +1
    print(m)