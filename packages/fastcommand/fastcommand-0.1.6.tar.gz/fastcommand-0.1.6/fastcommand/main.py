#!/usr/bin/env python3

# Copyright (c) 2021-2024 Jason Morley
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import functools
import logging
import sys


COMMANDS = {}


class Command(object):

    def __init__(self, name, help, arguments, epilog, formatter_class, callback):
        self.name = name
        self.help = help
        self.arguments = arguments
        self.epilog = epilog
        self.formatter_class = formatter_class
        self.callback = callback

class Argument(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def command(name, help="", arguments=[], epilog=None, formatter_class=argparse.HelpFormatter):
    def wrapper(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            return fn(*args, **kwargs)
        COMMANDS[name] = Command(name, help, arguments, epilog, formatter_class, inner)
        return inner
    return wrapper


class CommandParser(object):

    def __init__(self, *args, **kwargs):
        self.parser = argparse.ArgumentParser(*args, **kwargs)
        subparsers = self.parser.add_subparsers(help="command")
        for name, command in COMMANDS.items():
            subparser = subparsers.add_parser(command.name,
                                              help=command.help,
                                              epilog=command.epilog,
                                              formatter_class=command.formatter_class)
            for argument in command.arguments:
                subparser.add_argument(*(argument.args), **(argument.kwargs))
            subparser.set_defaults(fn=command.callback)

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def use_logging(self, format):
        verbose = '--verbose' in sys.argv[1:] or '-v' in sys.argv[1:]
        logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO,
                            format="[%(levelname)s] %(message)s")
        self.parser.add_argument('--verbose', '-v',
                                 action='store_true',
                                 default=False,
                                 help="show verbose output")

    def run(self):
        options = self.parser.parse_args()
        if 'fn' not in options:
            logging.error("No command specified.")
            exit(1)
        options.fn(options)
