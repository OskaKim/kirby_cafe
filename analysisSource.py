# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from format_helper import to_str

def get_available_schedule_for_reservation(html):
    calender = getCalender(html)
    monthStr = getMonthStr(html)
    dayInfos = getDayInfos(calender)
    reservationOfTimeInfoGroup = getReservationOfTimeInfoGroup(calender)

    resultGroup = []

    print(monthStr)

    for dayIndex in range(len(dayInfos)):
        dayStr = to_str(getDayStrFromDayInfo(dayInfos[dayIndex]))
        print("start find at" + dayStr)

        reservationOfTimeInfoOfDay = reservationOfTimeInfoGroup[dayIndex]
        reservationInfos = reservationOfTimeInfoOfDay.find_all("td")

        for i in range(len(reservationInfos)):
            reservationStr = to_str(reservationInfos[i].text)
            if reservationStr == 'o':
                timeStr = getTimeStrFromTimeInfo(reservationOfTimeInfoGroup[i])
                result = monthStr + dayStr + timeStr
                resultGroup.append(result)
                print(result)
    
    return resultGroup

def getCalender(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find("div", {'id':'calendar-scroller'})

def getMonthStr(html):
    soup = BeautifulSoup(html, 'html.parser')
    return to_str(soup.find("span", {'class':'body-1'}).text)

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