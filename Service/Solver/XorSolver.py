from itertools import cycle
from PIL import Image
from io import BytesIO

class XorSolver():

    def solve(self, sources, drm_hashes):
        images = []
        for source, drm_hash in zip(sources, drm_hashes):
            decoded_image_bytes = bytearray()
            for a, b in zip(source, cycle(bytes.fromhex(drm_hash[0:16]))):
                decoded_image_bytes.append(a ^ b)
            decoded_image = Image.open(BytesIO(decoded_image_bytes))
            images.append(decoded_image)
        return images