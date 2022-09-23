# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 18676673
# Date: 07/12/2021


#program starts here
rangeMarks = [0, 20, 40, 60, 80, 100, 120] #stores marks that are acceptable
x = 0
y = 0

#class prog_funcs starts here
class prog_funcs:
     #New Method below
     def retry(self,question="\nWould you like to try again ? (yes/no)\n"):
          '''Allows the user to have another chance to input data in case if the input is not acceptable.
               Variables :
                    Local :
                         ansyn : reads user input to determine the continuation 
                    Global :
                         y : Used to control the while loop
                         x : Used to identify the first time user enters data 
          '''
          global x,y
          ansyn = input(question).lower()
          if question == "\nWould you like to try again ? (yes/no)\n":
               if ansyn == "yes":
                    y = 0
               elif ansyn == "no":
                    if x == 0:
                         if userOption == "4":
                              import os
                              if os.path.exists("progressionData.txt"):
                                   print(f"\n{80 * '-'}\n")
                                   with open("progressionData.txt", "r") as poData: 
                                         for num,line in enumerate(poData):
                                             print(f"{num + 1}.{line}")
                                   quit()
                              else:
                                   print(f"\n{15 * '-'}\nPROGRAM ENDED !\n{15 * '-'}")
                                   quit()
                         else:
                              print(f"\n{15 * '-'}\nPROGRAM ENDED !\n{15 * '-'}")
                              quit()
                    else:
                         y = 1
               else:
                    if x != 0:
                         print("Undefined option selected. Cannot proceed with the selected request.")
                         y = 1
                    else:
                         print(f"\nUndefined option selected. Cannot proceed with the selected request.\n{15 * '-'}\nPROGRAM ENDED !\n{15 * '-'}")
                         quit()
          else:
               if ansyn == "y":
                    y = 0
               elif ansyn == "q":
                    y = 1
               else:
                    if x != 0:
                         print("Undefined option selected. Cannot proceed with the selected request.")
                         y = 1
                    else:
                         print(f"\nUndefined option selected. Cannot proceed with the selected request.\n{15 * '-'}\nPROGRAM ENDED !\n{15 * '-'}")
                         quit()

     #New Method below
     def repeat_input(self):
          '''Gets required user input and checks whether the input is acceptable. If not acceptable, it redirects to the retry method. If acceptable inputs will be assigned to variables.
               Variables :
                    Global :
                         y : controls the while loop
                         x : identify the first time user enters data, keeps count of the number of times user enters data
                         passMark : User input assigned variable
                         deferMark : User input assigned variable
                         failMark : User input assigned variable
          '''
          global y, x, passMark, deferMark, failMark
          try:
               passMark = int(input("\nEnter your total PASS credits : "))
               if passMark not in rangeMarks:
                    print("Out of range")
                    self.retry()
               else:
                    deferMark = int(input("Enter your total DEFER credits : "))
                    if deferMark not in rangeMarks:
                         print("Out of range")
                         self.retry()
                    else:
                         failMark = int(input("Enter your total FAIL credits : "))
                         if failMark not in rangeMarks:
                              print("Out of range")
                              self.retry()
                         elif passMark + deferMark + failMark != 120 and failMark in rangeMarks:
                              print("Total Incorrect.")
                              self.retry()
                         else:
                              y = 2 #This is the confirmation that the user input is an acceptable one. It will allow the user input to go through progression outcome prediction conditions.
                              x += 1 #Keeps count of the number of times user inputs data and allows to determine if the user is entering data for the first time.
          except ValueError:
               print("Integer Required.")
               self.retry()

     #New Method below
     def condition(self):
          '''Introduces the conditions and prints the value accordingly.
               Variables :
                    Global :
                         pCount,tCount,eCount,rCount : Stores the number of times each progression outcome is displayed.
          '''
          global pCount, tCount, eCount, rCount
          if passMark == 120:
               print("\nProgress")
               pCount += 1
          elif passMark == 100:
               print("\nProgress(module trailer)")
               tCount += 1
          elif passMark <= 40 and failMark >= 80:
               print("\nExclude")
               eCount += 1
          else:
               print("\nModule retriever")
               rCount += 1

     #New Method below
     def condition_adv(self):
          '''Introduces the conditions and prints the value accordingly while appending the progression outcome to each list.
               Variables :
                    Global :
                         pCount,tCount,eCount,rCount : Stores the number of times each progression outcome is displayed.
          '''
          global pCount, tCount, eCount, rCount
          if passMark == 120:
               print("\nProgress")
               progress.append(f"Progress - {passMark}, {deferMark}, {failMark}")
               pCount += 1
          elif passMark == 100:
               print("\nProgress(module trailer)")
               trailer.append(f"Progress(module trailer) - {passMark}, {deferMark}, {failMark}")
               tCount += 1
          elif passMark <= 40 and failMark >= 80:
               print("\nExclude")
               excluded.append(f"Exclude - {passMark}, {deferMark}, {failMark}")
               eCount += 1
          else:
               print("\nModule retriever")
               retriever.append(f"Module retriever - {passMark}, {deferMark}, {failMark}")
               rCount += 1

     #New Method below
     def horzprint(self):
          '''Prints a horizontal histogram of each progression outcome.
               Variables :
                    Global :
                         pCount,tCount,eCount,rCount : Stores the number of times each progression outcome is displayed.
          '''
          global pCount, tCount, eCount, rCount
          print(f"\nHORIZONTAL HISTOGRAM\n{'-' * 20}\n \nProgress {pCount} : {pCount * '*'}\nTrailer {tCount} : {tCount * '*'}\nRetriever {rCount} : {rCount * '*'}\nExcluded {eCount} : {eCount * '*'}")
          print(f"\n{x} outcomes in total.")

     #New Method below
     def vertprint(self):
          '''Prints a vertical histogram of each progression outcome.
               Variables :
                    Global :
                         pCount,tCount,eCount,rCount : Stores the number of times each progression outcome is displayed.
                    Local :
                         totCount : pCount + tCount + eCount + rCount
          '''
          global pCount, tCount, eCount, rCount
          print(f"\nVERTICAL HISTOGRAM\n{'-' * 18}\n \nProgress {pCount} | Trailer {tCount} | Retriever {rCount} | Exclude {eCount}")
          for z in range(max(pCount, tCount, rCount, eCount)):
               if pCount != 0:
                    print(f"{'*':>6}",end="")
                    pCount -= 1
               else:
                    print(f"{' ':>6}",end="")
               if tCount != 0:
                    print(f"{'*':>12}",end="")
                    tCount -= 1
               else:
                    print(f"{' ':>12}",end="")
               if rCount != 0:
                    print(f"{'*':>13}",end="")
                    rCount -= 1
               else:
                    print(f"{' ':>13}",end="")
               if eCount != 0:
                    print(f"{'*':>12}")
                    eCount -= 1
               else:
                    print(" ")
          print(f"\n{x} outcomes in total")
