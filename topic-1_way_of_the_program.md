# Instructions  
The material for this lesson is based on [Chapter 1: The way of the program](https://learnpythontherightway.com/chapter/chapter-1.html).

For this lesson, you will be required to complete the exercises below. 

Write your code solutions in  the `main.py` file. If necessary, create additional files under the "Files" section.

1. Write an English sentence with understandable semantics but incorrect syntax. Write another English sentence which has correct syntax but has semantic errors.


2. Using the Python interpreter, type `1 + 2` and then hit return. Python evaluates this expression, displays the result, and then shows another prompt. `*` is the multiplication operator, and `**` is the exponentiation operator. Experiment by entering different expressions and recording what is displayed by the Python interpreter.


3. Type `1 2` and then hit return. Python tries to evaluate the expression, but it can’t because the expression is not syntactically legal. Instead, it shows the error message:

    ```python
    File "<interactive input>", line 1
        1 2
          ^
    SyntaxError: invalid syntax
    ```

In many cases, Python indicates where the syntax error occurred, but it is not always right, and it doesn’t give you much information about what is wrong.

So, for the most part, the burden is on you to learn the syntax rules.

In this case, Python is complaining because there is no operator between the numbers.

See if you can find a few more examples of things that will produce error messages when you enter them at the Python prompt. Write down what you enter at the prompt and the last line of the error message that Python reports back to you.


4. Type `print("hello")`. Python executes this, which has the effect of printing the letters h-e-l-l-o. Notice that the quotation marks that you used to enclose the string are not part of the output. Now type `"hello"` and describe your result. Make notes of when you see the quotation marks and when you don’t.


5. Type cheese without the quotation marks. The output will look something like this:

    ```python
    Traceback (most recent call last):
      File "<interactive input>", line 1, in ?
    NameError: name 'cheese' is not defined
    ```

This is a run-time error; specifically, it is a NameError, and even more specifically, it is an error because the name cheese is not defined. If you don’t know what that means yet, you will soon.


6. Type 6 + 4 * 9 at the Python prompt and hit enter. Record what happens.

Now create a Python script with the following contents:

  ```python
  6 + 4 * 9
  ```

What happens when you run this script? Now change the script contents to:


  ```python
  print(6 + 4 * 9)
  ```
and run it again.

What happened this time?

Whenever an expression is typed at the Python prompt, it is evaluated and the result is automatically shown on the line below. (Like on your calculator, if you type this expression you’ll get the result 42.)

A script is different, however. Evaluations of expressions are not automatically displayed, so it is necessary to use the **print** function to make the answer show up.

It is hardly ever necessary to use the print function in immediate mode at the command prompt.
