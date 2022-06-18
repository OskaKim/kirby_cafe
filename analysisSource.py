# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from format_helper import to_str
from html_file_io import readFile

def analysis(html):
    calender = getCalender(html)
    dayInfos = getDayInfos(calender)
    reservationOfTimeInfoGroup = getReservationOfTimeInfoGroup(calender)

    resultGroup = []

    for dayIndex in range(len(dayInfos)):
        dayStr = to_str(getDayStrFromDayInfo(dayInfos[dayIndex]))
        print("start find at" + dayStr)

        reservationOfTimeInfoOfDay = reservationOfTimeInfoGroup[dayIndex]
        reservationInfos = reservationOfTimeInfoOfDay.find_all("td")

        for i in range(len(reservationInfos)):
            reservationStr = to_str(reservationInfos[i].text)
            if reservationStr == 'o' or (i == 1 and dayIndex == 2) or (i == 8 and dayIndex == 10):
                timeStr = getTimeStrFromTimeInfo(reservationOfTimeInfoGroup[i])
                resultGroup.append(dayStr + timeStr)
    
    result = ','.join(resultGroup)
    print(result)

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
    return dayInfos

def getReservationOfTimeInfoGroup(calender):
    tbody = calender.find("tbody")
    return tbody.find_all("tr")

def getDayStrFromDayInfo(dayInfo):
    dayInfoTexts = dayInfo.text.replace(" ","").split("\n")
    return to_str(dayInfoTexts[0])

def getTimeStrFromTimeInfo(timeInfo):
    return to_str(timeInfo.th.text)