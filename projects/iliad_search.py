#!usr/bin/env python 3

with open('iliad.txt') as iliad:
    term_count = 0
    mult_term_line = 0
    search_term = 'horse'
    for line in iliad:
        # line = line.lower()
        if 'horse' in line:
            term_count += line.count('horse') 
            if line.count('horse') > 1:
                print(line)
                mult_term_line += 1

    print(term_count) 
    print(mult_term_line) 