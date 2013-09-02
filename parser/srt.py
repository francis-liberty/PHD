"""Parse out text body from srt files.
according to http://en.wikipedia.org/wiki/SubRip

1.A numeric counter identifying each sequential subtitle
2.The time that the subtitle should appear on the screen, followed by " --> " and the time it should disappear
3.Subtitle text itself on one or more lines
4.A blank line containing no text indicating the end of this subtitle[10]
"""

import re


def parse(file_path):
    """
    Args
    ----
    file_path: string

    Returns
    -------
    sents: list
        list of strings.
        each string is a sentence.

    Note
    ----

    Examples
    --------
    """
    return parse_file(file_path)


def parse_file(file_path):
    string = ""
    with open(file_path, 'r') as f:
        string = f.read()

    return parse_string(string)


def parse_string(string):
    # each segment separate by a blank line
    segs = re.split('\n\n', string)
    texts = []
    for seg in segs:
        # ignore # and time
        lines = seg.split('\n')
        text = ' '.join(lines[2:])
        # strip <> markups
        text = re.sub(r'<[^>]*>', '', text)
        texts.append(text)

    texts = '\n'.join(texts)
    return texts

#    sents = texts.split('.\n')
#
#    return sents
