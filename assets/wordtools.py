import sys, string

def cleanword(word):
  """ Remove punctuation marks from a word """
  s_without_punct = ""
  for letter in word:
      if letter not in string.punctuation:
          s_without_punct += letter
  return s_without_punct


def has_dashdash(word):
  """ Determine if a word has double dashes """
  if word.find("--") < 0:
    return False
  else:
    return True


def extract_words(string):
  """ Extract words from a string and represent them in a list """
  if has_dashdash(string):
    new_string = string.replace("--", " ")
  else:
    new_string = string
  return cleanword(new_string.lower()).split()


def wordcount(word, string):
  """ Count the number of times 'word' occurs in a 'string' """
  count = 0
  for i in range(len(string)):
    if word == string[i]:
      count+=1
  return count


def wordset(list_of_words):
  """ Return a new list that contains unique values from 'list_of_words' """
  new_list = []
  for word in list_of_words:
    if word not in new_list:
      new_list.append(word)
  return new_list


def longestword(list_of_words, fallback=0):
  """ Return the length of the longest word in 'list_of_words' """
  return len(max(list_of_words, key = len)) if list_of_words else fallback
  

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")


test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))


test(extract_words("Now is the time!  'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])



test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)
    

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ['now', 'is', 'time'])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ['I', 'a', 'is', 'am'])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ['or', 'a', 'am', 'is', 'are', 'be', 'but'])


test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
