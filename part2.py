# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
#==================================================================================================
# Student ID: 20200616       
# Date:  16/04/2021
#==================================================================================================
# PART 2 - Student Version
#==================================================================================================

# Variables =======================================================================================
loop = True                                                                     # Boolean variable to decide while loop for Main Code                                                                    

# Functions =======================================================================================
def prompt_user():
    """This function prompts the user if they wish to continue or terminate the script.
          Function name : prompt_user
          Last modified: 16/04/2021 
          Author: Saadat Hamid Mansoor
    """
    global loop
    user_input = input("would you like to contine ? (yes/y or no/n): ").lower()
    if user_input == "no" or user_input == "n" :
       loop = False
       print("Ending script....")                                                  

def credit_input(type):
    """This function collects and returns the credit inputs (PASS, DEFER or FAIL) after checking if its an integer withing the range of accepted inputs.
          Function name : credit_input
          Last modified: 16/04/2021 
          Author: Saadat Hamid Mansoor
          
          Parameter:
              type (int): An integer value for PASS, DEFER or FAIL.
          Returns:
              int: An integer value for PASS, DEFER or FAIL.
    """
    try:
        credit = int(input(f"Please enter your credits at {type}\t: "))
        if credit not in range(0,140,20):
            print("Out of range")
            credit = credit_input(type)
    except ValueError:
        print("Integer required")
        credit = credit_input(type)
    return credit

def main():
    while loop == True:
      pass_credit = credit_input("pass")
      defer_credit = credit_input("defer")
      fail_credit = credit_input("fail")

      if pass_credit + defer_credit + fail_credit != 120:                           # Ensures all three Credit values add up to 120
        print("Total incorrect\n")
        continue
      elif pass_credit == 120:
        print("Progress\n")
        prompt_user()
        continue
      elif pass_credit == 100:
        print("Progress (module trailer)\n")
        prompt_user()
        continue
      elif fail_credit < 80:                                                        # Because for "Do not progress - Module Retriver" results, ALL the "FAIL Credit" values are below 80
        print("Do not progress - module retriever\n")
        prompt_user()
        continue
      elif fail_credit >= 80:                                                       # Because for "Exclude", ALL the "FAIL Credit" result values are equal to or above 80
        print("Exclude\n")
        prompt_user()
        continue
      else:
        print("Something went wrong... \n") 
        prompt_user()
    
# Main Code =======================================================================================
if __name__ == "__main__":
   main()
