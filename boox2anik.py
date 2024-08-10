#!/usr/bin/env python3

input_file = "sample.txt"
output_file = "anki_import.txt"

# transform2anki transform the list of items into colon seperated lines
# it complies to the Dict2Anki-v6.16(Fixed for Anki23 by Shige) format
def transform2anki(items=[]):
    # item at index 0 is dropped, it is the word being looked up, it could have tense, could be in plural
    # item at index 1 is dropped, it is the dictionary name where the word was looked up
    # item at index 2 is the word from dictionay
    word = items[2]
    phonetic = items[3]

    # merge examples into definitions
    # my leaf3 is configured with multiple dicts and each returned definitions and examples in its own flavor...
    definition = ""
    for item in items[4:]:
        definition += item + ";"

    # seperator is \t because other characters were used by the dictionary
    return word + "\t" + phonetic + "\t" + definition

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    items = []
    for line in infile:
        # '---' is a separting line for a new word
        if '---' in line:
            anki_item = transform2anki(items)
            outfile.write(anki_item + "\n")
            items = []
            continue
            
        line = line.replace("\r", "").replace("\n", "").strip()
        
        if not line:
            continue

        items.append(line)
