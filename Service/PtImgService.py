from abc import ABC, abstractmethod
from .Service import Service
from bs4 import BeautifulSoup
import json

'''
Base class with common operations used for services that implement ptimg DRM
Pages contain elements with html elements implementing a custom tag referencing to pt-img.json files
These pt-img.json files contain the location of the actual scrambled image and the unscrambling steps
'''
class PtImgService(Service, ABC):

    def download(self, chapter_url, storage):
        soup = self._get_soup_from_url(chapter_url)
        identifier = self._get_chapter_title_from_page(soup)
        page_specs = self._get_page_specs(soup, chapter_url)
        scrambled_images = self._get_page_images(page_specs, chapter_url)
        instructions = self._get_instructions(page_specs)
        unscrambled_images = self.decoder.solve(scrambled_images, instructions)
        storage.store(unscrambled_images, identifier)

    def _get_page_specs(self, soup, chapter_url):
        page_spec_locations = self._get_page_spec_locations_from_page(soup)
        page_specs = []
        for page_spec_location in page_spec_locations:
            page_spec = json.loads(super().request(chapter_url + '/' + page_spec_location).text)
            page_specs.append(page_spec)
        return page_specs
    
    def _get_page_images(self, page_specs, chapter_url):
        images = []
        for page_spec in page_specs:
            image_location = page_spec['resources']['i']['src']
            image = super().request_image(chapter_url + 'data/' + image_location)
            images.append(image)
        return images
    
    def _get_instructions(self, page_data):
        return [point['views'][0] for point in page_data]

    #TO:DO verify whether all services that implement ptimg use the same reader software, because if that were to
    #be the case there would be no use making this abstract
    @abstractmethod
    def _get_page_spec_locations_from_page(self, soup):
        pass

    @abstractmethod
    def _get_chapter_title_from_page(self, soup):
        pass



