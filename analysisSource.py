from bs4 import BeautifulSoup
from format_helper import to_str
from html_file_io import readFile

def analysis(html):
    calender = getCalender(html)
    getDayInfos(calender)
    getTimeInfos(calender)

def analysisInLocalFile():
    html = readFile()
    analysis(html)

def getCalender(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find("div", {'id':'calendar-scroller'})

def getDayInfos(calender):
    thead = calender.find("thead").tr
    dayInfos = thead.find_all("th")
    dayInfos.pop(0)

    for dayInfo in dayInfos:
        dayInfoTexts = dayInfo.text.replace(" ","").split("\n")
        print(to_str(dayInfoTexts[0]))

def getTimeInfos(calender):
    tbody = calender.find("tbody")
    timeInfos = tbody.find_all("tr")

    for timeInfo in timeInfos:
        print(to_str(timeInfo.th.text))