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

import re
try:
    import TextCommands.bases
except ImportError:
    import bases

"""
    Converts every snake_cased_word to a CamelCasedWord
"""


class SnakeToCamelCase(bases.PerWordTextCommand):
    def per_word(self, word):
        split = word.split("_")

        if len(split) > 1:
            strings = [x.capitalize() for x in split]
            word = "".join(strings)

        return word

"""
    Converts every CamelCasedWord to a snake_cased_word
"""


class CamelCaseToSnake(bases.PerWordTextCommand):
    def pre(self):
        super(CamelCaseToSnake, self).pre()
        self.split_re = re.compile('([A-Z]+)')

    def per_word(self, word):

        def process_token(tkn):
            char_first = tkn[0]
            return '_' + tkn.lower() if char_first.isupper() else tkn

        matches = self.split_re.split(word)
        matches = matches[1:] if matches[0] == '' else matches
        matches = matches[0:-1] if matches[-1] == '' else matches
        converted = ""
        if len(matches) > 0:
            head = [matches[0].lower()]
            rest = [process_token(tkn) for tkn in matches[1:]]
            words = head + rest
            sentence = "".join(words)
            converted += sentence

        return converted

"""
    Replaces all "_" characters with " " characters.
"""


class UnderscoreToSpacesCommand(bases.PerRegionTextCommand):
    def per_region(self, val):
        val = " ".join(val.split("_"))
        return val

"""
    Replaces all " " characters with "_" characters.
"""


class SpacesToUnderscoresCommand(bases.PerRegionTextCommand):
    def per_region(self, val):
        val = "_".join(val.split(" "))
        return val
