import os
from flask import jsonify
from .timetable_formatter import TimeTableFormatter
from .timetable import TimeTable
from .icalendar import ICalendar


class ICSFolderPathNotProvided(Exception):
    pass


def get_ics_folder_path():
    ics_folder = os.getenv("ADE_USMB_API_ICS_FOLDER")

    if ics_folder is None:
        raise ICSFolderPathNotProvided(
            "You need to provide an ADE_USMB_API_ICS_FOLDER environnement variable which contain the path to the ICS files"
        )

    return ics_folder


def sort_by(parameter, value, formatted_timetable):
    return [event for event in formatted_timetable if event[parameter] == value]


def departement_names():
    ics_folder_path = get_ics_folder_path()

    for departement_name in os.listdir(ics_folder_path):
        yield ics_folder_path + departement_name


def init_formatters():
    formatter_per_departement = {}

    for departement_name in departement_names():
        if os.path.isdir(departement_name):
            for ics in os.listdir(departement_name):
                filename, extension = ics.split(".")

                if extension == "ics":
                    path = f"{departement_name}/{filename}.ics"

                    formatter = TimeTableFormatter(
                        TimeTable(ICalendar.from_file(path))
                    ).format()

                    try:
                        formatter_per_departement[
                            departement_name.split("/")[-1:][0]
                        ].append((filename, formatter))

                    except KeyError:
                        formatter_per_departement[
                            departement_name.split("/")[-1:][0]
                        ] = [(filename, formatter)]

    return formatter_per_departement


def success(message):
    return jsonify(code=200, response=message)


def fail(message):
    return jsonify(code=404, response=message)
