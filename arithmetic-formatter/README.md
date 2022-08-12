#Arithmetic Formatter

_Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:_
>  235
>+  52
>-----
_Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed._

##Example
_Function Call:
>arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

##Output:
>   32      3801      45      123
>+ 698    -    2    + 43    +  49
>-----    ------    ----    -----

##Function Call:
>arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

##Fore more detail please visit below mentioned link.
>https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter