import re


class TimeTable:
    def __init__(self, icalendar_handler):
        self.icalendar_handler = icalendar_handler
        self.useless_data = (
            " ",
            "CREATED",
            "LAST-MODIFIED",
            "UID",
            "END",
            "SEQUENCE",
            "DTSTAMP",
        )
        self.events = []

    def _format_line(self, line):
        return re.sub("\n|,", "", line)

    def get_events(self):
        if not self.events:
            event_cursor = {}

            for icalendar_line in self.icalendar_handler:
                raw_line = self._format_line(icalendar_line)

                if raw_line == "END:VEVENT":
                    self.events.append(event_cursor)

                elif raw_line == "BEGIN:VEVENT":
                    event_cursor = {}

                else:
                    try:
                        data, value = raw_line.split(":")

                        if not data in self.useless_data:
                            event_cursor[data] = value

                    except ValueError:
                        pass

        return self.events
