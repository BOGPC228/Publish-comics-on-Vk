import requests
import os
import json

from download import download_img

def get_comix(url, directory):
    response = requests.get(url)
    response.raise_for_status()
    filename = "Comix"
    url_img = response.json()
    file_path = os.path.join(directory, filename)
    download_img(url_img, file_path, payload=None)


def download_comix(url, file_path, payload=None):
    response = requests.get(url, payload)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def main():
    url = "https://xkcd.com/info.0.json"
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    get_comix(directory)


if __name__ == "__main__":
    main()