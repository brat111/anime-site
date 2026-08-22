from flask import Flask, render_template, Response

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


@app.route("/robots.txt")
def robots():
    return Response(
        """User-agent: *
Allow: /

Sitemap: https://anime-site-q04r.onrender.com/sitemap.xml
""",
        mimetype="text/plain"
    )


@app.route("/sitemap.xml")
def sitemap():
    urls = [
        "https://anime-site-q04r.onrender.com/",
        "https://anime-site-q04r.onrender.com/naruto",
        "https://anime-site-q04r.onrender.com/naruto/episode/1",
        "https://anime-site-q04r.onrender.com/naruto/episode/2"
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    for url in urls:
        xml += f"<url><loc>{url}</loc></url>"

    xml += "</urlset>"

    return Response(xml, mimetype="application/xml")


if __name__ == "__main__":
    app.run()