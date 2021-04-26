# Imports
import random

# Core Logic
def deduper(raw_string):
    deduped_string = ''
    # Dedupe the string such that any number of occurrences of a letter is reduced to only one occurrence in the output.
    return deduped_string

# Driver
base_string = 'abcdefghijklmnopqrstuvwxyz'
for i in range(25):
    raw_string = ''
    for char in base_string:
        num = random.randint(1, 5)
        raw_string += char * num
    output = deduper(raw_string)

# Validation
    if output != base_string:
        print(f'Trial {i+1:2d} failed. Deduped string was : {output}')