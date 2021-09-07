# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
#==================================================================================================
# Student ID: 20200616       
# Date:  16/04/2021
#==================================================================================================
# PART 3 - Staff Version With Histogram
#==================================================================================================

# Variables =======================================================================================
loop = True                                                                     # Boolean variable to decide while loop for Main Code

p_count = 0                                                                     # Count variable for number of Students with Progress
p_mt_count = 0                                                                  # Count variable for number of Students with Trailer
dnp_mr_count = 0                                                                # Count variable for number of Students with Retriever
e_count = 0                                                                     # Count variable for number of Students with Excluded

# Functions =======================================================================================
def prompt_user():
    """This function prompts the user if they wish to continue collecting data or terminate the script and display the results.
          Function name : prompt_user
          Last modified: 16/04/2021 
          Author: Saadat Hamid Mansoor
    """ 
    global loop
    user_input = input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ").lower()
    if user_input == "q" or user_input == "n" :
       loop = False
       print("Getting Results Ready ...\n")  
    else:
       print("")

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
        credit = int(input(f"Enter your total {type} credits\t: ")) 
        if credit not in range(0,140,20):
            print("Out of range")
            credit = credit_input(type)
    except ValueError:
        print("Integer required")
        credit = credit_input(type)
    return credit

def main():
    global p_count
    global p_mt_count
    global dnp_mr_count
    global e_count

    while loop == True:
      pass_credit = credit_input("PASS")     
      defer_credit = credit_input("DEFER")
      fail_credit = credit_input("FAIL")

      if pass_credit + defer_credit + fail_credit != 120:                            
        print("Total incorrect\n")
        continue
      elif pass_credit == 120:
        print("Progress\n")
        p_count += 1
        prompt_user()
        continue
      elif pass_credit == 100:
        print("Progress (module trailer)\n")
        p_mt_count += 1
        prompt_user()
        continue
      elif fail_credit < 80:                                                         # Because for "Do not progress - Module Retriver" results, ALL the "Fail Credit" values are below 80
        print("Do not progress - module retriever\n")
        dnp_mr_count += 1
        prompt_user()
        continue
      elif fail_credit >= 80:                                                        # Because for "Exclude", ALL the "Fail Credit" result values are equal to or above 80
        print("Exclude\n")
        e_count += 1
        prompt_user()
        continue
      else:
        print("Something went wrong...\n") 
        prompt_user()

    print("---------------------------------------------------------------")
    print("Horizontal Histogram")
    print("---------------------------------------------------------------")
    print(f"Progress {p_count}\t: {'*' * p_count}")
    print(f"Trailer {p_mt_count}\t: {'*' * p_mt_count}")
    print(f"Retriever {dnp_mr_count}\t: {'*' * dnp_mr_count}")
    print(f"Excluded {e_count}\t: {'*' * e_count}")
    print("---------------------------------------------------------------")
    print(f"{p_count + p_mt_count + dnp_mr_count + e_count} outcomes in total.")
    print("---------------------------------------------------------------")

# Main Code =======================================================================================
if __name__ == "__main__":
   main()
