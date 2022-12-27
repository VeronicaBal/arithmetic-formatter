#Function that adds white spaces and creates dashes depending on length of each number in the computation

def arranged_string(problem_list, arranged_problems, *answer):
  
  first_number = problem_list[0]
  sign = problem_list[1]
  second_number = problem_list[2]

  if len(first_number) == len(second_number):
    first_line = "  " + first_number #Add two white spaces
    second_line = sign + " " + second_number #Add one white space btw sign and number
    third_line = "-" * (len(first_number) + 2) #Number of dashes = length first number + the two white spaces
  
  elif len(first_number) > len(second_number):
    length_difference = len(first_number)-len(second_number)
    first_line = "  " + first_number #Add two white spaces
    second_line = sign + " "*(length_difference+1) + second_number
    third_line = "-" * (len(first_number) + 2) #Number of dashes = length first number + the two white spaces
  
  elif len(second_number) > len(first_number):
    length_difference = len(second_number)-len(first_number)
    first_line = " "*(length_difference+2) + first_number
    second_line = sign + " " + second_number #Add one white space btw sign and number
    third_line = "-" * (len(second_number)+2) #Number of dashes = length second number + sign + white space

    
  arranged_problems["first_lines"] = arranged_problems["first_lines"] + first_line + "    "
  arranged_problems["second_lines"] = arranged_problems["second_lines"] + second_line + "    "
  arranged_problems["third_lines"] = arranged_problems["third_lines"] + third_line + "    "

  if answer:
    answer = "".join(answer[0]) #Answer is a tuple, transform into a string
    line_difference = len(second_line) - len(answer)
    fourth_line = " " * line_difference + answer
    arranged_problems["fourth_lines"] = arranged_problems["fourth_lines"] + fourth_line + "    "
  
  return arranged_problems