from bs4 import BeautifulSoup

def saveAsFile(html):
    f = open("analysis_target.html", "w")
    f.write(html)
    f.close()

def readFile():
    f = open("analysis_target.html", "r")
    html = f.read()
    f.close()
    return html

def analysis(html):
    html = BeautifulSoup(html, 'html.parser').prettify()
    saveAsFile(html)
    number = html.find("span", {"class":"reserve-step-number"})
    print(number.string)

def analysisInLocalFile():
    html = readFile()
    analysis(html)