#class prog_funcs ends here

obj = prog_funcs()
try:
     userOption = input("Welcome to the Student Progression Program. Select one of the options below.(1/2/3/4)\n \t1.Student Version\\Staff Version(Horizontal Histogram)\n\t2.Staff Version(Vertical Histogram)\n\t3.Staff Version(Data Stored on Lists)\n\t4.Staff Version(Save progression to a text file)\nYour Option : ")
     print(80 * "-")

     #Part 1 starts here
     if userOption == "1":
          selectUser = input("Which of the following are you ?\n\t1.Student\n\t2.Staff\nSelect an option above (1/2) : ") #User input is received to determine Student or Staff version should be executed

          #Part 1 - Sub part 1 - Student version starts here
          if selectUser == "1":
               while y < 1:
                    try:
                         passMark = int(input("\nPlease enter your credit at pass : "))
                         if passMark not in rangeMarks:
                              print("Out of range")
                              obj.retry() #Allows user to enter data again if mistakently entered an unacceptable data.
                         else:
                              deferMark = int(input("Please enter your credit at defer : "))
                              if deferMark not in rangeMarks:
                                   print("Out of range")
                                   obj.retry()
                              else:
                                   failMark = int(input("Please enter your credit at fail : "))
                                   if failMark not in rangeMarks:
                                        print("Out of range")
                                        obj.retry()
                                   elif passMark + deferMark + failMark != 120 and failMark in rangeMarks:
                                        print("Total Incorrect.")
                                        obj.retry()
                                   else:
                                        y = 2 #this is the confirmation that the user input is an acceptable one. It will allow the user input to go through progression outcome prediction conditions.
                                        x += 1 #Keeps count of the number of times user inputs data and allows to determine if the user is entering data for the first time.
                    except ValueError:
                         print("Integer Required.")
                         obj.retry()
               if y == 2:
                    if passMark == 120:
                         print("\nProgress")
                    elif passMark == 100:
                         print("\nProgress(module trailer)")
                    elif passMark <= 40 and failMark >= 80:
                         print("\nExclude")
                    else:
                         print("\nModule retriever")
          #Part 1 - Sub part 1 - Student version ends here

          #Part 1 - Sub part 2 - Staff version starts here
          elif selectUser == "2":
               pCount = 0
               tCount = 0
               rCount = 0
               eCount = 0
               while y != 1:
                    while y < 1:
                         obj.repeat_input() #user input is taken repeatedly until user wants to stop
                    if y == 2:
                         obj.condition() #predicts progression outcome
                         obj.retry("\nWould you like to enter another set of data?\nEnter 'y' to proceed or 'q' to quit and view results : ") 
               print(80 * "-")
               obj.horzprint() #prints horizontal histogram of progression outcomes
          #Part 1 - Sub part 2 - Staff version ends here
          else:
               print("Invalid option selected") #this line is executed when an invalid option is selected in the student/staff menu
     #Part 1 ends here

     #Part 2 starts here
     elif userOption == "2":
          pCount = 0
          tCount = 0
          rCount = 0
          eCount = 0
          while y != 1:
               while y < 1:
                    obj.repeat_input()
               if y == 2:
                    obj.condition()
                    obj.retry("\nWould you like to enter another set of data?\nEnter 'y' to proceed or 'q' to quit and view results : ")
          print(80 * "-")
          obj.horzprint()
          print(80 * "-")
          obj.vertprint() #prints a vertical histogram of progression outcomes
     #Part 2 ends here

     #Part 3 starts here
     elif userOption == "3":
          pCount = 0
          tCount = 0
          rCount = 0
          eCount = 0
          progress = []
          trailer = []
          retriever = []
          excluded = []
          while y != 1:
               while y < 1:
                    obj.repeat_input()
               if y == 2:          
                    obj.condition_adv() #predicts progression outcome while appendinf data to a list
                    obj.retry("\nWould you like to enter another set of data?\nEnter 'y' to proceed or 'q' to quit and view results : ")
          print(80 * "-")
          obj.horzprint()
          print(80 * "-")
          obj.vertprint()
          print(80 * "-")
          print(f"\nSUMMARY OF PROGRESSION\n{'-' * 22}")
          for el in progress:
               print(">",el)
          for el in trailer:
               print(">",el)
          for el in retriever:
               print(">",el)
          for el in excluded:
               print(">",el)
     #Part 3 ends here

     #Part 4 starts here
     elif userOption == "4":
          pCount = 0
          tCount = 0
          rCount = 0
          eCount = 0
          progress = []
          trailer = []
          retriever = []
          excluded = []
          while y != 1:
               while y < 1:
                    obj.repeat_input()
               if y == 2:
                    obj.condition_adv()
                    obj.retry("\nWould you like to enter another set of data?\nEnter 'y' to proceed or 'q' to quit and view results : ")
          print(80 * "-")
          obj.horzprint()
          print(80 * "-")
          obj.vertprint()
          print(80 * "-")
          with open("progressionData.txt", "a") as poData: #append mode
               print(f"\nSUMMARY OF PROGRESSION\n{'-' * 22}")
               for el in progress:
                    print(">",el)
                    poData.write(f"{el}\n")
               for el in trailer:
                    print(">",el)
                    poData.write(f"{el}\n")
               for el in retriever:
                    print(">",el)
                    poData.write(f"{el}\n")
               for el in excluded:
                    print(">",el)
                    poData.write(f"{el}\n")
          print(f"\n{'-' * 64}\nProgression data have been successfully written to a text file !\n{'-' * 64}\n")
          print(f"{80 * '-'}\n\nDATA FROM THE TEXT FILE\n{23 * '-'}")
          with open("progressionData.txt", "r") as poData: #read mode
               for num,line in enumerate(poData):
                    print(f"{num + 1}.{line}")
     #Part 4 ends here
               
     else:
          print("Invalid option selected") #this line is executed when an invalid option is selected in the main menu
except KeyboardInterrupt:
     print("\nPROGRAM ENDED DUE TO A KEYBOARD INTERRUPTION.")
#program ends here
