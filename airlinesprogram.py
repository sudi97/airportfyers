csv_file = input("Input File\n")
l = []
lst = []
i = 0
with open (csv_file,"r") as csv_file:
    
    for row in csv_file:
        ap_names = (row.split(",")[0])
        lst = l.append(ap_names)

d = {}
for i in l:
    if i not in d:
        d[i] = l.count(i)

print(" unique airport names and number of times it is repeated in a json format\n", d)

maxairport = max(d, key = d.get)
print("Airport Mentioned Heighest No of Times is:", maxairport)

minairport = min(d, key = d.get)
print("Airport Mentioned Least No of Times is:", minairport)
