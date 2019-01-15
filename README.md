# timing-magic-fact
Compare timing information from the IACTs MAGIC and FACT

## Installation
```
pip install git+https://github.com/noahhdf/timing-magic-fact.git
```

## Usage

### Download data

Download data files from http://data.magic.pic.es/Data/:
```python
from timing_magic_fact.download import MAGICDownloader

base = "http://data.magic.pic.es/Data/"
urls = [
    base + "v1/CrabNebula/2019_01_12/",
    base + "v1/CrabNebula/2019_01_13/",
]

downloader = MAGICDownloader("<password>")
downloader.download_files(urls, "<output-directory>")
```
