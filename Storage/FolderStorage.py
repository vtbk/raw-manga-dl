from PIL import Image
import os
class FolderStorage():
    base_path = None

    def __init__(self, path):
        if path[-1] != '/':
            path += '/'
        self.base_path = path
    
    def store(self, images, identifier: str):
        if identifier is None:
            raise TypeError
        identifier = identifier.replace(' ', '_')
        path = self.base_path + identifier + '/'
        self._createPath(path)
        for i, image in enumerate(images):
            filename = str(i) + '.jpg'
            filename = filename.rjust(7, '0') 
            image.save(path + filename)
        return path
        
    def _createPath(self, path):
        if not os.path.exists(path):
            os.makedirs(path)