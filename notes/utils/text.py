import re

def get_word_count(text):
    if not text:
        return 0
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def extract_tags(text):
    if not text:
        return []
    tags = re.findall(r'#(\w+)', text)
    return list(set(tags))
