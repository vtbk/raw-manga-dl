from abc import ABC, abstractmethod
from PIL import Image
import requests
import time
import random
import io

class Service(ABC):
    def __init__(self, decoder = None):
        self.decoder = decoder

    def supports_url(self, url: str):
        return url.startswith(self.get_base_url())

    def request(self, url: str):
        sleeptime = random.randint(200, 2000) #TO-DO: implement proper rate limiting..
        time.sleep(sleeptime / 1000)
        return requests.get(url)

    def request_image(self, url):
        sleeptime = random.randint(200, 1000) #TO-DO: implement proper rate limiting..
        time.sleep(sleeptime / 1000)
        imageByteRepresentation = requests.get(url).content
        byteStream = io.BytesIO(imageByteRepresentation)
        return Image.open(byteStream)

    @abstractmethod
    def download(self, chapter_url, storage):
        pass

    @abstractmethod
    def get_base_url(self):
        pass

    @abstractmethod
    def getAvailableChapters(self, mangaInfoUrl):
        pass
