#!/usr/bin/python3
""" Module """
import sys
import json
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_file = 'add_item.json'

my_list = []

if os.path.exists(my_file):
    my_list = load_from_json_file(my_file)
  
my_list.extend(sys.argv[1:])

save_to_json_file(my_list, my_file)