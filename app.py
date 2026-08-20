from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/naruto")
def naruto():
    return render_template("naruto.html")


@app.route("/naruto/episode/<int:episode>")
def naruto_episode(episode):
    return render_template("episode.html", episode=episode)


if __name__ == "__main__":
    app.run(debug=True)