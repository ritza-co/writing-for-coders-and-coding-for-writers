# Instructions

The material for this lesson is based on [Chapter 5: Conditionals](https://learnpythontherightway.com/chapter/chapter-5.html).

For this lesson, you will be required to complete the exercises below. 

Make sure to write your solutions in the `main.py` file.

1. Assume the days of the week are numbered `0,1,2,3,4,5,6` from Sunday to Saturday. Write a function that is given the day number, and it returns the day name (a string).


2. You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a Wednesday). You return home after 137 periods of sleep. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of the day of the week you will return on.


3. Give the logical opposites of these conditions

    ```python
    a > b
    a >= b
    a >= 18  and  day == 3
    a >= 18  and  day != 3
    ```

4. What do these expressions evaluate to?

    ```python
    3 == 3
    3 != 3
    3 >= 4
    not (3 < 4)
    ```

5. Complete this truth table:

    | p | q | r | (not (p and q)) or r |
    | --- | --- | --- | --- |
    | F | F | F | ? |
    | F | F | T | ? |
    | F | T | F | ? |
    | F | T | T | ? |
    | T | F | F | ? |
    | T | F | T | ? |
    | T | T | F | ? |
    | T | T | T | ? |

6. Write a function that is given an exam mark, and it returns a string — the grade for that mark — according to this scheme:

    | Mark | Grade |
    | --- | --- |
    | >= 75 | First |
    | [70-75) | Upper Second |
    | [60-70) |	Second |
    | [50-60) |	Third |
    | [45-50) |	F1 Supp |
    | [40-45) |	F2 |
    | < 40 | F3 |

  The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So `39.99999` gets grade `F3`, but `40` gets grade `F2`. Assume

    ```python
    xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                        49.9, 45, 44.9, 40, 39.9, 2, 0]
    ```

  Test your function by printing the mark and the grade for all the elements in this list.


## Bonus Questions
7. Modify the turtle bar chart program so that the pen is up for the small gaps between each bar.


8. Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled with yellow, and bars representing values less than 100 are filled with green.


9. In the turtle bar chart program, what do you expect to happen if one or more of the data values in the list is negative? Try it out. Change the program so that when it prints the text value for the negative bars, it puts the text below the bottom of the bar.


10. Write a function `find_hypot` which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse. (*Hint: `x ** 0.5` will return the square root.*)


11. Write a function `is_rightangled` which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return `True` if the triangle is right-angled, or `False` otherwise.

  *Hint: Floating-point arithmetic is not always exactly accurate, so it is not safe to test floating-point numbers for equality. If a good programmer wants to know whether `x` is equal or close enough to `y`, they would probably code it up as:*

    ```python
    if  abs(x-y) < 0.000001:    # If x is approximately equal to y
        ...
    ```

12. Extend the above program so that the sides can be given to the function in any order.


13. If you’re intrigued by why floating-point arithmetic is sometimes inaccurate, on a piece of paper, divide 10 by 3 and write down the decimal result. You’ll find it does not terminate, so you’ll need an infinitely long sheet of paper. The representation of numbers in computer memory or on your calculator has similar problems: memory is finite, and some digits may have to be discarded. So small inaccuracies creep in. Try this script:

    ```python
    import math
    a = math.sqrt(2.0)
    print(a, a*a)
    print(a*a == 2.0)
    ```
