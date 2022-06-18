# -*- coding: utf-8 -*-

from analysisSource import analysis, analysisInLocalFile
from html_file_io import saveAsFile
from webDriver import getReservationPageSource

def test_process():
    analysisInLocalFile()

def normal_process():
    html = getReservationPageSource()
    saveAsFile(html)
    analysis(html)
    
if __name__ == "__main__": 
    normal_process()
    #test_process()