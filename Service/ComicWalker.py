from .Service import Service
from bs4 import BeautifulSoup
import json
class ComicWalker(Service):
    chapter_base_url = 'https://comic-walker.com'
    api_base_url ='https://manga-api.nicoseiga.jp/api/v1/comicwalker'

    def download(self, chapter_url:str, storage):
        chapter_id = chapter_url.split('=')[-1] 
        chapter_info = self._get_chapter_info(chapter_id)
        chapter_frames = self._get_chapter_frames(chapter_id)
        identifier = '{}_{}'.format(chapter_id, chapter_info['meta']['title']) 
        images = self.decoder.solve(self._fetch_images_as_bytes(chapter_frames), self._get_drm_hashes_from_frames(chapter_frames))
        storage.store(images, identifier)

    def _get_chapter_info(self, chapter_id):
        url = '{}/contents/{}'.format(self.api_base_url, chapter_id)
        return json.loads(super().request(url).content)['data']['result']

    def _get_chapter_frames(self, chapter_id):
        url = '{}/episodes/{}/frames'.format(self.api_base_url, chapter_id)
        return json.loads(super().request(url).content)['data']['result']

    def _fetch_images_as_bytes(self, frames):
        images = []
        for frame in frames:
            url = frame['meta']['source_url']
            image_as_bytes = super().request(url).content
            images.append(image_as_bytes)
        return images
    
    def _get_drm_hashes_from_frames(self, frames):
        return [frame['meta']['drm_hash'] for frame in frames]

    def get_base_url(self):
        return self.chapter_base_url

    def get_available_chapters(self, overview_url):
        raise NotImplementedError
