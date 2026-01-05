from scanner.header_analysis import analyze_headers
from scanner.url_analysis import extract_urls, analyze_urls
from scanner.content_analysis import analyze_content

with open("sample.eml") as f:
    raw_email = f.read()

print("Header Analysis:", analyze_headers(raw_email))
urls = extract_urls(raw_email)
print("Suspicious URLs:", analyze_urls(urls))
print("ML Result:", analyze_content(raw_email))