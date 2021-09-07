# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
#==================================================================================================
# Student ID: 20200616       
# Date:  16/04/2021
#==================================================================================================
# PART 5 - Alternative Staff Version 
#==================================================================================================

# Variables =======================================================================================
result = [                                                                      # Two-dimensional list where each sub list has credit values in the order [Pass, Defer, Fail]
          [120,0,0],
          [100,20,0],
          [100,0,20],
          [80,20,20],
          [60,40,20],
          [40,40,40],
          [20,40,60],
          [20,20,80],
          [20,0,100],
          [0,0,120],
         ]
          
p_count = 0                                                                     # Count variable for number of Students with Progress
p_mt_count = 0                                                                  # Count variable for number of Students with Trailer
dnp_mr_count = 0                                                                # Count variable for number of Students with Retriever
e_count = 0                                                                     # Count variable for number of Students with Excluded

# Functions =======================================================================================
def credits(pass_credit = 0, defer_credit = 0, fail_credit = 0):
    """This function Reads a list within the result list and extracts the PASS, DEFER and FAIL credits, and then determins the apropriate final result.
            Function name : credits
            Last modified: 16/04/2021 
            Author: Saadat Hamid Mansoor

            Parameter:
              pass_credit (int): Integer value for PASS credit. Defaults to 0.
              defer_credit (int): Integer value for DEFER credit. Defaults to 0.
              fail_credit (int): Integer value for FAIL credit. Defaults to 0.

            Returns:
              str: Appropriate string value for final result.
    """
    global p_count
    global p_mt_count
    global dnp_mr_count
    global e_count

    if pass_credit + defer_credit + fail_credit != 120:                            
      return "Total incorrect"
    elif pass_credit == 120:
      p_count += 1
      return "Progress"
      
    elif pass_credit == 100:
      p_mt_count += 1
      return "Progress (module trailer)"
    elif fail_credit < 80:                                                    # Because for "Do not progress - Module Retriver" results, ALL the "Fail Credit" values are below 80
      dnp_mr_count += 1
      return "Do not progress - module retriever"
    elif fail_credit >= 80:                                                   # Because for "Exclude", ALL the "Fail Credit" result values are equal to or above 80
      e_count += 1
      return "Exclude"
    else:
      return "Something went wrong..."

def main():
    for i in result:
        print(credits(i[0], i[1], i[2]))

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