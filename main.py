def main():
  import os
  ans=True
  while ans:
      print("""
      1. Week 0 Key Learnings
      2. Week 1 Key Learnings
      Z. Exit/Quit
      """)
      ans=input("What would you like to do? ")
      import time
      def ocean_print():
        # print ocean
        print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
        print("\n\n\n\n")
        print(OCEAN_COLOR + "  " * 35)
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
              ship_print(position)
              time.sleep(.1)
      if ans=="1":
        ans2=True
        while ans2:
          print("""
      a. Ship Pattern
      b. Print random serial numbers
      c. Build a Christmas Tree
      Z. Exit/Quit
      """)
          ans2=input("What would you like to do? ")
          if ans2=="a":
            ANSI_CLEAR_SCREEN = u"\u001B[2J"
            ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
            OCEAN_COLOR = u"\u001B[44m\u001B[2D"
            SHIP_COLOR = u"\u001B[32m\u001B[2D"
            RESET_COLOR = u"\u001B[0m\u001B[2D"
            ship()
            quit=input("Do you want to go back to the main menu? (yes/no)")

            if quit=="yes":
              os.system('clear')
              main()
            else:
              print("Staying put")
  
            
          
          elif ans2=="b":
            print("\n4LPJ-4N6J-DDQ7-VUMEMMKM-7GZJ-6XGQ-DSJ5ZJT9-4NXX-4SQH-MTSJBBYD-7T8P-GG8T-YKXVNMAJ-XYSN-DFV6-HESUBE7Z-QH4L-E398-P7G3V7Z8-P4D5-SNTX-U93TS5VA-X4FX-8SXK-U9VH2CTM-X6C8-HKMC-4S77PR53-MLLU-TEYV-UJ94PH25-MTLA-95TG-45M96QX9-5XVB-S88L-ASPAPALP-3P2C-5KUV-GPFTU4T4-8DX8-K8WV-ZJNZ9R93-99ST-R87H-MREJBZNR-TXS3-2QPV-2YWTF5UY-K3VS-JUVV-6DDA7T9W-3JNF-94C4-D325CGYX-A3UP-PEG2-HW3LJFGL-2RSM-P9TJ-9PUP58FK-6RDQ-SSNE-L9YRXVE5-KE6E-7V6V-6S6YBCCG-2FVQ-XPE9-2U5DFYLM-ERYQ-4QLL-7XDX7XYG-ZJQ4-5FRF-WVWFSRT7-HND6-VF5B-UFBEDDUN-MGS4-LAJJ-RYFK6W85-JA9W-6ELL-XUEYK6T5-EJNH-GMBE-JVDBKEUL-PT5K-E6T7-RAKLW74X-25TB-5CJ6-UQ3LMEYK-68GC-YZAD-FGVQX4Q7-CV6N-PZKZ-VBZV4QWD-U49Q-LKC4-9FZRGM7F-PHA3-2WYD-EHPZ5ZSF-GY65-GJQQ-828A8G4R-BGKW-BWE5-4FRUGUL7-UKWY-3KZD-V4A34BGG-BAEM-3RK9-YZUQWX2C-3DG4-RH7Y-ZLF9JK4N-RZQX-QUH6-X25KSLXC-ZG7F-4WQN-C9R2QYTA-2E5D-2PMD-V5WDREFP-FWE8-XLQW-H3ULQGMG-R7CP-J2RH-FNWXM9V7-GGPZ-L3GV-6JCXY38L-97BQ-E4LN-74K2D2E3-J9R3-FK64-QE2R5W92-KTPG-SZHN-5PQGVTFL-X5KG-CY8F-8MJYMVLU-B4TP-6PXH-BVC6KLPJ-DGBF-KVKT-YBYP885K-5C7G-9D6Y-QUDA8AS4-3MLF-VU3N-4LFNEX3L-AJ27-JAQX-QH96F3DF-8W4R-9QRC-XL6TLA67-XTCW-2G94-BFMACJDS-JZ7E-HDFP-HAKLKRH7-SVMN-CYYX-9TSCFZVD-XCMS-JEUD-PBF3PUXE-N7T7-Y9EK-4VNJBEX5-FDKT-Z43G-FCNMHCGW-GBBY-JK7D-4KNJHDFW-YG63-HTKS-W4NF9ME7-6X8K-5HS9-WY4UHTJ7-ZGLM-JJC6-286FFD7R-V9HD-XUBZ-GQEBHSN9-SA3K-9SVW-9BUD9ER9-KKSV-4AWX-MVZWNFMS-A3DY-TZC8-PA237TY2-ATRY-XCME-H7Z88GZC-G3KJ-USHW-6735WGVF-R699-98W2-EAA4WB7D-LRMM-M5B4-XE3S8ZV8-FGLL-VUA6-JYKSGZNZ-QGLH-S2NE-XEKFEL84-GTPQ-8J4X-LLGJ2MYD-LRAA-4NKG-SP26Z3PN-B26K-3UWU-MFKP6Y43-46FM-QM5N-YU6MVVGK-BTMN-6AGW-WTYE2F5Y-YCTE-BQZ5-S27RDKV3-UZS5-Y6LS-4NUZX8HN-8E36-BUWY-A7JZE6EW-HSYW-RUPJ-KWBKYAE5-9M32-YTAC-U83XTETF-E2XS-LV2J-EKBC7FKU-VVXB-NWD3-94V686QP-2G3M-5JHB-79H95HVW-PJAE-9ERD-KS9X5VFR-5N42-XVRM-CK8V92HQ-LK3H-NBMV-KKRU9LG5-NH8J-FQRB-B8VEWZLB-TARA-8YJ8-89ZHMBLL-EAWZ-K9KJ-D94GE3HX-29H2-QYLV-GJB8RL62-AK3Q-SZZL-YRU988N9-HKXH-68CC-LB45C3S7-AUJE-9CVP-52M42SUA-C49U-S9YV-U284")
            quit=input("Do you want to go back to the main menu? (yes/no) ")

            if quit=="yes":
              os.system('clear')
              main()
            else:
              print("Staying put")
        
  
          elif ans2=="c":
            def triangleShape(n):
              for i in range(n):
                  for j in range(n-i):
                      print(' ', end=' ')
                  for k in range(2*i+1):
                      print('*',end=' ')
                  print()
        
        # Generating Pole Shape
            def poleShape(n):
              for i in range(n):
                  for j in range(n-1):
                      print(' ', end=' ')
                  print('* * *')
        
        # Input and Function Call
            row = int(input('Enter number of rows: '))
        
            triangleShape(row)
            triangleShape(row)
            poleShape(row)
            quit=input("Do you want to go back to the main menu? (yes/no) ")
  
            if quit=="yes":
              os.system('clear')
              main()
            else:
              print("Staying put")

      if ans=="2":
        ans3=True
        while ans3:
          print("""
      a. InfoDB lists
      b. InfoDB loops
      c. Fibonacci
      Z. Exit/Quit
      """)
          ans3=input("What would you like to do? ")
          if ans3=="a":
            print("\nDisplaying InfoDB List now.\n")
            InfoDb = []
            InfoDb.append({  
               "FirstName": "Colin",  
               "LastName": "Howard",  
               "DOB": "March 14th",  
               "Residence": "Poway, CA",  
               "Email": "colinh36220@stu.powayusd.com",  
               "hobbies":["Cooking","Video Games","Playing Music"]  
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
              
          elif ans3=="b":
            InfoDb = []
            InfoDb.append({  
               "FirstName": "Colin",  
               "LastName": "Howard",  
               "DOB": "March 14th",  
               "Residence": "Poway",  
               "Email": "colinh36220@stu.powayusd.com",  
               "hobbies":["Cooking","Video Games","Playing Music"]  
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
            def for_loop():
              for n in range(len(InfoDb)):
                print_data(n)
            def while_loop(p):
              while p < len(InfoDb):
                print_data(p)
                p += 1
              return
            def recursive_loop(b):
              if b < len(InfoDb):
                print_data(b)
                recursive_loop(b + 1)
              return 
            def program():
              print("----------------------------------------")
              print("For loop\n")
              for_loop()
              print("----------------------------------------")
              print("While loop\n")
              while_loop(0)
              print("----------------------------------------")
              print("Recursive loop\n")
              recursive_loop(0)
              print("----------------------------------------")
            program()
            quit=input("Do you want to go back to the main menu? (yes/no) ")

            if quit=="yes":
              os.system('clear')
              main()
            else:
              print("Staying put")
          elif ans3=="c":
            def fibo_recur(n):

             if n <= 1:
               return n  
             else:
               return(fibo_recur(n-1) + fibo_recur(n-2))

            fibo = int(input("How many series would you like? "))

            if fibo <= 0:  
              print("Error. You have to put in a positive integer. ")
            else:   
              print("Fibonacci of ",fibo," is :")
              for i in range(fibo):  
                print(fibo_recur(i)) 
      elif ans=="Z":
        print("/n Goodbye")
        break
main()