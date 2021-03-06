from dateutil.parser import parse

class TimeTableFormatter:
    def __init__(self, timetable):
        self.timetable = timetable
    
    def format(self):
        formatted_timetable = self.timetable.get_events()

        for event in formatted_timetable:
            try:
                event["teacher"] = event.pop("DESCRIPTION")
                event["teacher"] = event["teacher"].replace("\\n", " ")
            
            except KeyError: pass

            event["begin"] = str(parse(event.pop("DTSTART")))
            event["room"] = event.pop("LOCATION")
            event["subject"] = event.pop("SUMMARY")
            event["end"] = str(parse(event.pop("DTEND")))

        return formatted_timetable

    def __str__(self):
        return str(self.format())