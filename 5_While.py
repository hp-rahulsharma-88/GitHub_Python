it = 10

while it>1:
    if it == 9:
        it = it-1 # 8
        continue # skip rest loop execution from line no 7 to 10 for this iteration (it==9) only
    if it == 3:
        break # jump out from the loop when if condition matches
    print(it) # 10, 8, 7, 6, 5, 4
    it = it-1

print("While loop execution is done")