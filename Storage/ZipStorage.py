from .FolderStorage import FolderStorage
import os
import shutil
class ZipStorage(FolderStorage):

    '''
    First stores the image files in a folder based on base_path + identifier, then creates a base_path + identifier.zip
    and removes the temporary folder
    '''
    def store(self, images, identifier):
        path = super().store(images, identifier)
        shutil.make_archive(path, 'zip', path)
        shutil.rmtree(path)
        return path + '.zip'