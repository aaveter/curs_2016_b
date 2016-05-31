



from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/admin")
def admin():
    return "Some adminka!"


@app.route("/product/<id>")
def product(id):
    return "product # {}".format(id)


if __name__ == "__main__":
    app.run()