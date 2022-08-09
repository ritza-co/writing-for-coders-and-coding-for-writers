# Instructions  
The material for this lesson is based on [Chapter 11: Lists](https://learnpythontherightway.com/chapter/chapter-11.html).

For this lesson, you will be required to complete the  exercises below. 

Make sure to write your solutions in the `main.py` file.

1.  What is the Python interpreter's response to the following?

```python
>>> list(range(10, 0, -2))
```

  The three arguments to the *range* function are *start*, *stop*, and *step*, respectively. In this example, `start` is greater than `stop`. What happens if `start < stop` and `step < 0`? Write a rule
  for the relationships among `start`, `stop`, and `step`.

2.  Consider this fragment of code:

```python
import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
```

  Does this fragment create one or two turtle instances? Does setting the color of `alex` also change the color of `tess`? Explain in detail.

3.  Draw a state snapshot for `a` and `b` before and after the third line of the following Python code is     
    executed:

```python
a = [1, 2, 3]
b = a[:]
b[0] = 5
```

4.  What will be the output of the following program?

```python
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))
```

Provide a *detailed* explanation of the results.

5.  Lists can be used to represent mathematical *vectors*. In this exercise and several that follow you will write functions to perform standard operations on vectors. Create a script named `vectors.py` and write Python code to pass the tests in each case.

Write a function `add_vectors(u, v)` that takes two lists of numbers of the same length, and returns a new list containing the sums of the corresponding elements of each:

```python
test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
```

6.  Write a function `scalar_mult(s, v)` that takes a number, `s`, and a list, `v` and returns the [scalar multiple](http://en.wikipedia.org/wiki/Scalar_multiple) of `v` by `s`:

```python
test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
```

7.  Write a function `dot_product(u, v)` that takes two lists of numbers of the same length, and returns the sum of the products of the corresponding elements of each (the [dot\_product](http://en.wikipedia.org/wiki/Dot_product)).

```python
test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
```

8.  **Extra challenge for the mathematically inclined**: Write a function `cross_product(u, v)` that takes two lists of numbers of length 3 and returns their [cross product](http://en.wikipedia.org/wiki/Cross_product). You should write your own tests.

9.  Describe the relationship between `" ".join(song.split())` and `song` in the fragment of code below. Are they the same for all strings assigned to `song`? When would they be different?

```python
song = "The rain in Spain..."
```

10. Write a function `replace(s, old, new)` that replaces all occurrences of `old` with `new` in a string `s`:

```python
test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
```

**Hint**: use the `split` and `join` methods.

11. Suppose you want to swap around the values in two variables. You decide to factor this out into a reusable function, and write this code:

```python
def swap(x, y):      # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)

a = ["This", "is", "fun"]
b = [2,3,4] 
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)
```

Run this program and describe the results. Oops! So it didn't do what you intended! Explain why not. Using a Python visualizer like the one at http://pythontutor.com may help you build a good conceptual model of what is going on. What will be the values of `a` and `b` after the call to `swap`?
