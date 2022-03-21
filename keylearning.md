
## Code Snippets

Static and Animated Patterns
```html
    # print ship with colors and leading spaces
    def ship_print(position):
        print(ANSI_HOME_CURSOR)
        print(RESET_COLOR)
        sp = " " * position
        print(sp + "    |\   ")
        print(sp + "    |/   ")
        print(SHIP_COLOR, end="")
        print(sp + "\__ |__/ ")
        print(sp + " \____/  ")
        print(RESET_COLOR)


    # ship function, iterface into this file
    def ship():
        # only need to print ocean once
        ocean_print()
    
        # loop control variables
        start = 0  # start at zero
        distance = 60  # how many times to repeat
        step = 2  # count by 2
    
        # loop purpose is to animate ship sailing
        for position in range(start, distance, step):
            ship_print(position)  # call to function with parameter
            time.sleep(.1)

    if ans=="1":
      ANSI_CLEAR_SCREEN = u"\u001B[2J"
      ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
      OCEAN_COLOR = u"\u001B[44m\u001B[2D"
      SHIP_COLOR = u"\u001B[32m\u001B[2D"
      RESET_COLOR = u"\u001B[0m\u001B[2D"

      ship()
```

Info DB Lists
```html
          if ans3=="a":
            print("\nDisplaying InfoDB List now.\n")
            InfoDb = []
            InfoDb.append({  
               "FirstName": "Timothy",  
               "LastName": "Lin",  
               "DOB": "November 10th",  
               "Residence": "San Diego, CA",  
               "Email": "timothyzlin@gmail.com",  
               "hobbies":["Eating Food","Video Games","Listening to Music"]  
              }) 
            def print_data(n):
              print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
              print("\n")
              print(InfoDb[n]["DOB"])
              print("\n")
              print(InfoDb[n]["Residence"])
              print("\n")
              print(InfoDb[n]["Email"])
              print("\n")
              print("My Hobbies: ", end="") 
              print(", ".join(InfoDb[n]["hobbies"]))
              print()
            print_data(0)
            quit=input("Do you want to go back to the main menu? (yes/no) ")

            if quit=="yes":
              os.system('clear')
              main()
            else:
              print("Staying put")
```
