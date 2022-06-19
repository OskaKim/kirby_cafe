# -*- coding: utf-8 -*-

from analysisSource import get_available_schedule_for_reservation
from format_helper import to_str
from line_notify import line_notify
from webDriver import getReservationPageSources

if __name__ == "__main__":
    pageSources = getReservationPageSources()

    results = []
    for pageSource in pageSources:
        results.extend(get_available_schedule_for_reservation(pageSource))
        
    if results:
        result = to_str(','.join(results))
        line_notify(to_str(result + "...が空いてるぽよ！"))
    else:
        line_notify(to_str("今は空いてる時間がない見たいぽよ..."))