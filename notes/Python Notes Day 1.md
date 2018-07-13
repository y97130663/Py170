# Notes

# Python

**Strings:** Refer: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

Strings are objects with state (content) and behaviors (which are acted upon by the methods; methods are functions that are attached to the objects)

Strings are immutable; you cannot modify a string.

- `"pass" + "word"` gives a `"password"` which is a new string
- “`Ha" * 4` gives `'HaHaHaHa'` since it is ‘Ha’ + ‘Ha’ + ‘Ha’ + ‘Ha’

`#` is for single line comments

`""" ... """` is for multi-line comments

    >>> "double".find('s')
     -1 
    >>> "double".find('u')
    2
    since the string similar to arrays are 
    indexed and the items are positional

**Manipulating strings:**

    >>> <object>.lower()
    returns a lowercase 
    or returns the samething as there maynot
    be lower cases for the same.

**Delimiters:**

`\t` gives a tab spacing

`\n` gives a new line

`\` is an escape sequence

single quotes can be inside the double quotes and vice-versa. however you can also use escape sequence to get single quotes inside single quotes printed.

**Numbers:** Refer: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Integers and strings are always immutable; for example a 2 + 2 is 4 and it will not change the number two; 2 always remains as 2.

*Math operations:*

addition `+` ;

subtraction `-` ;

multiplication `*` ;

floor division 5 `//` 3 gives 1 which is quotient; gives whole number portion of the number

modulo division 5 `%` 3 gives 2 which is the remainder

power `**`

normal division 5.0 `/` 3 gives 1.6666…7; any math operation with float in it will give you float.

**Type Conversions:**

`type(`3`)` returns `int`

`int("`1`")` returns 1 which is an integer

`float("`1.1`")` returns 1.1 which is a float

`str(`1.1`)` returns ‘1.1’

**Numbers:**

There are two main types of numbers that we’ll use in Python, int and float. For the most part, we won’t be calling methods on number types, and we will instead be using a variety of operators.

Note: If either of the numbers in a mathematical operation in Python is a float, then the other will be converted before carrying out the operation, and the result will always be a float.

    >>> 2 + 2 # Addition
    4
    >>> 10 - 4 # Subtraction
    6
    >>> 3 * 9 # Multiplication
    27
    >>> 5 / 3 # Division
    1.66666666666667
    >>> 5 // 3 # Floor division, always returns a number without a remainder
    1
    >>> 8 % 3 # Modulo division, returns the remainder
    2
    >>> 2 ** 3 # Exponent
    8

**Converting Strings and Numbers:**

Conversion is not uncommon since we need to convert from one type to another when writing a script and Python provides built-in functions for doing that with the built-in types. For strings and numbers, we can use the str, int, and float functions to convert from one type to another (within reason).

    >>> str(1.1)
    '1.1'
    >>> int("10")
    10
    >>> int(5.99999)
    5
    >>> float("5.6")
    5.6
    >>> float(5)
    5.0

You’ll run into issues trying to convert strings to other types if they aren’t present in the string

    >>> float("1.1 things")
    Traceback (most recent call last):
      File "", line 1, in 
    ValueError: could not convert string to float: '1.1 things'

**Booleans and None:**

