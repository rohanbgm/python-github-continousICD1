from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hey,Mate"

if __name__=="__main__":
    app.run()
