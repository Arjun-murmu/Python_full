#instance (object) 
class name:
    def __init__(self):
        self.name1 = "Arjun"
        self.name2 = "Jaga"
nam = name()
print(nam.name2)

class name:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
#Modify variables
N_name = name("arjun", "jaga")
p_name = name("abinash", "uttam")
print(N_name.name1)
print(p_name.name2)

# __len__ returns the length of the object or collection.
# __contains__ tests whether the object contains an item.
# __eq__ tests whether two objects are equal.
