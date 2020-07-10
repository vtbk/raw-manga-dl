from .Service import Service
from bs4 import BeautifulSoup
import json

class ComicDays(Service):
    _base_url = 'https://comic-days.com/episode/' #does not support paywall/auth locked /volume/{id} links

    def download(self, chapter_url, storage): 
        soup = self._get_soup_from_url(chapter_url)
        page_specs = self._get_page_specs(soup)
        scrambled_images = self._get_page_images(page_specs)
        images = self.decoder.solve(scrambled_images, page_specs)
        storage.store(images, self._get_title_from_page(soup))

    def _get_page_specs(self, soup):
        pages_string = soup.find('script', {'id':'episode-json'}).get('data-value')
        page_specs = json.loads(pages_string)['readableProduct']['pageStructure']['pages']
        page_specs = [page for page in page_specs if page['type'] == 'main'] #filter advertisement placeholders
        return page_specs

    def _get_page_images(self, page_specs):
        images = []
        for page_image_spec in page_specs:
            images.append(super().request_image(page_image_spec['src']))
        return images

    def _get_title_from_page(self, soup):
        manga_name = soup.find('h1', attrs={'class':'series-header-title'}).text
        chapter_title = soup.find('h1', attrs={'class':'episode-header-title'}).text
        return '{}-{}'.format(manga_name, chapter_title)
 
    def get_base_url(self):
        return self._base_url

    def get_available_chapters(self, overview_url):
        raise NotImplementedError