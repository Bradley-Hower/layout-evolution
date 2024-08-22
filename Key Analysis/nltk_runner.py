from nltk.corpus.reader.bnc import BNCCorpusReader

# Initialize the BNCCorpusReader


# Get all words from the corpus
def get_bnc_words():
  bnc_reader = BNCCorpusReader(root='BNC_baby/Texts/', fileids=r'[A-K]/\w*/\w*\.xml')
  bnc_words = bnc_reader.words(fileids=None, strip_space=False, stem=False)
  return bnc_words
