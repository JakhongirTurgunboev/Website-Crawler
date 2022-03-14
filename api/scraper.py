import re
from urllib.request import urlopen

def scrape(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")

    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title)

    return title

