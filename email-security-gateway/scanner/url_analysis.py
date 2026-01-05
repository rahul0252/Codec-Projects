import re

def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)

def analyze_urls(urls):
    return [u for u in urls if '@' in u or u.count('.') > 4]