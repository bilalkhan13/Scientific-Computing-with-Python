from logging import exception


def arithmetic_arranger(problems, displayMode=False):
    # Local Variables
    start = True
    first_operand_line = ""
    second_operand_line = ""
    dashes_line = ""
    output_line = ""

    try:
        if len(problems) > 5:
            raise InvalidProblemsCount
    except:
        return "Error: Too many problems."

# Main Loop
    for problem in problems:

        operand1 = splitFunc(problem, 'firstOperand')
        operator = splitFunc(problem, 'operator')
        operand2 = splitFunc(problem, 'secondOperand')

        # Exception Handling
        try:
            if len(operand1) > 4 or len(operand2) > 4:
                raise LargeOperandsLength
            if operator != "+" and operator != "-":
                raise NotAValidOperator
            if str(operand1).isnumeric() != True or str(operand2).isnumeric() != True:
                raise NotADigit

        except LargeOperandsLength:
            return "Error: Numbers cannot be more than four digits."

        except NotAValidOperator:
            return "Error: Operator must be '+' or '-'."

        except NotADigit:
            return "Error: Numbers must only contain digits."

        space = max(len(operand1), len(operand2))

        if start == True:
            first_operand_line += operand1.rjust(space+2)
            second_operand_line += operator + " " + operand2.rjust(space)
            dashes_line += "-" * (space + 2)
            if displayMode == True:
                if operator == "+":
                    output_line += str(int(operand1) +
                                       int(operand2)).rjust(space + 2)
                else:
                    output_line += str(int(operand1) -
                                       int(operand2)).rjust(space + 2)
            start = False
        else:
            first_operand_line += str(operand1).rjust(space+6)
            second_operand_line += str(operator).rjust(5) + \
                " " + str(operand2).rjust(space)
            dashes_line += "    " + "-" * (space+2)
            if displayMode == True:
                if operator == "+":
                    output_line += "    " + \
                        str(int(operand1) + int(operand2)).rjust(space + 2)
                else:
                    output_line += "    " + \
                        str(int(operand1) - int(operand2)).rjust(space + 2)

    # Display Output
    if displayMode == True:
        return first_operand_line + "\n" + second_operand_line + "\n" + dashes_line + "\n" + output_line
    return first_operand_line + "\n" + second_operand_line + "\n" + dashes_line

# Split Function


def splitFunc(problem, arg):
    split_problem = problem.split()
    if arg == "firstOperand":
        return split_problem[0]
    elif arg == "operator":
        return split_problem[1]
    else:
        return split_problem[2]

# Exception Classes


class Error (Exception):
    pass


class LargeOperandsLength(Error):
    pass


class NotAValidOperator(Error):
    pass


class InvalidProblemsCount(Error):
    pass


class NotADigit(Error):
    pass
