import os
import re

initial_string = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

# Simple count how much whitespaces in the text using isspace() method
def count_whitespaces(string):
    amount = 0
    for symbol in string:
        if symbol.isspace():
            amount += 1
    print(f'Provided text include {amount} whitespaces')


# Replacing iz with is. Added spaces before/after iz to not replace unnecessary elements.
def replace_iz_with_is(string):
    return string.replace(' iz ', ' is ')

# Extracting words with regex, inserting them into string with spaces between words
def create_last_sentence_on_last_words(string):
    last_sentence = ''
    matches = re.findall(r" [a-zA-Z\d]*\.", string)
    for word in matches:
        last_sentence = last_sentence + word[:-1]
    return last_sentence[1:] + '.'

def append_sentence_to_paragraph_end(text, sentence, par_number):
    par_number -= 1
    text_split = text.splitlines()
    text_split[par_number] += " " + sentence
    return '\n'.join(text_split)

# Normalizing case. First all text to lower, than first letters in sentences to upper.
def normalize_string_case(string):
    string = string.lower()
    # My favorite part, took a lot of googling
    string = re.sub(r"((^[a-z])|\. ([a-z])|\t([a-z]))", lambda reg_match: reg_match.group(1).upper(), string)
    return string


def remove_empty_lines(string):
    return os.linesep.join([s for s in string.splitlines() if s])


# Processing initial text through all necessary actions. Tried to give as meaningful names of methods as possible.
# Initial text was saved into preliminary_string on which was actions was done.
count_whitespaces(initial_string)
preliminary_string = remove_empty_lines(initial_string)
sentence_to_add = create_last_sentence_on_last_words(preliminary_string)
preliminary_string = append_sentence_to_paragraph_end(preliminary_string, sentence_to_add, 3) # 3 - number of paragraph
preliminary_string = normalize_string_case(preliminary_string)
final_text = replace_iz_with_is(preliminary_string)
print(final_text)