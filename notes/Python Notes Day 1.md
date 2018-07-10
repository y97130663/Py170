# Python

**Strings:**
Refer: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

Strings are objects with state (content) and behaviors (which are acted upon by the methods; methods are functions that are attached to the objects)

Strings are immutable; you cannot modify a string.

- `"pass" + "word"` gives a `"password"` which is a new string
- "`Ha" * 4` gives `'HaHaHaHa'` since it is 'Ha' + 'Ha' + 'Ha' + 'Ha'

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

single quotes can be inside the double quotes and vice-versa. however you can also use \ escape sequence to get single quotes inside single quotes printed.

**Numbers:**
Refer: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Integers and strings are always immutable; for example a 2 + 2 is 4 and it will not change the number two; 2 always remains as 2.

*Math operations:* 

addition `+` ; 

subtraction `-` ; 

multiplication `*` ; 

floor division 5 `//` 3 gives 1 which is quotient; gives whole number portion of the number

modulo division 5 `%` 3 gives 2 which is the remainder

power `**`

normal division 5.0 `/` 3 gives 1.6666...7; any math operation with float in it will give you float.

**Type Conversions:**

`type(`3`)` returns `int`

`int("`1`")` returns 1 which is an integer

`float("`1.1`")` returns 1.1 which is a float

`str(`1.1`)` returns '1.1' 

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

Refer: [https://docs.python.org/3/library/stdtypes.html#truth-value-testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

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
