import httpx
from bs4 import BeautifulSoup, Tag
from pathlib import Path

response = httpx.get("https://kwejk.pl/")
response.raise_for_status()
html = BeautifulSoup(response.text, features = "html.parser")
images = html.find_all("img", attrs = {"class": "full-image"})


"""
Pobierz obrazki do folderu jpgs
"""

def download_jpg(url : str, filename: str):
    response = httpx.get(url)
    jpg_file = open(Path(__file__).parent / "jpgs" / filename, "wb")
    jpg_file.write(response.content)

for image in images:
    image: Tag
    url = image.attrs["src"]
    print(url)
    name = image.attrs["alt"]+".jpg"
    print(name)
    download_jpg(url, name)

"""
Używając html.find znajdź aktualnie najnowszą stronę memów: 57132
"""

def find_newest_page_number(xml_tag: Tag) -> int:
    tags_with_kwejk_href = xml_tag.find_all("a", attrs = {"href": "https://kwejk.pl"})
    for tag in tags_with_kwejk_href:
        if tag.text.isnumeric():
            return int(tag.text)

find_newest_page_number()