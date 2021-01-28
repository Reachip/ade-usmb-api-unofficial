import requests


class ICalendar:
    @staticmethod
    def from_url(url):
        return requests.get(url).content.decode("utf-8")

    @staticmethod
    def from_file(path):
        with open(path, "r") as icalendar_handler:
            return icalendar_handler.readlines()
