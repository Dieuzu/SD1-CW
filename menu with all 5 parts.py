# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#==================================================================================================
# Student ID: 20200616
# Date:  16/04/2021
#==================================================================================================
# Part 0 - Menu with ALL 5 Parts
#==================================================================================================
import importlib
import part1          
import part2
import part3
import part4
import part5

# Variables =======================================================================================
oloop = True                                                                     # Boolean variable to decide while loop for Main Code

# Functions =======================================================================================
def prompt_user():
    """This function prompts the user if they wish to Return to Menu or End the Full script.
          Function name : prompt_user
          Last modified: 16/04/2021 
          Author: Saadat Hamid Mansoor
    """ 
    global oloop
    user_input = input("Press any key to return to Main Menu Or 'N'/'Q' to Quit : ").lower()
    if user_input == "q" or user_input == "n" :
       oloop = False
       print("Ending full script! Thank you for trying it out!")  
    else:
       print(" ")
       main()
       
def reloader(mod):                                                               # Reference : https://docs.python.org/3/library/importlib.html#importlib.reload
    """This function reloads any imported modules
          Function name : reloader
          Last modified: 16/04/2021 
          Author: Saadat Hamid Mansoor

          Parameter:
            mod (module): A Module like part2 or part3 or part4.
    """
    importlib.reload(mod)  

def main():
    global oloop
    
    print("|===================================================================|")
    print("|                Software Development I – Coursework                |")
    print("|                     By : Saadat Hamid Mansoor                     |")
    print("|===================================================================|")
    print("|Student ID: 20200616                                               |")
    print("|Date:  16/04/2021                                                  |")
    print("|===================================================================|")
    print("|                              Options                              |")
    print("|-------------------------------------------------------------------|")
    print("|  Input 1 : for [Part 1 - Student Version]                         |")
    print("|  Input 2 : for [Part 2 - Student Version (Validation)]            |")
    print("|  Input 3 : for [Part 3 - Staff Version With Horizontal Histogram] |")
    print("|  Input 4 : for [Part 4 - Staff Version With Vertical Histogram]   |")
    print("|  Input 5 : for [Part 5 - Alternative Staff Version]               |")
    print("|  Input 6 : to  [Quit Script]                                      |")
    print("|-------------------------------------------------------------------|")
    option = int(input("Select your Option : "))
    if option == 1:
        print("[Part 1 - Student Version] Selected\n")
        part1.main()                                                             # Reference : https://docs.python.org/3/tutorial/modules.html [ also used in line 73, 80, 87, and 93 ]
        print(" ")
        prompt_user()
    elif option == 2:
        print("[Part 2 - Student Version (Validation)] Selected\n")
        part2.main()
        reloader(part2) 
        print(" ")
        prompt_user()
    elif option == 3:
        loop = True
        print("[Part 3 - Staff Version With Horizontal Histogram] Selected\n")
        part3.main()
        reloader(part3)
        print(" ")
        prompt_user()
    elif option == 4:
        loop = True
        print("[Part 4 - Staff Version With Vertical Histogram] Selected\n")
        part4.main()
        reloader(part4)
        print(" ")
        prompt_user()
    elif option == 5:
        print("[Part 5 - Alternative Staff Version] Selected\n")
        part5.main()
        print(" ")
        prompt_user()
    elif option ==6:
        print("Ending full script! Thank you for trying it out!")
        oloop = False
    else:
        print("Invalid Input Enterd!\n")
                                                
# Main Code =================================================================================================================================================================
while oloop == True:
    try :
        main()
    except ValueError:
       print ("The Input you enterd is not a valid numerical value!\n")             
