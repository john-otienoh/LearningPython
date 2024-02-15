#!/usr/bin/python3
import csv

name = input("Eneter you  name: ").upper()
code = list(csv.DictReader(open('nato_phonetic.csv')))
letter_code = {dict_key:dict_val for dict_key,dict_val in zip([l['letter'] for l in code], [c['code'] for c in code])}
try:
    print([letter_code[n] for n in [i for i in name]])
except KeyError:
    print('Only letters in the alaphabet.')
    name = input("Eneter you  name: ").upper()
else:
    print([letter_code[n] for n in [i for i in name]])