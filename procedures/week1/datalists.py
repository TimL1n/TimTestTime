# Datalists hack task -------------------------------
InfoDb = []

InfoDb.append({  
               "Name": "Timothy Lin",  
               "Birth": "November 10",
               "Siblings": "Yes",
               "Hobbies":["Basketball", "Anime", "Driving", "Gaming"]  
              })  

InfoDb.append({  
               "Name": "Nathan Shih",  
               "Birth": "November 12",
               "Siblings": "Yes",
               "Hobbies":["Coding", "Fishing", "Driving", "Gaming"]  
              })  

InfoDb.append({  
               "Name": "Diego Rodriguez",  
               "Birth": "July 28",
               "Siblings": "Yes",
               "Hobbies":["Sleeping", "Gaming", "Music", "Anime"] 
              })

InfoDb.append({  
               "Name": "Nicholas Genovese",  
               "Birth": "May 7",
               "Siblings": "Yes",
               "Hobbies":["Soccer", "Anime", "YouTube", "Music"] 
              })

# Datalist to print using the three loops - for - while - recursion

InfoDbLoop = []

InfoDbLoop.append({  
               "Name": "Timothy Lin",  
               "Birth": "November 10",
               "Siblings": "Yes",
               "Hobbies":["Basketball", "Sleeping", "Driving", "Gaming"]  
              })  

InfoDbLoop.append({  
               "Name": "Nathan Shih",  
               "Birth": "November 12",
               "Siblings": "Yes",
               "Hobbies":["Coding", "Fishing", "Driving", "Gaming"]  
              })  

InfoDbLoop.append({  
               "Name": "Diego Rodriguez",  
               "Birth": "July 28",
               "Siblings": "Yes",
               "Hobbies":["Sleeping", "Gaming", "Music", "Anime"] 
              })

InfoDb.append({  
               "Name": "Nicholas Genovese",  
               "Birth": "May 7",
               "Siblings": "Yes",
               "Hobbies":["Soccer", "Anime", "YouTube", "Music"] 
              })

def print_data(n):
  print(InfoDbLoop[n]["Name"])  # print name
  print("\t", "Sport: ", end="")
  print(InfoDbLoop[n]["Sport"])
  print("\t", "Age: ", end="")  # \t is a tab indent, end="" make sure no return occurs
  print(InfoDbLoop[n]["Age"])
  print("\t", "Hobbies: ", end="")
  print(", ".join(InfoDbLoop[n]["Hobbies"]))  # join allows printing a string list with separator
  print()


# Dataloops hack task ------------------------------------

# For Loop
def for_loop():
  for n in range(len(InfoDbLoop)):
    print_data(n)

# While Loop
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
  while n < len(InfoDbLoop):
    print_data(n)
    n += 1
  return

# Recursion
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
  if n < len(InfoDbLoop):
    print_data(n)
    recursive_loop(n + 1)
  return # exit condition

def main():
  print("THIS IS THE FOR LOOP PRINTING")
  for_loop()
  print("THIS IS THE WHILE LOOP PRINTING")
  while_loop(0)
  print("THIS IS RECURSION PRINTING")
  recursive_loop(0)