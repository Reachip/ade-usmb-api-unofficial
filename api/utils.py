import os
from flask import jsonify
from .timetable_formatter import TimeTableFormatter
from .timetable import TimeTable
from .icalendar import ICalendar


def sort_by(parameter, value, formatted_timetable):
    return [event for event in formatted_timetable if event[parameter] == value]


def departement_names():
    for departement_name in os.listdir("./ics"):
        yield f"./ics/{departement_name}"


def init_formatters():
    formatter_per_departement = {}

    for departement_name in departement_names():
        if os.path.isdir(departement_name):
            for ics in os.listdir(departement_name):
                filename, extension = ics.split(".")

                if extension == "ics":
                    formatter = TimeTableFormatter(
                        TimeTable(
                            ICalendar.from_file(f"{departement_name}/{filename}.ics")
                        )
                    ).format()

                    try:
                        formatter_per_departement[
                            departement_name.split("/")[2]
                        ].append((filename, formatter))

                    except NameError:
                        formatter_per_departement[departement_name.split("/")[2]] = [
                            (filename, formatter)
                        ]

    return formatter_per_departement


def success(message):
    return jsonify(code=200, response=message)


def fail(message):
    return jsonify(code=404, response=message)
