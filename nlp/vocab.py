"""Generate the vocabulary

"""


import nltk


def make(text):
    """Make a new vocabulary based on text
    Args
    ----
    text: string
        cleaned raw text

    Returns
    -------
    vocab: dict
        vocabulary
        {word:{
            definition: string,  # crawl from merriam webster
            synonyms: list of other words  # crawl from merriam webster
            antonyms: list of other words  # crawl from merriam webster
            examples: list of strings}}

    Raises
    ------

    Note
    ----

    Examples
    --------
    """
    stemmer = nltk.PorterStemmer()
    sents = nltk.sent_tokenize(text)
    vocab = {}
    for idx, sent in enumerate(sents):
        tokens = [stemmer.stem(t) for t in nltk.word_tokenize(sent)]
        for token in tokens:
            vocab.setdefault(token, []).append(idx)
    return sents, vocab
