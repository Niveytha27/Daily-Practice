# Imports
import random


# Core Logic
def deduper(raw_string):
    deduped_string = ''
    # Dedupe the string such that any number of occurrences of a letter is reduced to only one occurrence in the output.
    for i in range(len(raw_string)):
        if raw_string[i] != raw_string[(i+1) % len(raw_string)] and \
                raw_string[i] not in deduped_string:
            deduped_string += raw_string[i]
    return deduped_string


# Driver
base_string = 'abcdefabcdef'
for i in range(25):
    raw_string = ''
    for char in base_string:
        num = random.randint(1, 5)
        raw_string += char * num
    output = deduper(raw_string)


# Validation
    if output != base_string:
        print(f'Trial {i+1:2d} failed. Deduped string was : {output}')
