import io

def saveAsFile(html):
    f = io.open("analysis_target.html", "w")
    f.write(html)
    f.close()

def readFile():
    f = io.open("analysis_target.html", "r")
    html = f.read()
    f.close()
    return html