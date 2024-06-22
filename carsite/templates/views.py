from flask import Blueprint
from flask import render_template
from flask import request

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@bp.route("/contactus", methods=["POST"])
def contactus():
    print(
        "name: {}\nemail: {}\nsubject: {}\nmessage: {}".format(
            request.args.get("name"),
            request.args.get("email"),
            request.args.get("subject"),
            request.args.get("message"),
        )
    )

    return render_template("contactus.html")
