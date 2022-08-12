

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

        operand_max_length = max(len(operand1), len(operand2))

        if status == True:
            first_operand_line += operand1.rjust(operand_max_length+2)
            second_operand_line += operator + " " + \
                operand2.rjust(operand_max_length)
            dashes_line += "-" * (operand_max_length + 2)
            if displayMode == True:
                result_line += display_mode(problem,
                                            operator, operand_max_length)
            status = False
        else:
            first_operand_line += str(operand1).rjust(operand_max_length+6)
            second_operand_line += str(operator).rjust(5) + \
                " " + str(operand2).rjust(operand_max_length)
            dashes_line += spaces_before_result + "-" * (operand_max_length+2)
            if displayMode == True:
                result_line += spaces_before_result + \
                    display_mode(problem, operator, operand_max_length)

    problems_output = first_operand_line + "\n" + \
        second_operand_line + "\n" + dashes_line
    # Display Output
    if displayMode == True:
        return problems_output + "\n" + result_line
    return problems_output


def display_mode(problem, operator, operand_max_length):
    return str(add_operands(problem)).rjust(operand_max_length+2) if operator == "+" else str(subtract_operands(problem)).rjust(operand_max_length+2)


def add_operands(problem):
    [operand1, operator, operand2] = problem.split()
    return str(int(operand1) + int(operand2))


def subtract_operands(problem):
    [operand1, operator, operand2] = problem.split()
    return str(int(operand1) - int(operand2))
