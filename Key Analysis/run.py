import string      # definitions of ascii printable chars
from collections import defaultdict     # fast counting
from nltk_runner import get_bnc_words

d = defaultdict(int)    # define dictionary for counting frequencies

# define text - see below for how to download from a url

bnc_output = get_bnc_words()

text = "".join(bnc_output)

########TEMP TO GET CORPUS AS TEXT ##########
with open('bnc_corpus_baby.txt', 'w', encoding='utf-8') as f:
  f.write(text)
#############################################

for ch in text:       # loop over each character 
  if ch in string.printable:     # is the character in the ascii/printable set?
    d[ch] += 1    #   if so, add 1 to that characters frequency counter


# Results sorted by value

fv = open("results_value_sorted.txt", "w")

v_sorted = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

for key in v_sorted:
  print(f'{key}: {d[key]}')
  fv.write(f'{key}: {d[key]}\n')
