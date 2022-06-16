import io
from bs4 import BeautifulSoup
from format_helper import to_str

def saveAsFile(html):
    f = io.open("analysis_target.html", "w")
    f.write(html)
    f.close()

def readFile():
    f = io.open("analysis_target.html", "r")
    html = f.read()
    f.close()
    return html

def analysis(html):
    soup = BeautifulSoup(html, 'html.parser')

    calender = soup.find("div", {'id':'calendar-scroller'})
    thead = calender.find("thead").tr
    dayInfos = thead.find_all("th")
    dayInfos.pop(0)

    for dayInfo in dayInfos:
        dayInfoTexts = dayInfo.text.replace(" ","").split("\n")
        print(type(dayInfoTexts[0]))
        print(to_str(dayInfoTexts[0]))
        #print(to_str(dayInfoTexts[0]))
        #print(dayInfoTexts[0].decode('EUC-KR'))
        #print(dayInfoTexts[0].decode('CP949'))
        #print(dayInfoTexts[0].decode('UTF-8'))
        #print(dayInfoTexts[0].decode('UTF-16'))
        #print(dayInfoTexts[0].decode('ASCII'))

        #dayNum = to_str(dayInfoTexts[1])
        #dayOfTheWeek = to_str(dayInfoTexts[3])
        #print(type(dayNum)) # < unicode in ubuntu
        #print(type(dayOfTheWeek)) # < unicode in ubuntu
        #print("{}{}".format(dayNum, dayOfTheWeek).encode('utf-8'))

def analysisInLocalFile():
    html = readFile()
    analysis(html)

