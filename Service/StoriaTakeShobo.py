from .PtImgService import PtImgService
from bs4 import BeautifulSoup

class StoriaTakeShobo(PtImgService):
    _base_url = 'http://storia.takeshobo.co.jp'

    def _get_page_spec_locations_from_page(self, soup):
        return  [el.get("data-ptimg") for el in soup.find_all("div", attrs={"data-ptimg":True})]

    def get_base_url(self):
        return self._base_url

    def get_available_chapters(self, overview_url):
        raise NotImplementedError
    
    def _get_chapter_title_from_page(self, soup):
        return soup.find("meta", attrs={"property":"og:title"}).get("content")