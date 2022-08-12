def arithmetic_arranger(problems, displayMode=False):
    first_operand_line = second_operand_line = dashes_line = ""
    result_line = ""

    for index in range(len(problems)):
        problem = problems[index]
        [operand1, operator, operand2] = problem.split()

        # Error Handling
        if len(problems) > 5:
            return "Error: Too many problems."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if not operand1.isnumeric() or not operand2.isnumeric():
            return "Error: Numbers must only contain digits."

        operand_max_length = max(len(operand1), len(operand2))
        if index == 0:
            first_line_before_spaces = operand_max_length+2
            second_line_before_spaces = operand_max_length + 1
            before_operator_Spaces = 0
            dashes_line_before_spaces = operand_max_length+2
            spaces_before_result = ""
            result_new_line = "\n"
        else:
            first_line_before_spaces = operand_max_length+6
            second_line_before_spaces = operand_max_length+1
            before_operator_Spaces = 5
            dashes_line_before_spaces = operand_max_length+2
            spaces_before_result = " " * 4
            result_new_line = ""

        first_operand_line += operand1.rjust(first_line_before_spaces)
        second_operand_line += operator.rjust(before_operator_Spaces) + operand2.rjust(second_line_before_spaces)
        dashes_line += spaces_before_result + "-" * (dashes_line_before_spaces)
        if displayMode == True:
            result_line += result_new_line
            result_line += spaces_before_result + str(int(operand1) + int(operand2)).rjust(
                dashes_line_before_spaces) if operator == "+" else spaces_before_result+str(int(operand1) - int(operand2)).rjust(dashes_line_before_spaces)

    return first_operand_line + "\n" + second_operand_line + "\n" + dashes_line + result_line