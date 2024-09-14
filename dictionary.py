#Dictionaries are another data structure in Python. They’re similar to a list in that they can be used to organize data into collections
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

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
  print(extension)
#   jpg
# txt
# csv
# py

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext))

# There are 10 files with the .jpg extension
# There are 14 files with the .txt extension
# There are 2 files with the .csv extension
# There are 23 files with the .py extension

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts.keys())
print(file_counts.values())

# dict_keys(['jpg', 'txt', 'csv', 'py'])
# dict_values([10, 14, 2, 23])

def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result
print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))

# {'a': 5}
# {'t': 2, 'e': 1, 'n': 2, 'a': 1}
# {'a': 2, ' ': 7, 'l': 3, 'o': 3, 'n': 2, 'g': 2, 's': 2, 't': 5, 'r': 2, 'i': 2, 'w': 1, 'h': 1, 'f': 1, 'e': 2}
