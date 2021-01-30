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

            except KeyError:
                pass

            dtstart = parse(event.pop("DTSTART"))
            dtend = parse(event.pop("DTEND"))
            
            event["date"] =  str(dtstart.date())
            event["day"] =  dtstart.strftime("%A").lower()
            event["begin"] = f"{dtstart.hour+1:02}:{dtstart.minute:02}"
            event["room"] = event.pop("LOCATION")
            event["subject"] = event.pop("SUMMARY")
            event["week"] = str(dtstart.isocalendar()[1])
            event["end"] = f"{dtend.hour+1:02}:{dtend.minute:02}"

        return formatted_timetable

    def __str__(self):
        return str(self.format())
