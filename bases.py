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

import sublime
import sublime_plugin
import re
import os
from util import *


class PerRegionTextCommand(sublime_plugin.TextCommand):
    def pre(self):
        pass

    def post(self):
        pass

    def per_region(self, region_text):
        return region_text

    def run(self, edit):
        self.pre()
        view = self.view
        regions = view.sel()

        for region in regions:
            val = view.substr(region)
            view.replace(edit, region, self.per_region(val))

        self.post()


class PerLineTextCommand(PerRegionTextCommand):
    def pre(self):
        self.linebreak = os.linesep

    def per_line(self, line):
        return line

    def per_region(self, region):
        lines = region.split(self.linebreak)
        return self.linebreak.join(map(self.per_line, lines))


class PerWordTextCommand(PerRegionTextCommand):
    def pre(self):
        self.word_regex = re.compile("(\\s+)")

    def per_word(self, word):
        return word

    def per_region(self, region):
        word_result = ""

        words = self.word_regex.split(region)

        for word in words:

            if self.word_regex.match(word):
                word_result += word
                continue

            word_result += self.per_word(word)

        return word_result


class PerIntegerTextCommand(PerRegionTextCommand):
    def per_int(self, intval):
        pass

    def per_region(self, region):
        val = string_as_integer(region)

        if val is not None:
            return self.per_int(val)

        return region
