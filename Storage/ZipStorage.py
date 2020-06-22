from .FolderStorage import FolderStorage
import os
import shutil
class ZipStorage(FolderStorage):

    #TO:DO: this doesn't make a lot of sense from an user perspective; make it accept a path 
    #refering to a zip file, not a folder (i.e. ZipStorage(/tmp/foo.zip) instead of /tmp/foo)
    def store(self, images):
        super().store(images)
        shutil.make_archive(self.path, 'zip', self.path)
        shutil.rmtree(self.path)