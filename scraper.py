import urllib.request
from bs4 import BeautifulSoup

def scrapeWebPageMumc(webpage_url):
    page = urllib.request.urlopen(webpage_url)
    soup = BeautifulSoup(page, "html.parser")

    imageUrl = soup.find("div", attrs={"class": "image"}).contents[1]["src"]
    caption = soup.find("header", attrs={"class": "articleHead"})

    caption_title = caption.contents[1].contents[0]
    caption_function = caption.contents[3].contents[0]

    article_content = soup.find("div", attrs={"class": "articleContent"})

    output = {
        "image_url": imageUrl,
        "title": caption_title,
        "function": caption_function,
        "content": article_content
    }

    return(output)