from bs4 import BeautifulSoup

ALLOWED_TAGS = ['p', 'br']

def sanitize_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(True):
        if tag.name not in ALLOWED_TAGS:
            return False

    return True

def compute_page_count(number_of_articles, limit):
    if (number_of_articles % limit) == 0:
        return number_of_articles // limit
    return (number_of_articles // limit) + 1
