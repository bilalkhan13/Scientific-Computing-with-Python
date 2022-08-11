from logging import exception


def arithmetic_arranger(problems, displayMode=False):

    status = True
    first_operand_line = ""
    second_operand_line = ""
    dashes_line = ""
    result_line = ""
    spaces_before_result = "    "

    for problem in problems:
        [operand1, operator, operand2] = problem.split()

        # Exception Handling
        if len(problems) > 5:
            return "Error: Too many problems."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if str(operand1).isnumeric() != True or str(operand2).isnumeric() != True:
            return "Error: Numbers must only contain digits."

        alignment_space = max(len(operand1), len(operand2))

        if status == True:
            first_operand_line += operand1.rjust(alignment_space+2)
            second_operand_line += operator + " " + \
                operand2.rjust(alignment_space)
            dashes_line += "-" * (alignment_space + 2)
            if displayMode == True:
                if operator == "+":
                    result_line += add_operands(problem, alignment_space)
                else:
                    result_line += subtract_operands(problem, alignment_space)
            status = False
        else:
            first_operand_line += str(operand1).rjust(alignment_space+6)
            second_operand_line += str(operator).rjust(5) + \
                " " + str(operand2).rjust(alignment_space)
            dashes_line += spaces_before_result + "-" * (alignment_space+2)
            if displayMode == True:
                if operator == "+":
                    result_line += spaces_before_result + \
                        add_operands(problem, alignment_space)
                else:
                    result_line += spaces_before_result + \
                        subtract_operands(problem, alignment_space)

    problems_output = first_operand_line + "\n" + \
        second_operand_line + "\n" + dashes_line
    # Display Output
    if displayMode == True:
        return problems_output + "\n" + result_line
    return problems_output


def add_operands(problem, alignment_space):
    [operand1, operator, operand2] = problem.split()
    return str(int(operand1) + int(operand2)).rjust(alignment_space + 2)


def subtract_operands(problem, alignment_space):
    [operand1, operator, operand2] = problem.split()
    return str(int(operand1) - int(operand2)).rjust(alignment_space + 2)
