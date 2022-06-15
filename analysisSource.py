import io
from bs4 import BeautifulSoup

def saveAsFile(html):
    f = io.open("analysis_target.html", "w", encoding="UTF-8-sig")
    f.write(html)
    f.close()

def readFile():
    f = io.open("analysis_target.html", "r", encoding="UTF-8-sig")
    html = f.read()
    f.close()
    return html

def analysis(html):
    html = BeautifulSoup(html, 'html.parser').prettify()
    saveAsFile(html)
    print(html.encode("UTF-8-sig"))

def analysisInLocalFile():
    html = readFile()
    analysis(html)