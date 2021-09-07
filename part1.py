# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
#==================================================================================================
# Student ID: 20200616       
# Date:  16/04/2021
#==================================================================================================
# PART 1 - Student Version
#==================================================================================================

# Functions =======================================================================================
def main():
    pass_credit = int(input("Please enter your credits at pass:\t"))
    defer_credit = int(input("Please enter your credits at defer:\t"))
    fail_credit = int(input("Please enter your credits at fail:\t"))

    if pass_credit == 120: 
      print("Progress")
    elif pass_credit == 100: 
      print("Progress (module trailer)")
    elif fail_credit < 80:                                                          # Because for "Do not progress - Module Retriver" results, ALL the "FAIL Credit" values are below 80 
      print("Do not progress - module retriever")
    elif fail_credit >= 80:                                                         # Because for "Exclude", ALL the "FAIL Credit" result values are equal to or above 80
      print("Exclude")
    else:
      print("Something went wrong... ")

# Main Code =======================================================================================
if __name__ == "__main__":
   main()