# MovieFlask

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/Kaveen-Adithya/MovieFlask/tree/main)

MovieFlask is a simple, self-hosted movie streaming web application built with Python and Flask. It scans a local directory for your movie files, fetches metadata and posters from IMDb, and presents them in a clean web interface for browsing and streaming directly in your browser.

## Features

-   **Automatic Library Scanning:** Scans a specified directory for movie files (`.mp4`, `.mkv`, `.avi`).
-   **IMDb Metadata Fetching:** Automatically cleans movie filenames and scrapes IMDb for the correct title, poster, and IMDb page URL.
-   **Local Caching:** Caches fetched metadata in a `cache.json` file and downloads posters to the `static/posters` directory to minimize API calls and speed up subsequent loads.
-   **Web-Based Streaming:** Stream your movies directly in the browser using a simple HTML5 video player.
-   **Search Functionality:** Filter your movie collection by title.
-   **Responsive UI:** A clean, Netflix-inspired interface that works on both desktop and mobile devices.

## How It Works

1.  **Flask Backend (`app.py`):** The main application handles HTTP requests.
    -   The `/` route scans the movie directory, checks the cache for existing metadata, or calls the scraper for new files. It then renders the movie grid.
    -   The `/search` route filters the movie list based on a query.
    -   The `/watch/<filename>` route displays the video player page.
    -   The `/stream/<filename>` route serves the actual video file for streaming.
2.  **IMDb Scraper (`scrape.py`):**
    -   Cleans the movie filename by removing common tags (like `1080p`, `Bluray`, `YIFY`) and special characters to create a clean search query.
    -   Searches IMDb with the cleaned title and parses the first result to get the movie's title, poster URL, and IMDb link.
    -   Downloads a high-resolution version of the poster and saves it locally.
3.  **Frontend (`templates/` & `static/`):**
    -   The UI is built with simple HTML, CSS, and a touch of JavaScript.
    -   `index.html` displays the movie library in a responsive grid.
    -   `watch.html` provides the video player interface.

## Setup and Installation

### 1. Prerequisites

-   Python 3.x
-   `pip` package installer

### 2. Clone the Repository

```bash
git clone https://github.com/kaveen-adithya/movieflask.git
cd movieflask
```

### 3. Install Dependencies

Install the required Python packages using `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configure Your Movie Directory

You must edit the `app.py` file to point to your local movie folder. Open `app.py` and change the `MOVIE_DIR` variable to the absolute path of your movie collection.

```python
# app.py

# ...
CACHE_FILE = "cache.json"
MOVIE_DIR = "D:/Plex/Movies" # <-- CHANGE THIS PATH
# ...
```

For example, on Linux or macOS, it might look like this:
`MOVIE_DIR = "/home/user/Videos/Movies"`

### 5. Run the Application

Start the Flask development server.

```bash
python app.py
```

The application will be accessible at `http://0.0.0.0:80` or `http://localhost:80`. The first time you run the app, it may take a while to load as it needs to scrape metadata and download posters for your entire collection.

## License

This project is licensed under the Mozilla Public License 2.0. See the [LICENSE](LICENSE) file for more details.
## Contribution 4/20
- **Date**: 2026-01-09 13:47:03
- **Update**: Data point 6756

## Contribution 15/20
- **Date**: 2026-01-09 14:23:03
- **Update**: Data point 1045

## Contribution 4/20
- **Date**: 2026-02-08 14:27:36
- **Update**: Data point 8621

## Contribution 15/20
- **Date**: 2026-02-08 11:53:36
- **Update**: Data point 1557

