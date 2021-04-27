# Imports
import random

# Core Logic
def deduper(raw_string):
    deduped_string = ''
    # Dedupe the string such that any number of occurrences of a letter is reduced to only one occurrence in the output.
    string_list = list(raw_string)
    conv_list = []
    for idx, char in enumerate(string_list):
        next_char = string_list[(idx + 1) % len(string_list)]
        if char == next_char and char not in conv_list:
            conv_list.append(char)
        elif char not in conv_list:
            conv_list.append(char)
    deduped_string = ("".join(str(elem) for elem in sorted(conv_list)))
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
