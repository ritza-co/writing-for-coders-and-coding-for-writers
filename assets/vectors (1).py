import sys, math

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# Question 5
def add_vectors(u, v):
  """ Function takes two lists of numbers of the same length, and returns a new list containing the sums of the corresponding elements of each """
  sum_list = []
  for i,j in zip(u,v):
    sum_list.append(i + j)
  return sum_list


# Question 6
def scalar_mult(s,v):
  """ Function takes a number, s, and a list, v and returns the scalar multiple of v by s """
  mult_list = []
  for i in v:
    mult_list.append(s * i)
  return mult_list


# Question 7
def dot_product(u, v):
  """ Function takes two lists of numbers of the same length, and returns the sum of the products of the corresponding elements of each """
  sum = dot = 0
  for i, j in zip(u, v):
    dot = i * j
    sum += dot
  return sum


# Question 8
def cross_product(a, b):
  """ Function takes two lists of numbers of length 3 and returns their cross product """
  c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
  return c


def test_suite():
  """ Run the suite of tests for code in this module (this file).
    """
  # Question 5
  test(add_vectors([1, 1], [1, 1]) == [2, 2])
  test(add_vectors([1, 2], [1, 4]) == [2, 6])
  test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
  # Question 6
  test(scalar_mult(5, [1, 2]) == [5, 10])
  test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
  test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
  # Question 7
  test(dot_product([1, 1], [1, 1]) ==  2)
  test(dot_product([1, 2], [1, 4]) ==  9)
  test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
  # Question 8
  test(cross_product([1, 2, 1], [1, 4, 3]) == [2, -2, 2])
  test(cross_product([1, 0, -1], [1, 4, 3]) == [4, -4, 4])
  test(cross_product([1, 2, 1], [3, 0, 5]) == [10, -2, -6])


test_suite()