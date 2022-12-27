def compute_answer(problem_list):
  if problem_list[1] == "+":
    answer = int(problem_list[0]) + int(problem_list[2])
  else: #It's a subtraction
    answer = int(problem_list[0]) - int(problem_list[2])
  return str(answer)