from flask import Flask, request
from api.utils import sort_by, success, fail, init_formatters


app = Flask(__name__)
formatters = init_formatters()


@app.route("/api/<department>/<td>")
def timetable(department, td):
    try:
        formatters_per_department = formatters[department]
        response = [
            formatter[1]
            for formatter in formatters_per_department
            if formatter[0] == td
        ][0]

    except KeyError:
        return fail("Bad departement provided")

    except IndexError:
        return fail("Bad TD group provided")

    for arg_name, arg_value in request.args.to_dict().items():
        response = sort_by(arg_name, arg_value, response)

    return success(response)


if __name__ == "__main__":
    app.run("0.0.0.0")
