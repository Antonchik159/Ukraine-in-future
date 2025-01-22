import requests
from bs4 import BeautifulSoup
import os
import time
import json
from datetime import datetime
def get_all_pages():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    r = requests.get(url="https://uaserials.pro/films/f/year=2010;2023/imdb=0;10", headers=headers)

    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/page_1.html", "w", encoding="utf-8") as file:
        file.write(r.text)

    with open("data/page_1.html", encoding="utf-8") as file:
        src = file.read()


    soup = BeautifulSoup(src, "lxml")
    pages_count = int(soup.find("div", class_="navigation fx-row fx-center").find_all("a")[4].text)

    for i in range(1, pages_count + 1):
            url = f"https://uaserials.pro/films/f/year=2010;2023/imdb=0;10/page/{i}/"
            r = requests.get(url=url, headers=headers)

            with open(f"data/page_{i}.html", "w", encoding="utf-8") as file:
                file.write(r.text)
            time.sleep(2)
    return pages_count + 1


def collect_data(pages_count):
    cur_date = datetime.now().strftime("%d_%m_%Y")
    data = []
    for page in range(1, pages_count):
        with open(f"data/page_{page}.html", encoding="utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        items_cards = soup.find_all("div", class_="short-cols fx-row")
        for item in items_cards:
            product_name_element = item.find("div", class_="th-title truncate")
            product_name = product_name_element.text if product_name_element else "Unknown Product"

            image = item.find("img", class_="lazyload")
            if image and image.get('data-src'):
                image_ = image.get('data-src')
            else:
                image_ = "No Image"

            product_link_element = item.find("a", class_="short-img img-fit")
            if product_link_element:
                product_link = product_link_element['href']
            else:
                product_link = "No Link"

            data.append(
                {
                    "img": image_,
                    "product_name": product_name,
                    "product_link": product_link,
                }
            )
    with open("film.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def main():
    pages_count = get_all_pages()
    collect_data(pages_count=pages_count)

if __name__ == '__main__':
    main()


