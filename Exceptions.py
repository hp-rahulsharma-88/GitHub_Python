CART = 0

# if CART != 2:
#     raise Exception("CART should be equal to 2")

#assert(CART == 0) # If condition false then throwing assertion error else pass the test case

# Condition 1
try:
    with open('filelog.txt', 'r') as reader: # incorrect file so it will throw an exception
        reader.read()

except:
    print("Customized Exception or Error")

# Condition 2
try:
    with open('filelog.txt', 'r') as reader: # incorrect file so it will throw an exception
        reader.read()

except Exception as msg: # real python msg about this exception
    print(msg)

finally:
    print("try block failed and except section triggered")

# Condition 3
try:
    with open('test.txt', 'r') as reader: # correct file so will not throw any exception
        reader.read()

except:
    print("Except Block")

finally:
    print("try block passed and except section didn't trigger")