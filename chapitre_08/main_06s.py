import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from pathlib import Path
from time import perf_counter, perf_counter_ns


def main():
    """ """
    # start_time = perf_counter_ns()
    start_time = perf_counter()
    url = "https://logs.eolem.com/"
    # NOTE: creating downlaod folder with pathlib
    download_dir = Path("chapitre_08") / "download"
    download_dir.mkdir(exist_ok=True)

    req = requests.get(url=url)
    print(req.text)
    soup = BeautifulSoup(req.text, "html.parser")
    # NOTE: the fast simpel way
    all_infos = soup.find_all("a")
    # pprint(all_infos)
    # print(all_infos)

    for info in all_infos:
        list_all = [info["href"] for info in all_infos if info["href"].endswith(".log")]

    # list_all = [info["href"] for info in BeautifulSoup(req.text, "html.parser") if info["href"].endswith(".log")]
    print(list_all)
    for file in list_all:
        url_file = f"{url}/{file}"
        download_file = download_dir / file
        print(f"Downloading {url_file}")
        destination = download_dir / url_file
        request = requests.get(url=url_file)
        with open(download_file, "w") as file:
            file.write(request.text)
    # end_time = perf_counter_ns()
    end_time = perf_counter()
    print(f"Time execution : {end_time - start_time:0.3f} sec")


if __name__ == "__main__":
    main()