TextCommands
============

Sublime Text 2 (and 3!) Plugin including a variety of commands for manipulating/navigating text
--------------------------------------------------------------------------------------


![Demo](https://raw.github.com/chaosphere2112/TextCommands/screenshots/demo.gif)



There are things that humans excel at. Creativity, free thinking, visual processing.

Editing text is not one of those things.

In every document, there will crop up moments when some menial task threatens to throw you off your groove.
Sublime Text does an excellent job of making many of these things easier, with multiple selections and its many other
wonderful features. Still, menial tasks are what computers excel at. You shouldn't have to write out numbers in a sequence
from 1 to N. You shouldn't have to sort words or phrases.  You shouldn't have to keep track of how many selections you have,
you shouldn't have to convert things to hexadecimal by hand, and you shouldn't have to count how many characters are in a 
string.

That's where TextCommands comes in.

It's a collection of commands that are tested in the field.

I edit thousands of lines of XML by hand on a regular basis, and I do best to automate the things that I find menial and repetitive.
You can benefit from my automation.

So, enjoy a free pass to become more productive in your text editing. If you think of something to add, feel free to 
either do a pull request or file a bug report.


Text Conversion:
----------------

`Snake To CamelCase`: Converts "method\_names\_like_this" to "MethodNamesLikeThis"

`CamelCase to Snake`: Converts "MethodNamesLikeThis" to "method\_names\_like_this"

`Underscore To Spaces`: Converts "names\_like\_this" to "names like this"

`Space To Underscores`: Converts "names like this" to "names\_like\_this"


Text Manipulation:
------------------

`Remove Duplicate Lines`: Removes duplicate lines in each selection (duplicates only tracked inside each selection)

`Line Length`: Breaks a selection into multiple lines based on a maximum character length (breaks only on spaces) _(does not work in Sublime Text 3 beta 3021)_

`Sort Text`: Sorts your selections in place.

Given some text:

    joe went there from here

If you select `joe`, `went there`, `from`, and `here` each as its own selection and use the `Sort Text` command, you are left with this:

    from here joe went there

`Shift Selections Left`: Shifts all selections left one character.

`Shift Selections Right`: Shifts all selections right one character.

Text Navigation:
----------------

`Go To Character`: Jumps to a specified character number, moving it into view.

Numeric Commands:
-----------------

`Integer Sequence`: Converts all selected integers into a numeric sequence from 0 to N, where N is the number of integers.

`Decimal To Hex`: Converts all selected integers from decimal to hexadecimal.

`Hex To Decimal`: Converts all selected numbers from hexadecimal to decimal.

`Increment Selection`: Raises the value of all selected numbers by 1

`Decrement Selection`: Lowers the value of all selected numbers by 1


Text Info:
----------

`Character Value`: Presents an alert that contains the value of each character selected.

`Selection Length`: Presents a dialog informing you of the number of characters you have selected (added together for each selection)

`Number of Selections`: Presents a dialog informing you of the number of selections you have.


License:
--------

    Copyright © 2013 Samuel B. Fries

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
    and associated documentation files (the "Software"), to deal in the Software without restriction, 
    including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
    and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial 
    portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
    LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN 
    NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
