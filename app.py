from flask import Flask, render_template

app = Flask(__name__)

VIDEO_IDS = {
    1: "34sl",
    2: "43vq7",
    3: "",
    4: "",
    5: ""
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/naruto")
def naruto():
    return render_template("naruto.html")


@app.route("/naruto/episode/<int:episode>")
def naruto_episode(episode):
    video_id = VIDEO_IDS.get(episode)

    if not video_id:
        return "Този епизод все още няма видео.", 404

    return render_template(
        "episode.html",
        episode=episode,
        video_id=video_id
    )


if __name__ == "__main__":
    app.run()