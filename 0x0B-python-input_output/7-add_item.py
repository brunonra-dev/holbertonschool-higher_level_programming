#!/usr/bin/python3
"""
load_add_save module
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.exists('add_item.json'):
    objs = load_from_json_file('add_item.json')
else:
    objs = []

for n in range(1, len(sys.argv)):
    objs.append(sys.argv[n])

save_to_json_file(objs, 'add_item.json')
