def arithmetic_arranger(problems, displayMode=False):
    first_operand_line = second_operand_line = dashes_line = result_line = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for index in range(len(problems)):
        problem = problems[index]
        [operand1, operator, operand2] = problem.split()

        # Error Handling
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        if not operand1.isnumeric() or not operand2.isnumeric():
            return "Error: Numbers must only contain digits."

        operand_max_length = max(len(operand1), len(operand2))
        before_line_spaces = operand_max_length + 2
        result_new_line = "\n"

        if index == 0:
            spaces_before_problem = ""
        else:
            spaces_before_problem = " " * 4
            result_new_line = ""

        first_operand_line += spaces_before_problem + operand1.rjust(before_line_spaces)
        second_operand_line += spaces_before_problem + operator + operand2.rjust(before_line_spaces - 1)
        dashes_line += spaces_before_problem + "-" * (before_line_spaces)

        if displayMode == True:
            result = int(operand1) + int(operand2) if operator == "+" else int(operand1) - int(operand2)
            result_line +=  result_new_line + spaces_before_problem + str(result).rjust(before_line_spaces)

    return first_operand_line + "\n" + second_operand_line + "\n" + dashes_line + result_line