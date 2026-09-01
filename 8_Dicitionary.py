Dic = {"a": 22, 2:"abcd", "c" : "220187", 4: 22.01} # key: value
print(Dic) # {'a': 22, 2: 'abcd', 'c': '22', 4: 22.01}
print(Dic["a"]) # 22
print(Dic[2]) # abcd
print(Dic["c"]) # 220187
print(Dic[4]) # 22.01

Dict = {} # Blank Dictionary

print(Dict) # {}
# adding values in Dictionary at Run Time
Dict["FirstName"] = "John"
Dict["LastName"] = "Doe"
Dict["DOB"] = "22Jan1987"
Dict[49] = "New York"
print(Dict) # {'FirstName': 'John', 'LastName': 'Doe', 'DOB': '22Jan1987', 49: 'New York'}