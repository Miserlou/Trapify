#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import argparse
import xerox

trap_letters = { 
    "A":"∆",
    "B":"Ɓ",
    "C":"Ͼ",
    "D":"Ɖ",
    "E":"Є",
    "F":"₣",
    "G":"₲",
    "H":"ῌ",
    "I":"Ị",
    "J":"J",
    "K":"₭",
    "L":"Ɫ",
    "M":"M", 
    "N":"И",
    "O":"Ø",
    "P":"Ᵽ",
    "Q":"Q",
    "R":"Я",
    "S":"Ϩ",
    "T":"₮",
    "U":"Ṳ",
    "V":"Ṿ",
    "W":"Ш",
    "X":"X",
    "Y":"Ϋ",
    "Z":"Z", 
    ".":"",
    "-":"︻╦╤─",
    "!":"!!!",
    "?":"???", 
    "[":"︻╦╤─",
    "]":"─╤╦︻",
    "<":"︻╦╤─",
    ">":"─╤╦︻", 
    "(":"︻╦╤─",
    ")":"─╤╦︻", 
}

def trapify(args):

    words = ' '.join(args['query']).upper()
    to_print = u''

    for letter in words:
        if letter in trap_letters:
            to_print = to_print + trap_letters[letter]
        else:
            to_print = to_print + letter

    print(to_print)
    if args['copy']:
        xerox.copy(to_print)

def get_parser():
    parser = argparse.ArgumentParser(description='Command line trillification.')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
            help='the string to search to trapify')
    parser.add_argument('-c','--copy', help='copy result to the clipboard.', default=False, dest='copy', action='store_true')
    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if not args['query']:
        parser.print_help()
        return

    trapify(args)

if __name__ == '__main__':
    command_line_runner()
