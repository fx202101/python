from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    print("init")
    return render_template('event.html')


@app.route('/login')
def login():
    # return 'Hello World'
    print("login")
    return render_template("event.html")


@app.route("/login_event", methods=["POST"])
def login_event():
    # return 'Hello World'
    print("login_event")
    return request.form["sid"] + request.form["comment"]


@app.route("/login_manager", methods=["POST"])  # 追加
def login_manager():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
