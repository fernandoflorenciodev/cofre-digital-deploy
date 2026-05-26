import re

def mask_sensitive_data(text):

    patterns = [
        r'password=\w+',
        r'api[_-]?key=\w+',
        r'secret=\w+'
    ]

    for pattern in patterns:
        text = re.sub(pattern, '***MASKED***', text, flags=re.IGNORECASE)

    return text
