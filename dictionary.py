#dictionary
x = {}
print(type(x))

file_counts = {"txt":12,"jpg":23,"py":23,"csv":2,"cpp":10}
print(file_counts)

#count the dictinory
print(file_counts["csv"])
# check
print("txt" in file_counts)
print("g++" in file_counts)
#add new 
file_counts["c"] = 14
print(file_counts)
#update 
file_counts["csv"] = 22
print(file_counts)
# delete
del file_counts["jpg"]
print(file_counts)

# //output

# // <class 'dict'>
# // {'txt': 12, 'jpg': 23, 'py': 23, 'csv': 2, 'cpp': 10}
# // 2
# // True
# // False
# // {'txt': 12, 'jpg': 23, 'py': 23, 'csv': 2, 'cpp': 10, 'c': 14}
# // {'txt': 12, 'jpg': 23, 'py': 23, 'csv': 22, 'cpp': 10, 'c': 14}
# // {'txt': 12, 'py': 23, 'csv': 22, 'cpp': 10, 'c': 14}
