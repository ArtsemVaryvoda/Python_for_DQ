def main():
    count_whitespaces(initial_string)
    text_without_empty_lines = remove_empty_lines(initial_string)
    sentence_to_add = create_last_sentence_on_last_words(text_without_empty_lines)
    preliminary_string \
        = append_sentence_to_paragraph_end(text_without_empty_lines, sentence_to_add, 3)  # 3 - number of paragraph
    preliminary_string = normalize_string_case(preliminary_string)
    final_text = replace_iz_with_is(preliminary_string)
    print(final_text)

if __name__ == "__main__":
   main()

import os
import re

initial_string = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

def count_whitespaces(text):
    amount = 0
    for symbol in text:
        if symbol.isspace():
            amount += 1
    print(f'Provided text include {amount} whitespaces')


def replace_iz_with_is(text):
    return text.replace(' iz ', ' is ')

def create_last_sentence_on_last_words(text):
    last_sentence = ''
    matches = re.findall(r" [a-zA-Z\d]*\.", text)
    for word in matches:
        last_sentence = last_sentence + word[:-1]
    return last_sentence[1:] + '.'

def append_sentence_to_paragraph_end(text, sentence, par_number):
    par_number -= 1
    text_split = text.splitlines()
    text_split[par_number] += " " + sentence
    return '\n'.join(text_split)

def normalize_string_case(text):
    lowered_text = text.lower()
    # My favorite part, took a lot of googling
    normalized_text = re.sub(r"((^[a-z])|\. ([a-z])|\t([a-z]))"
                             , lambda reg_match: reg_match.group(1).upper(), lowered_text)
    return normalized_text


def remove_empty_lines(text):
    return os.linesep.join([s for s in text.splitlines() if s])



