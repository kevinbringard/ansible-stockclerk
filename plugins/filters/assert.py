#  Copyright (c) 2017 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.


def is_bool(var):
    return (is_true(var) or is_false(var))


def is_true(var):
    return var in ['yes', 'on', '1', 'true', 1, 'True', True]


def is_false(var):
    return var in ['no', 'off', '0', 'false', 0, 'False', False]


def is_dict(var):
    if isinstance(var, dict):
        return True
    else:
        return False


def is_list(var):
    if isinstance(var, list):
        return True
    else:
        return False


def is_set(var):
    if isinstance(var, set):
        return True
    else:
        return False


def is_number(var):
    if isinstance(var, (int, long, float, complex)):
        return True
    else:
        return False


def is_string(var):
    if isinstance(var, basestring):
        return True
    else:
        return False


def is_ipaddr(var):
    ip = var.split('.')
    if len(ip) != 4:
        return False
    for octet in ip:
        if not octet.isdigit():
            return False
        digit = int(octet)
        if digit < 0 or digit > 255:
            return False
    return True


class FilterModule(object):
    def filters(self):
        return {
            'is_bool': is_bool,
            'is_dict': is_dict,
            'is_list': is_list,
            'is_set': is_set,
            'is_number': is_number,
            'is_string': is_string,
            'is_ipaddr': is_ipaddr,
        }
