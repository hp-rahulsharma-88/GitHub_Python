str1 = "RahulSharma.com.in"
str2 = " Learning Python "
str3 = "Rahul"

print(str1[3]) # u
print(str1[0:5]) # Rahul - substring
print(str2) # Learning Python
var1 = str2.strip() # Remove left and right space from the string
print(var1) #Learning Python
print(str2.lstrip()) #Learning Python (Remove left space from the string)
print(str2.rstrip()) # Learning Python(Remove right space from the string)

print(str1 + str2) #RahulSharma.com.in Learning Python

print(str3 in str1) #True

var = str1.split(".") #str1 = "RahulSharma.com.in" (a list would create on the basis of .)
print(var) #['RahulSharma', 'com', 'in']
print(var[0]) #RahulSharma
print(var[2]) #in