def arithmetic_arranger(problems,solve=False):
  import re
  if len(problems)>5:
    return 'Error: Too many problems.'
  #Defining variables for each line 
  top_line=""
  bottom_line=""
  dash_line=""
  solution_line=""
  arranged_line=''
  for problem in problems:
    new=problem.split()
    num=new[0]
    operator=new[1]
    den=new[2]
    
    if operator=="*" or operator=="/":
      return "Error: Operator must be '+' or '-'."

    if re.search("[^\d]",num) or re.search("[^\d\+\-]",den):
        return "Error: Numbers must only contain digits."
    if len(num)>4 or len(den)>4:
      return 'Error: Numbers cannot be more than four digits.'

    #answer
    answer=''
    if operator=='+':
      answer=str(int(num)+int(den))
    else:
      answer=str(int(num)-int(den))
    line_length=max(len(num),len(den))+2
    
    numerator_line=""
    numerator_line = str(num.rjust(line_length))
  
    denominator_line=""
    denominator_line =str(operator) + str(den.rjust(line_length - 
    1))
  
    dash=""
    for p in range(line_length):
      dash +="-"
  
    answer_line=""
    answer_line += answer.rjust(line_length)  
  
#Arranging each line starts
    if problem != problems[-1]:
      top_line += numerator_line + "    "
      bottom_line += denominator_line + "    "
      dash_line += dash + "    "
      solution_line += answer_line + "    "
    else:
      top_line += numerator_line 
      bottom_line += denominator_line 
      dash_line += dash 
      solution_line += answer_line

  if solve==True:
    arranged_peoblem = top_line + "\n" + bottom_line + "\n" + dash_line + "\n" + solution_line
  else:
    arranged_problem = top_line + "\n" + bottom_line + "\n" + dash_line
  return arranged_problem


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
