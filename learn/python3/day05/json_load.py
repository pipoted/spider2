#!/usr/bin/env python3

import json

# json_str = '[{"username": "xiao", "age": 21, "country": "china"}, {"username": "xiaojian", "age": 21, "country": "china"}]'
# persons = json.loads(json_str)
# print(type(persons))
# for person in persons:
#     print(person)

with open('persons.json', 'r', encoding='utf-8') as fp:
    persons = json.load(fp)
    print(type(persons))
    for person in persons:
        print(person)
