# MAGIC Downloader
Download MAGIC data.

## Installation
```
pip install git+https://github.com/noahhdf/magic-downloader.git
```

## Usage

### Download data

Download data files from http://data.magic.pic.es/Data/:
```python
from MAGICDownloader import MAGICDownloader

base = "http://data.magic.pic.es/Data/Star/"
urls = [
    base + "v1/CrabNebula/2019_01_12/",
    base + "v1/CrabNebula/2019_01_13/",
]

downloader = MAGICDownloader("<user>", "<password>")
downloader.download_files(urls, "<output-directory>")
```

If a file is already downloaded, this file will be skipped.

### Ignore some files

It's possible to ignore some files and not download them, based on
`string`-content:
```python
downloader.download_files(urls, "<output-directory>", ignore_pattern="ignore")
```
skips files where
```python
"ignore" in filename
```
evaluates to `True`.


### Reading delayed files

Delayed files are labeled with a truck: .
These files will be skipped, if after 5 seconds the download does not start.
Just try to download again later.

If you want to wait longer and don't skip:
```python
downloader.download_files(urls, "<output-directory>", skip=False)
```
