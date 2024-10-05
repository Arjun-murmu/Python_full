#Q.1
def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word) > 0:
        # Complete the return statement using a string operation.
        return len(word)
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0

#Q2.
# Consider the following scenario about using Python lists: 

# A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list of students in 
# the order they arrived in the classroom. Aniyah was the first one to note which students arrived, and then Imani
# took over. After class, they each entered their lists into the computer and emailed them to the professor. 
# The professor wants to combine the two lists into one and sort it in alphabetical order. 
def alphabetize_lists(list1, list2):


  new_list = [] # Initialize a new list.
  combine_list = list1+list2 # Combine the lists.
  combine_list.sort() # Sort the combined lists.
  new_list = combine_list # Assign the combined lists to the "new_list".
  return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']

#Q3.
#Complete the for loop and string method needed in this function so that a function call like "alpha_length("This has 1 number in it")" will return the output "17". This function should:

def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for x in string: 
        # Complete the if-statement using a string method. 
        if x.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21

#Q4.
def increments(start, end):
    return [n+2 for n in range(start,end+1)] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#Q5.
def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for key,value in animal_dict.items(): 
        # Use a string method to format the required string.
        result += f"{key}\n"
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

#Q6
def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary 
    for guest in guest_list: # Iterate over the elements in the list 
        result[guest] = 0 # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}

#Q7
def setup_gradebook(old_gradebook):
    # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook. 
    for student in new_gradebook:
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[student] = 0
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}