- Refer: [https://docs.python.org/3/library/stdtypes.html#truth-value-testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

  TBD

Booleans (truthiness):

Booleans represent “truthiness” and Python has two boolean constants: `True` and `False`.

Notice that these both start with capital letters. Later we will learn about comparisons operations, and those will often return either `True` or `False`.

Truthiness examples:

    >>> type(True)
    
    <class 'bool'>
    
    >>> False
    
    False
    >>> type(False)
    <class 'bool'>
    
    >>> bool({})
    
    False
    
    >>>bool("Keith")
    
    True

## **Representing Nothingness with `None`**

Most programming languages have a type that represents the lack of a value, and Python is no different. The constant used to represent nothingness in Python is `None`. `None` is a “falsy”, and we’ll often use it to represent when a variable has no value yet.

An interesting thing to note about `None` is that if you type `None` into your REPL, there will be nothing printed to the screen. That’s because `None` actually evaluates into nothing.

    None

**Variables:**

We can assign a value to a variable by using a single `=` and we don’t need to (nor can we) specify the type of the variable.

    >>> my_str = "This is a simple string"

Now we can print the value of that string by using `my_var` later on:

    >>> print(my_str)
    This is a simple string

Before, we talked about how we can’t change a string because it’s immutable. This is easier to see now that we have variables.

    >>> my_str += " testing"
    >>> my_str
    'This is a simple string testing'

That didn’t change the string; it reassigned the variable. The original string of `"This is a simple string"` was unchanged.

An important thing to realize is that the contents of a variable can be changed and we don’t need to maintain the same type:

    >>> my_str = 1
    >>> print(my_str)
    1

Ideally, we wouldn’t change the contents of a variable called `my_str` to be an int, but it is something that python would let use do.

One last thing to remember is that if we assign a variable with another variable, it will be assigned to the result of the variable and not whatever that variable points to later.

    >>> my_str = 1
    >>> my_int = my_str
    >>> my_str = "testing"
    >>> print(my_int)
    1
    >>> print(my_str)
    testing

**Lists:**

In Python, there are a few different “sequence” types that we’re going to work with, the most common of which is the list type.

Sequence types:

- [https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

  TBD

- [https://docs.python.org/3/library/stdtypes.html#list](https://docs.python.org/3/library/stdtypes.html#list)

  TBD

A list is created in Python by using the square brackets (`[`, and `]`) and separating the values by commas. Here’s an example list:

    >>> my_list = [1, 2, 3, 4, 5]

There’s really not a limit to how long our list can be (there is, but it’s very unlikely that we’ll hit it while scripting).

To access an individual element of a list, you can use the index and Python uses a zero-based index system:

    >>> my_list[0]
    1
    >>> my_list[1]
    2

If we try to access an index that is too high (or too low) then we’ll receive an error:

    >>> my_list[5]
    Traceback (most recent call last):
      File "", line 1, in 
    IndexError: list index out of range

To make sure that we’re not trying to get an index that is out of range, we can test the length using the `len` function (and then subtract 1):

    >>> len(my_list)
    5

negative indexing is possible. my_list[-1] is the first from right and my_list[-6] is out of range where my_list = [1,2,3,4,5] 

Slice in list: Gets subsections 

Additionally, we can access subsections of a list by “slicing” it. We provide the starting index and the ending index (the object at that index won’t be included).

    # 2nd index is not considered; hence 0th and 1st indexes are printed
    >>> my_list[0:2]
    [1,2]
    # my_list[1:] is same as my_list[1:0] 
    # It prints everything but the first index
    >>> my_list[1:0]
    [2, 3, 4, 5]
    # my_list[:3] everything upto 3rd index 
    >>> my_list[:3]
    [1, 2, 3]
    # step of 1 from 0th index
    >>> my_list[0::1]
    [1, 2, 3, 4, 5]
    # step of 2 from 0th index
    >>> my_list[0::2]
    [1, 3, 5]

> Lists are mutable data types which means they can be changed.

Notes: square bracket is the called the subscript assignment operator.

- **Appending lists**: my_list.append(7)
- **Concatenating lists**: my_list + [8,9,10] appends the values 8,9,10 at the end. my_list += [8,9,10] is also same as concatenating the lists.

Items in lists can be set using slices also:

    >>> my_list[1:3] = ['b', 'c']
    >>> my_list
    ['a', 'b', 'c', 4, 5, 6, 7, 8, 9, 10]
    # Replacing 2 sized slice with length 3 list inserts new element
    my_list[3:5] = ['d', 'e', 'f']
    print(my_list)

***Observe:*** If we pass more parameters it will extend the list and will make it longer.

To removed certain items from the list we can replace the unwanted items with 'nothingness'. 

    >>> my_list
    ['a', 'b', 'c', 4, 5, 6, 7, 8, 9, 10]
    >>>my_list[4:] = []
    ['a','b','c',4]

Methods to remove items from the list: .remove(x) and .pop(x)

These methods change the items that they are called upon.

    >>> my_list.remove('b')
    # Does not return anything
    >>> print(my_list)
    ['a','c', 4, 5, 6, 7, 8, 9, 10]
    >>>my_list.pop(index_value_to_be_removed)
    #Returns the removed value; default value to be removed is last
    10
    IndexErrors: 
    - pop from empty list
    - pop index out of range
    - list.remove(x): x not in list

**Tuples:**

- Ref: [https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

  TBD

- Ref: [https://docs.python.org/3/library/stdtypes.html#tuple](https://docs.python.org/3/library/stdtypes.html#tuple)

  TBD

Immutable sequential data type; hence we do not have the methods as seen as in lists. However concatenate works since it returns a new tuple.

    >>> point = (2.0, 4.0)
    >>> points = point + (4.0,)
    >>> points
    (2.0, 4.0, 4.0)
    # Observe
    >>> point
    (2.0, 4.0, 4.0)
    >>> point = point + (4.0,5.0)
    >>> point
    (2.0, 4.0, 4.0, 4.0, 5.0)
    # To unpack a tuple
    >>> x, y, z, a, b = point
    >>> x
    2.0
    >>> a
    4.0

Pass values to string: A best use case for tuple

The time you’re most likely to see tuples will be when looking at a format string that’s compatible with Python 2:

    >>> print("Tuple are used here %s %s" % ("A","B"))
    Tuple are used here A B

> Keep reading code since it make you write python code much faster.

**Dictionaries:**

- Ref: [https://docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

  TBD

Dictionaries are the main mapping type that we’ll use in Python. This object is comparable to a Hash or “associative array” in other languages.

Things to note about dictionaries:

1. Unlike Python 2 dictionaries, as of Python 3.6, keys are ordered in dictionaries. You'll need `OrderedDict` if you want this to work on another version of Python.
2. You can set the key to any IMMUTABLE TYPE (no lists).
3. Avoid using things other than simple objects as keys.
4. Each key can only have one value (so don’t have duplicates when creating a dict).

>> Key values are commonly strings or any immutable types - ints, floats and strings.

>> Dictionaries created in python3 stay in the same order of creation unlike the ones create in the python2.

We create dictionary literals by using curly braces (`{` and `}`), separating keys from values using colons (`:`), and separating key/value pairs using commas (`,`). Here’s an example dictionary:

    >>> ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
    >>> ages
    {'kevin': 59, 'alex': 29, 'bob': 40}

We can read a value from a dictionary by subscripting using the key:

    >>> ages['kevin']
    59
    >>> ages['billy']
    Traceback (most recent call last):
      File "", line 1, in 
    KeyError: 'billy'

Keys can be added or changed using subscripting and assignment:

    >>> ages['kayla'] = 21
    >>> ages
    {'kevin': 59, 'alex': 29, 'bob': 40, 'kayla': 21}

Items can be removed from a dictionary using the `del` statement or by using the `pop` method:

    >>> del ages['kevin']
    >>> ages
    {'alex': 29, 'bob': 40, 'kayla': 21}
    >>> del ages
    >>> ages
    Traceback (most recent call last):
      File "", line 1, in 
    NameError: name 'ages' is not defined
    >>> ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
    >>> ages.pop('alex')
    29
    >>> ages
    {'kevin': 59, 'bob': 40}
    # Note pop function requires that argument 'key'
    # it needs to have the argument and does not take blanks

It’s not uncommon to want to know what keys or values we have without caring about the pairings. For that situation we have the `values` and `keys` methods:

    >>> ages = {'kevin': 59, 'bob': 40}
    >>> ages.keys()
    dict_keys(['kevin', 'bob'])
    >>> list(ages.keys())
    ['kevin', 'bob']
    >>> ages.values()
    dict_values([59, 40])
    >>> list(ages.values())
    [59, 40]

## **Alternative Ways to Create a `dict` Using Keyword Arguments**

There are a few other ways to create dictionaries that we might see, those being those that use the `dict`constructor with key/value arguments and a list of tuples:

    >>> weights = dict(kevin=160, bob=240, kayla=135)
    >>> weights
    {'kevin': 160, 'bob': 240, 'kayla': 135}
    >>> colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
    >>> colors
    {'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}

**Conditionals and Comparisons:**

- Ref: [https://docs.python.org/3/library/stdtypes.html#comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)

  TBD

- Ref: [https://docs.python.org/3/tutorial/controlflow.html#if-statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

  TBD

There are some standard comparison operators that we’ll use that match pretty closely to those used in mathematical equations. Let’s take a look at them:

    >>> 1 < 2
    True
    >>> 0 > 2
    False
    >>> 2 == 1
    False
    >>> 2 != 1
    True
    >>> 3.0 >= 3.0
    True
    >>> 3.1 <= 3.0
    False

If we try to make comparisons of types that don’t match up, we will run into errors:

    >>> 3.1 <= "this"
    Traceback (most recent call last):
      File "", line 1, in 
    TypeError: '<=' not supported between instances of 'float' and 'str'
    >>> 3 <= 3.1
    True
    >>> 1.1 == "1.1"
    False
    >>> 1.1 == float("1.1")
    True

We can compare more than just numbers. Here’s what it looks like when we compare strings:

    >>> "this" == "this"
    True
    >>> "this" == "This"
    False
    >>> "b" > "a"
    True
    >>> "abc" < "b"
    True

Notice that the string `'b'` is considered greater than the strings `'a'` and `'abc'`. The characters are compared one at a time alphabetically to determine which is greater. This concept is used to sort strings alphabetically.

## T**he `in` Check**

We often get lists of information that we need to ensure contains (or doesn’t contain) a specific item. To make this check in Python, we’ll use the `in` and `not in` operations.

    >>> 2 in [1, 2, 3]
    True
    >>> 4 in [1, 2, 3]
    False
    >>> 2 not in [1, 2, 3]
    False
    >>> 4 not in [1, 2, 3]
    True

`if/else` and `pass` statements:

    # pass can be used for the else block to do nothing as passon
    >>> if 1 == 1:
    ...     print("Alpha")
    ... else:
    ...     pass
    ... 
    Alpha
    >>> if 1 != 1:
    ...     print("Beta")
    ... else:
    ...     pass