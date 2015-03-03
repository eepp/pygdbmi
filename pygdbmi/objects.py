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

import enum


class ResultRecord:
    pass


class DoneResultRecord(ResultRecord):
    pass


class ConnectedResultRecord(ResultRecord):
    pass


class ErrorResultRecord(ResultRecord):
    def __init__(self, msg, code):
        self._msg = msg
        self._code = code

    @property
    def msg(self):
        return self._msg

    @property
    def code(self):
        return self._code


class ExitResultRecord(ResultRecord):
    pass


class StreamRecord:
    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        return self._text


class ConsoleOutput(StreamRecord):
    def __init__(self, text):
        super().__init__(text)


class TargetOutput(StreamRecord):
    def __init__(self, text):
        super().__init__(text)


class LogOutput(StreamRecord):
    def __init__(self, text):
        super().__init__(text)


class AsyncRecord:
    pass


class ExecAsyncOutput(AsyncRecord):
    pass


class StatusAsyncOutput(AsyncRecord):
    pass


class NotifyAsyncOutput(AsyncRecord):
    pass


class RunningAsyncOutput(ExecAsyncOutput):
    def __init__(self, thread_id):
        self._thread_id = thread_id

    @property
    def thread_id(self):
        return self._thread_id


@enum.unique
class StopReason(enum.Enum):
    BREAKPOINT_HIT = 0
    WATCHPOINT_TRIGGER = 1
    READ_WATCHPOINT_TRIGGER = 2
    ACCESS_WATCHPOINT_TRIGGER = 3
    FUNCTION_FINISHED = 4
    LOCATION_REACHED = 5
    WATCHPOINT_SCOPE = 6
    END_STEPPING_RANGE = 7
    EXITED_SIGNALLED = 8
    EXITED = 9
    EXITED_NORMALLY = 10
    SIGNAL_RECEIVED = 11
    SOLIB_EVENT = 12
    FORK = 13
    VFORK = 14
    SYSCALL_ENTRY = 15
    SYSCALL_RETURN = 16
    EXEC = 17


class StoppedAsyncOutput(ExecAsyncOutput):
    def __init__(self, reason, thread_id, stopped_thread_ids, core):
        self._reason = reason
        self._thread_id = thread_id
        self._stopped_thread_ids = stopped_thread_ids
        self._core = core

    @property
    def reason(self):
        return self._reason

    @property
    def thread_id(self):
        return self._thread_id

    @property
    def stopped_thread_ids(self):
        return self._stopped_thread_ids

    def all_threads_stopped(self):
        return self._stopped_thread_ids == 'all'

    @property
    def core(self):
        return self._core


class ThreadGroupAddedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_group_id):
        self._thread_group_id = thread_group_id

    @property
    def thread_group_id(self):
        return self._thread_group_id


class ThreadGroupRemovedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_group_id):
        self._thread_group_id = thread_group_id

    @property
    def thread_group_id(self):
        return self._thread_group_id


class ThreadGroupStartedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_group_id, pid):
        self._thread_group_id = thread_group_id
        self._pid = pid

    @property
    def thread_group_id(self):
        return self._thread_group_id

    @property
    def pid(self):
        return self._pid


class ThreadGroupExitedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_group_id, exit_code):
        self._thread_group_id = thread_group_id
        self._exit_code = exit_code

    @property
    def thread_group_id(self):
        return self._thread_group_id

    @property
    def exit_code(self):
        return self._exit_code


class ThreadCreatedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_id, thread_group_id):
        self._thread_id = thread_id
        self._thread_group_id = thread_group_id

    @property
    def thread_id(self):
        return self._thread_id

    @property
    def thread_group_id(self):
        return self._thread_group_id


class ThreadExitedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_id, thread_group_id):
        self._thread_id = thread_id
        self._thread_group_id = thread_group_id

    @property
    def thread_id(self):
        return self._thread_id

    @property
    def thread_group_id(self):
        return self._thread_group_id


class ThreadSelectedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_id):
        self._thread_id = thread_id

    @property
    def thread_id(self):
        return self._thread_id


class RecordStartedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_group_id):
        self._thread_group_id = thread_group_id

    @property
    def thread_group_id(self):
        return self._thread_group_id


class RecordStoppedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, thread_group_id):
        self._thread_group_id = thread_group_id

    @property
    def thread_group_id(self):
        return self._thread_group_id


class CmdParamChangedAsyncOutput(NotifyAsyncOutput):
    def __init__(self, params, value):
        self._params = params
        self._value = value

    @property
    def params(self):
        return self._params

    @property
    def value(self):
        return self._value

