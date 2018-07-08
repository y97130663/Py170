# Python

**Strings:**

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
