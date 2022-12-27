from arranged_string import arranged_string
from catch_errors import catch_errors
from compute_answer import compute_answer


def arithmetic_arranger(problems, *answer):
  
    if len(problems) > 5:
        return "Error: Too many problems."
      
    else:  #Create an empty object to store arranged lines   
      arranged_problems = {
        "first_lines": "", 
        "second_lines": "", 
        "third_lines": "",
        "fourth_lines": ""
      }
      
      for problem in problems:
        problem_list = problem.split(" ")

        #See if any of the condition is not met
        error = catch_errors(problem_list)
        if error:
          return error

        if answer:
          fourth_line = compute_answer(problem_list)
          arranged_problems = arranged_string(problem_list, arranged_problems, fourth_line)
        else:
          arranged_problems = arranged_string(problem_list, arranged_problems)

      #Concatenate all the problems line by line and remove trailing spaces
      result = arranged_problems["first_lines"].rstrip() + "\n" + arranged_problems["second_lines"].rstrip() + "\n" + arranged_problems["third_lines"].rstrip() 
      
      if answer:
        result = result +"\n" + arranged_problems["fourth_lines"].rstrip()
      
      return result

