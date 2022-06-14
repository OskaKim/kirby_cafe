from analysisSource import analysis, analysisInLocalFile
from webDriver import getReservationPageSource
    
def test_process():
    analysisInLocalFile()

def normal_process():
    html = getReservationPageSource()
    analysis(html)
    
if __name__ == "__main__":
    #normal_process()
    test_process()