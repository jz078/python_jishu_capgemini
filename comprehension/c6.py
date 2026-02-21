# from a dictionary, create a new dictionary with students scoring >= 60.

dict1 = {
    "ram":70, 
    "sham":80, 
    "rohit":46, 
    "rahul":59, 
    "priya": 71, 
    "Aman": 75,
    "Riya": 55,
    "Rahul": 62,
    "Neha": 48,
    "Karan": 81}

# dict2 = {i : x if x>=60 for i in dict1}
dict2 = {name:marks for name, marks in dict1.items() if marks >= 60}

print(dict2)