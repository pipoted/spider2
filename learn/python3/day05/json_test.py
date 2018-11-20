# coding=utf-8

import json

persons = [
    {
        'username': '肖',
        'age': 21,
        'country': 'china',
    },
    {
        'username': 'xiaojian',
        'age': 21,
        'country': 'china',
    }
]

# json_str = json.dumps(persons)
# with open('persons.json', 'w', encoding='utf-8') as fp:
#     # fp.write(json_str)
#     json.dump(persons, fp, ensure_ascii=False)


class Person(object):
    country = 'china'


a = {
    'person': Person(),
}
