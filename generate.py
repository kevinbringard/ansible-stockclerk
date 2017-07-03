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

import contextlib

import yaml


class SafeDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(SafeDumper, self).increase_indent(flow, False)


def safe_load(string):
    return yaml.safe_load(string) or {}


def safe_load_file(filename):
    with open_file(filename) as stream:
        return safe_load(stream)


def safe_dump(data):
    return yaml.dump(
        data, Dumper=SafeDumper, default_flow_style=False, explicit_start=True)


def write_file(filename, content):
    with open_file(filename, 'w') as f:
        f.write(content)


@contextlib.contextmanager
def open_file(filename, mode='r'):
    with open(filename, mode) as stream:
        yield stream


def get_assert(var, var_data):
    if var_data['type'] == 'bool':
        return _bool_assert(var)
    if var_data['type'] == 'map':
        return _dict_assert(var)
    if var_data['type'] == 'seq':
        return _list_assert(var)
    if var_data['type'] == 'str':
        return _string_assert(var)
    if var_data['type'] in ['int', 'float']:
        return _number_assert(var)


def _defined_assert(var):
    is_defined = '{} is defined'.format(var)

    return {'assert': {'that': is_defined}}


def _bool_assert(var):
    is_bool = '{} | is_bool'.format(var)
    msg = '"{}" must be of type bool'.format(var)

    return {
        'assert': {
            'that': is_bool,
            'msg': msg,
        },
        'tags': ['assert'],
    }


def _dict_assert(var):
    is_dict = '{} | is_dict'.format(var)
    msg = '"{}" must be of type dict'.format(var)

    return {
        'assert': {
            'that': is_dict,
            'msg': msg,
        },
        'tags': ['assert'],
    }


def _list_assert(var):
    is_list = '{} | is_list'.format(var)
    msg = '"{}" must be of type list'.format(var)

    return {
        'assert': {
            'that': is_list,
            'msg': msg,
        },
        'tags': ['assert'],
    }


def _string_assert(var):
    is_string = '{} | is_string'.format(var)
    msg = '"{}" must be of type string'.format(var)

    return {
        'assert': {
            'that': is_string,
            'msg': msg,
        },
        'tags': ['assert'],
    }


def _number_assert(var):
    is_number = '{} | is_number'.format(var)
    msg = '"{}" must be of type int'.format(var)

    return {
        'assert': {
            'that': is_number,
            'msg': msg,
        },
        'tags': ['assert']
    }


model_dict = safe_load_file('model/model.yml')
data = [
    get_assert(var, var_data)
    for var, var_data in model_dict['groupvars']['all'].items()
]
write_file('playbooks/assert_generated.yml', safe_dump(data))
