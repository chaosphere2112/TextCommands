"""
Copyright (c) 2013 Samuel B. Fries

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from util import *
import bases

"""
    Plugins that deal with numeric data
"""

"""
    Converts a group of selected integers into a sequence (from 0 to N, where N is the number of selections)
"""


class IntegerSequenceCommand(bases.PerIntegerTextCommand):
    def pre(self):
        self.ind = 0

    def per_int(self, intval):
        self.ind += 1
        return str(self.ind-1)

"""
    Converts selected hex numbers into decimal equivalents
"""


class HexToDecimalCommand(bases.PerWordTextCommand):
    def per_word(self, text):
        try:
            int_val = int(text, base=16)
            return str(int_val)
        except ValueError:
            return text


"""
    Converts selected decimal numbers into hexadecimal equivalents
"""


class DecimalToHexCommand(bases.PerIntegerTextCommand):
    def per_int(self, num):
        return num_to_hex(num)

"""
    Increments the selected numbers
"""


class IncrementSelectionCommand(bases.PerIntegerTextCommand):
    def per_int(self, num):
        num += 1
        return str(num)

"""
    Decrements the selected numbers
"""


class DecrementSelectionCommand(bases.PerIntegerTextCommand):
    def per_int(self, num):
        num -= 1
        return str(num)
