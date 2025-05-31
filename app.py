import os , json
from scrape import hook
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

CACHE_FILE = "cache.json"
MOVIE_DIR = "D:/Plex/Movies"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


@app.route("/")
def index():
    movies = []
    cache = load_cache()

    for filename in os.listdir(MOVIE_DIR):
        if filename.lower().endswith(('.mp4', '.mkv', '.avi')):
            title = filename

            if title in cache:
                imdb_data = cache[title]
            else:
                imdb_data = hook(title)
                if imdb_data:
                    cache[title] = imdb_data
                    save_cache(cache)  # move this after cache update

            if imdb_data:
                movies.append({
                    "title": imdb_data['title'],
                    "poster": imdb_data['poster'],
                    "url": imdb_data['url'],
                    "filename": filename
                })
            else:
                movies.append({
                    "title": title,
                    "poster": "",
                    "url": "#",
                    "filename": filename
                })

    return render_template("index.html", movies=movies)

@app.route("/search")
def search():
    query = request.args.get("query", "").lower()
    cache = load_cache()
    movies = []

    for filename in os.listdir(MOVIE_DIR):
        if filename.lower().endswith(('.mp4', '.mkv', '.avi')) and query in filename.lower():
            title = filename

            imdb_data = cache.get(title) or hook(title)
            if imdb_data:
                cache[title] = imdb_data
                save_cache(cache)

                movies.append({
                    "title": imdb_data['title'],
                    "poster": imdb_data['poster'],
                    "url": imdb_data['url'],
                    "filename": filename
                })
            else:
                movies.append({
                    "title": title,
                    "poster": "",
                    "url": "#",
                    "filename": filename
                })

    return render_template("index.html", movies=movies)

@app.route("/watch/<filename>")
def watch(filename):
    video_path = os.path.join(MOVIE_DIR, filename)
    if not os.path.exists(video_path):
        return "Movie not found 🫠", 404
    return render_template("watch.html", filename=filename)


@app.route("/stream/<filename>")
def stream(filename):
    return send_from_directory(MOVIE_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' , port='80')
