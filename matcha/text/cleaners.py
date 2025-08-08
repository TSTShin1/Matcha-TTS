"""
Cleaners are transformations that run over the input text at both training and eval time.

You should use:
  - "vietnamese_cleaners" if your input text is Vietnamese.
"""

import re

# Regular expression matching whitespace:
_whitespace_re = re.compile(r"\s+")

# Remove brackets
_brackets_re = re.compile(r"[\[\]\(\)\{\}]")

# List of (regex, replacement) for Vietnamese abbreviations
_vietnamese_abbreviations = [
    (re.compile(r"\bTP\.", re.IGNORECASE), "thành phố"),
    (re.compile(r"\bĐH\b", re.IGNORECASE), "đại học"),
    (re.compile(r"\bTS\.", re.IGNORECASE), "tiến sĩ"),
    (re.compile(r"\bBS\.", re.IGNORECASE), "bác sĩ"),
    (re.compile(r"\bVNĐ\b", re.IGNORECASE), "Việt Nam đồng"),
    (re.compile(r"\bBTC\b", re.IGNORECASE), "ban tổ chức"),
    (re.compile(r"\bCLB\b", re.IGNORECASE), "câu lạc bộ"),
    (re.compile(r"\bNXB\b", re.IGNORECASE), "nhà xuất bản"),
    (re.compile(r"\bTW\b", re.IGNORECASE), "trung ương"),
    (re.compile(r"\bTHCS\b", re.IGNORECASE), "trung học cơ sở"),
    (re.compile(r"\bTHPT\b", re.IGNORECASE), "trung học phổ thông"),
    (re.compile(r"\bđc\b", re.IGNORECASE), "được"), 
    (re.compile(r"\bTV\b", re.IGNORECASE), "ti vi"),
    (re.compile(r"\bkm\b", re.IGNORECASE), "ki lô mét"),
    (re.compile(r"\bkg\b", re.IGNORECASE), "ki lô gam"),
]

def lowercase(text):
    return text.lower()

def remove_brackets(text):
    return re.sub(_brackets_re, "", text)

def collapse_whitespace(text):
    return re.sub(_whitespace_re, " ", text)

def expand_vietnamese_abbreviations(text):
    for regex, replacement in _vietnamese_abbreviations:
        text = re.sub(regex, replacement, text)
    return text

def vietnamese_cleaners(text):
    """Cleaners for Vietnamese text with abbreviation expansion."""
    text = lowercase(text)
    text = expand_vietnamese_abbreviations(text)
    text = remove_brackets(text)
    text = collapse_whitespace(text)
    return text
