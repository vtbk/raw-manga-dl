from PIL import Image
import os
class FolderStorage():
    path = None
    def __init__(self, path):
        if path[-1] != '/':
            path += '/'
        self.path = path
        self._createPath(path)
    
    def store(self, images):
        for i, image in enumerate(images):
            filename = str(i) + '.jpg'
            filename = filename.rjust(7, '0') 
            image.save(self.path + filename)
    
    def _createPath(self, path):
        if not os.path.exists(path):
            os.makedirs(path)