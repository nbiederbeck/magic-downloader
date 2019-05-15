"""Loop over all files in given *days*"""
import requests
import bs4
from tqdm import tqdm
from os import path, makedirs


class MAGICDownloader:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def download_files(
        self,
        urls: list,
        output_directory: str = ".",
        ignore_pattern=None,
        chunk_size=1024,
        skip=True,
    ):
        makedirs(output_directory, exist_ok=True)
        for url in urls:
            page = requests.get(url, auth=(self.user, self.password))
            if not page.ok:
                day = url.split("/")[-2]
                print(f"No data found for {day}")
                continue
            soup = bs4.BeautifulSoup(page.text, "lxml")
            table_rows = soup.find_all("tr")

            # skip table header row
            for row in table_rows[1:]:
                file = row.find_all("a", download=True)[0]
                filename = file.attrs["download"]
                if ignore_pattern is not None:
                    if ignore_pattern in filename:
                        print(f"Ignoring {filename}")
                        continue
                local_filename = f"{output_directory}/{filename}"
                if path.exists(local_filename):
                    print(f"Not downloading existing {local_filename}")
                    continue
                download_url = url + filename
                try:
                    availability = row.find_all("i")[0].attrs["title"]
                except KeyError:
                    availability = row.find_all("span")[0].attrs["title"]
                print(file.attrs["title"])
                print(availability)
                try:
                    stream = requests.get(
                        download_url,
                        stream=True,
                        auth=(self.user, self.password),
                        timeout=5,
                    )
                except requests.exceptions.ReadTimeout:
                    if availability.startswith("Reading") and skip:
                        print("Skipping. Try again later.")
                        continue
                file_size = stream.headers["content-length"]
                with open(local_filename, "wb") as f:
                    for chunk in tqdm(
                        stream.iter_content(chunk_size=chunk_size),
                        total=int(int(file_size) / chunk_size),
                    ):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
