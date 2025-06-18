import re
import os
import requests
from bs4 import BeautifulSoup

def imdb_search(query, filename=None):  # filename helps us name the image file
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://www.imdb.com/find/?q={query.replace(' ', '+')}&s=tt&ttype=ft&ref_=fn_ft"
    res = requests.get(search_url, headers=headers)
    
    if res.status_code != 200:
        print("IMDb request failed 🚫")
        return None

    soup = BeautifulSoup(res.text, "html.parser")
    result_section = soup.find("section", {"data-testid": "find-results-section-title"})
    if not result_section:
        print("No result section found 😕")
        return None

    first_result = result_section.select_one("ul > li")
    if not first_result:
        print("No movie result found 🚫")
        return None

    title_tag = first_result.find("a")
    if not title_tag:
        print("No link in result ❌")
        return None

    title = title_tag.text.strip()
    link = "https://www.imdb.com" + title_tag["href"].split("?")[0]

    img_tag = first_result.find("img")
    poster_url = get_high_res_img_url(img_tag["src"] if img_tag else "")

    local_img_path = download_image(poster_url, filename)

    return {
        "title": title,
        "url": link,
        "poster": local_img_path  # use local image
    }


def download_image(url, filename):
    if not url:
        return ""
    
    ext = url.split('.')[-1].split('?')[0]  # .jpg, .png, etc.
    safe_name = os.path.splitext(filename)[0].replace(" ", "_").replace(".", "_")
    poster_folder = os.path.join("static", "posters")
    os.makedirs(poster_folder, exist_ok=True)
    
    local_path = os.path.join(poster_folder, f"{safe_name}.{ext}")
    
    # Normalize to forward slashes before returning
    normalized_path = local_path.replace("\\", "/")

    if os.path.exists(local_path):
        return normalized_path  # already downloaded ✅

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"✅ Poster saved: {normalized_path}")
        else:
            print(f"❌ Image download failed ({response.status_code})")
            return ""
    except Exception as e:
        print(f"❌ Error downloading image: {e}")
        return ""

    return normalized_path

#cleaning title
def clean_movie_title(filename):
    name = os.path.splitext(filename)[0]  # Remove extension
    name = name.replace('.', ' ')  # Replace dots with spaces
    name = re.sub(r'\(.*?\)', '', name)  # Remove (2013)
    name = re.sub(r'\[.*?\]', '', name)  # Remove [stuff]
    name = re.sub(r'\b(Bluray|BluRay|BRRip|WEBRip|720P|1080P|x264|H264|Dual Audio|YIFY|AAC|HDRip|HEVC|HD|480p|2160p|4K|WEB-DL|DVD|CAM|TS|FS|PDVDRip|DVDRip|XviD|DTS|ESubs|mp4|mkv|avi|2016|Sinhala|English|Theligu|(2025)|Telugu|HDLeak-|Malayalam|Hindi|Tamil|Thamil|2013|2024|2025|Telugu|1080p|10bit|DS4K|AMZN|WEBRip|Multi3|DDP5|CineSubz.com|-|x|20\d{2})\b', '', name, flags=re.IGNORECASE)
    name = re.sub(r'[^a-zA-Z0-9\s]', '', name)  # Remove weird symbols
    name = re.sub(r'\s+', ' ', name).strip()  # Clean up spacing
    return name


def get_high_res_img_url(thumbnail_url):
    # Replace the sizing/cropping part between '@.' and '.jpg'
    new_url = re.sub(r'(_V1_).*?(\.jpg)', r'_V1_FMjpg_UX1000_.jpg', thumbnail_url)
    return new_url


def hook(filename):
    print(filename)
    clean_title = clean_movie_title(filename)
    return imdb_search(clean_title, filename=clean_title)
