# Instructions  

The material for this lesson is based on [Chapter 20: Dictionaries](https://learnpythontherightway.com/chapter/chapter-20.html).

For this lesson, you will be required to complete the  exercises below. 

Make sure to write your solutions in the `main.py` file.

1. Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample output of the program when the user enters the data “ThiS is String with Upper and lower case Letters”, would look this:
```python
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
```

2. Give the Python interpreter’s response to each of the following from a continuous interpreter session:
```python
>>> d = {"apples": 15, "bananas": 35, "grapes": 12}
>>> d["bananas"]
```
```python
>>> d["oranges"] = 20
>>> len(d)
```
```python
>>> "grapes" in d
```
```python
>>> d["pears"]
```
```python
>>> d.get("pears", 0)
```
```python
>>> fruits = list(d.keys())
>>> fruits.sort()
>>> print(fruits)
```
```python
>>> del d["apples"]
>>> "apples" in d
```

Be sure you understand why you get each result. Then apply what you have learned to fill in the body of the function below:
```python
def add_fruit(inventory, fruit, quantity=0): 
    return

# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)  
```


## Bonus Questions
3. Write a program called `alice_words.py` that creates a text file named `alice_words.txt` containing an alphabetical listing of all the words, and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland. (You can obtain a free plain text version of the book, along with many others, from http://www.gutenberg.org.) The first 10 lines of your output file should look something like this:

  # Word Count
  a 631 a-piece 1 abide 1 able 1 about 94 above 3 absence 1 absurd 2

  How many times does the word `alice` occur in the book?


4. What is the longest word in Alice in Wonderland? How many characters does it have?
