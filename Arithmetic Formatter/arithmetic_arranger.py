def error_checking(operand1, operator, operand):
    try:
        if len(num1) > 4 or len(num2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits"

    try:
        if operator != "+" and operator != "-":
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."

    try:
        if operand1 != True or operand2 != True:
            raise BaseException
    except:
        return "Error: Numbers must only contain digits."
    return " "


def arithmetic_arranger(arr):
    try:
        if len(arr) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    result = 0
    res_display = ""
    line1 = ""
    line2 = ""
    line3 = ""
    space = "------"

    for problem in arr:
        split_problem = problem.split()
        operand1 = split_problem[0]
        operator = split_problem[1]
        operand2 = split_problem[2]
        e = error_checking(operand1, operator, operand2)
        if e != " ":
            return e

        line1 += operand1.rjust(10, " ")
        line2 += operator.rjust(6, " ") + " " + operand2.rjust(3, " ")
        line3 += space.rjust(10, " ")
        print()
        if operator == "+":
            result = int(operand1) + int(operand2)
            result = str(result)
            res_display += result.rjust(10, " ")
        else:
            result = int(operand1) - int(operand2)
            result = str(result)
            res_display += result.rjust(10, " ")

    print(line1)
    print(line2)
    print(line3)
    print(res_display)
    return ""
