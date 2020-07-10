from .PtImgService import PtImgService

class ComicTrail(PtImgService):
    _base_url = 'https://comic-trail.jp'

    def _get_page_spec_locations_from_page(self, soup):
        return  [el.get("data-ptimg") for el in soup.find_all("div", attrs={"data-ptimg":True})]

    def get_base_url(self):
        return self._base_url

    def get_available_chapters(self, overview_url):
        raise NotImplementedError

    def _get_chapter_title_from_page(self, soup):
        return soup.find("title").string