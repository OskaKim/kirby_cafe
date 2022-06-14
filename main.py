from analysisSource import analysis, analysisInLocalFile
from webDriver import getReservationPageSource
    
def test_process():
    analysisInLocalFile()

def normal_process():
    html = getReservationPageSource()
    analysis(html)
    
if __name__ == "__main__":
    print("start")
    #normal_process()
    test_process()
    print("end")