#!/usr/bin/python3
"""Module 9-add_item.
Adds all arguments to a Python list,
and then save them to a file
"""

import sys
import json

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

my_file = 'add_item.json'

my_list = []

if load_from_json_file(my_file):
    my_list = load_from_json_file(my_file)

for elem in sys.argv[1:]:
    my_list.append(elem)

save_to_json_file(my_list, my_file)
