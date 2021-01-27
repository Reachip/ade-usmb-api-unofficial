from flask import Flask, request
from api.utils import sort_by, success, fail, formatters


app = Flask(__name__)


@app.route('/api/<department>/<td>')
def timetable(department, td):
    try:
        formatters_per_department = formatters[department]
        response = [formatter[1] for formatter in formatters_per_department if formatter[0] == td][0] 


    except KeyError:
        return fail("Bad departement provided")

    except IndexError:
        return fail("Bad TD group provided")

    subject_param = request.args.get("subject")
    begin_param = request.args.get("begin")
    end_param = request.args.get("end")
    room_param = request.args.get("room")

    if subject_param is not None:
        response = sort_by("subject", subject_param, response)

    if begin_param is not None:
        response = sort_by("begin", begin_param, response)

    if end_param is not None:
        response = sort_by("end", end_param, response)

    if room_param is not None:
        response = sort_by("room", room_param, response)
    
    return success(response)


if __name__ == "__main__":
    app.run("0.0.0.0")
    

    

