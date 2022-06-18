from bs4 import BeautifulSoup
from format_helper import to_str
from html_file_io import readFile

def analysis(html):
    soup = BeautifulSoup(html, 'html.parser')

    calender = soup.find("div", {'id':'calendar-scroller'})
    thead = calender.find("thead").tr
    dayInfos = thead.find_all("th")
    dayInfos.pop(0)

    for dayInfo in dayInfos:
        dayInfoTexts = dayInfo.text.replace(" ","").split("\n")
        print(to_str(dayInfoTexts[0]))

def analysisInLocalFile():
    html = readFile()
    analysis(html)
