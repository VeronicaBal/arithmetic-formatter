def catch_errors(problem_list):
  if problem_list[1] != "+" and problem_list[1] != "-":
    return "Error: Operator must be '+' or '-'."
  if not problem_list[0].isdigit() or not problem_list[2].isdigit():
    return "Error: Numbers must only contain digits."
  if len(problem_list[0]) > 4 or len(problem_list[2]) > 4:
    return "Error: Numbers cannot be more than four digits."