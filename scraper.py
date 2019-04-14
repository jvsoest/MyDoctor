import urllib.request
from bs4 import BeautifulSoup

def scrapeZorgkaartResponse(webpage_url):
    page = urllib.request.urlopen(webpage_url)
    soup = BeautifulSoup(page, "html.parser")

    header = str(soup.find("head"))
    header = header.replace("href=\"https://www.zorgkaartnederland.nl", "href=\"")
    header = header.replace("href=\"", "href=\"https://www.zorgkaartnederland.nl")

    sliders = str(soup.find("div", attrs={"class": "sliders_holder"}))
    sliders = sliders.replace("<sup>", "<sup style='top: 0px;'>")

    scripts = soup.body.findAll("script")
    scriptString = ""
    for script in scripts:
        scriptString = scriptString + str(script)
    scriptString = scriptString.replace("src=\"/bundles", "src=\"https://www.zorgkaartnederland.nl/bundles")
    scriptString = scriptString.replace("src=\"/js", "src=\"https://www.zorgkaartnederland.nl/js")

    htmlPage = "<html>" + header + "<body><div id='body-content'><section class='content-section'><div class='container content_section_inner no_side_padding_mobile no_top_border_radius no_top_padding_mobile collapsable_elements_holder'><div class='content_holder'><div class='tab-content'><div class='content_section_row tab-pane active'><div class='tab_content_spacer'><div class='row'><div class='col-xs-12 col-sm-8'><div class='text_block hide-empty'>" + sliders + "</div></div></div></div></div></div></div></div></section></div>" + scriptString + "</body></html>"

    return htmlPage

scrapeZorgkaartResponse("https://www.zorgkaartnederland.nl/zorgverlener/dermatoloog-martens-h-302277")

def scrapeCrisUMArticlesHtml(webpage_url):
    page = urllib.request.urlopen(webpage_url)
    soup = BeautifulSoup(page, "html.parser")

    articlesListHtml = soup.findAll("div", attrs={"class": "rendering_researchoutput"})

    returnString = ""
    for article in articlesListHtml:
        returnString = returnString + str(article) + "<br/>"
    return returnString

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