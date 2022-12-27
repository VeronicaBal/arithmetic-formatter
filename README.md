# Arithmetic Formatter
Program to arrange arithmetic problems vertically and side-by-side. If the second, optional argument is set to true, the answer will be displayed.

Examples:

Funciton call: 
```
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output: 
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function call with second argument:
```
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
````

Output with second argument:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```


This project is part of the freeCodeCamp's "Scientific Computing with Python" projects.
Instructions for building this project can be found [here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter).
