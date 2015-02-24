# The MIT License (MIT)
#
# Copyright (c) 2015 Philippe Proulx <eeppeliteloop@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

class ResultRecord:
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token


class DoneResultRecord(ResultRecord):
    def __init__(self, token, results):
        self._results = results
        super().__init__(token)

    @property
    def results(self):
        return self._results


class ConnectedResultRecord(ResultRecord):
    pass


class ErrorResultRecord(ResultRecord):
    def __init__(self, token, msg, code):
        self._msg = msg
        self._code = code
        super().__init__(token)

    @property
    def msg(self):
        return self._msg

    @property
    def code(self):
        return self._code


class ExitResultRecord(ResultRecord):
    pass
