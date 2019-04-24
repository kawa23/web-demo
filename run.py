# @Time      : 2019.04.18
# @Author    : kawa Yeung
# @Licence   : MIT
# @function  : database utils


from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
