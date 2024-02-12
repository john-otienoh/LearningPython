#!/usr/bin/python3
import csv

name = input("Eneter you  name: ").upper()
code = list(csv.DictReader(open('nato_phonetic.csv')))
letter_code = {dict_key:dict_val for dict_key,dict_val in zip([l['letter'] for l in code], [c['code'] for c in code])}
print([letter_code[n] for n in [i for i in name]])