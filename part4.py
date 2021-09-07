# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
#==================================================================================================
# Student ID: 20200616       
# Date:  16/04/2021
#==================================================================================================
# PART 4 - Staff Version With Vertical Histogram
#==================================================================================================

# Variables =======================================================================================
loop = True                                                                     # Boolean variable to decide while loop for Main Code
p_count = 0                                                                     # Count variable for number of Students with Progress
p_mt_count = 0                                                                  # Count variable for number of Students with Trailer
dnp_mr_count = 0                                                                # Count variable for number of Students with Retriever
e_count = 0                                                                     # Count variable for number of Students with Excluded

# Functions =======================================================================================
def prompt_user():
    """This function prompts the user if they wish to continue collecting Data or terminate the script and display the results.
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
      elif fail_credit < 80:                                                    # Because for "Do not progress - Module Retriver" results, ALL the "Fail Credit" values are below 80
        print("Do not progress - module retriever\n")
        dnp_mr_count += 1
        prompt_user()
        continue
      elif fail_credit >= 80:                                                   # Because for "Exclude", ALL the "Fail Credit" result values are equal to or above 80
        print("Exclude\n")
        e_count += 1
        prompt_user()
        continue
      else:
        print("Something went wrong...\n") 
        prompt_user()

    print("|===============================================|")
    print("|              Vertical Histogram               |")
    print("|-----------------------------------------------|")
    print("|  Progress | Trailing  | Retriever | Excluded  |")
    print(f"|{p_count:^11}|{p_mt_count:^11}|{dnp_mr_count:^11}|{e_count:^11}|")  # Refference : algnments in "Format Specification Mini-Language" from : https://docs.python.org/3/library/string.html
    print("|-----------------------------------------------|")
    star_1= p_count                                                              # Backup Variable to hold value of p_count
    star_2= p_mt_count                                                           # Backup Variable to hold value of p_mt_count
    star_3= dnp_mr_count                                                         # Backup Variable to hold value of dnp_mr_count
    star_4= e_count                                                              # Backup Variable to hold value of e_count
    while star_1 > 0 or star_2 > 0 or star_3 > 0 or star_4 > 0:
            a = " "                                                              # Variable to hold "*" or " " for Progress Column
            b = " "                                                              # Variable to hold "*" or " " for Trailer Column
            c = " "                                                              # Variable to hold "*" or " " for Retriever Column
            d = " "                                                              # Variable to hold "*" or " " for Excluded Column

            if star_1 > 0:
              a = "*"
              star_1 -= 1
              
            if star_2 > 0:
              b = "*"
              star_2 -= 1

            if star_3 > 0:
              c = "*"
              star_3 -= 1

            if star_4 > 0:
              d = "*"
              star_4 -= 1

            print(f"|{a:^11}|{b:^11}|{c:^11}|{d:^11}|")                          # Design to print neat rows in the format : |     *     |     *     |     *     |     *     |
    print("|-----------------------------------------------|")
    print(f"| Total number of Outcomes : {p_count + p_mt_count + dnp_mr_count + e_count:<19}|") 
    print("|===============================================|")

# Main Code =======================================================================================
if __name__ == "__main__":
   main()