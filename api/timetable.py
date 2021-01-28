import re

class TimeTable:
    def __init__(self, icalendar_handler):
        self.icalendar_handler = icalendar_handler
        self.useless_data = (" ", "CREATED", "LAST-MODIFIED", "UID", "END", "SEQUENCE", "DTSTAMP")

    def get_events(self):
        event_cursor = {}
        events = []

        for icalendar_line in self.icalendar_handler:
            raw_line = re.sub('\n|,', '', icalendar_line)
    
            if raw_line == "END:VEVENT":
                events.append(event_cursor)

            elif raw_line == "BEGIN:VEVENT":
                event_cursor = {}

            else:
                try:
                    data, value = raw_line.split(":")

                    if not data in self.useless_data:
                        event_cursor[data] = value

                except ValueError: pass

        return events