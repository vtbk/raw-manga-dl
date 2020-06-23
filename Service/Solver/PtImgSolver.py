from PIL import Image
import re
import io

class PtImgSolver():
    def solve(self, scrambled_images, instructions):
        unscrambled_images = []
        for scrambled_image, data in zip(scrambled_images, instructions):
            movements = data['coords']
            width = data['width']
            height = data['height']
            unscrambled_image = Image.new(mode = "RGB", size = (width, height))
            for move in movements:
                self._apply_move(scrambled_image, unscrambled_image, move)
            unscrambled_images.append(unscrambled_image)
        return unscrambled_images

    def _apply_move(self, original_image, new_image, move):
            movement = re.split(':|\+|>|,', move)
            source_x = movement[1]
            source_y = movement[2]
            box_width = movement[3]
            box_height = movement[4]
            destination_x = movement[5]
            destination_y = movement[6]

            sourceBox = (int(source_x), int(source_y), int(source_x) + int(box_width), int(source_y) + int(box_height)) 
            destination = (int(destination_x), int(destination_y))
            tile = original_image.crop(sourceBox)
            new_image.paste(tile, destination)
            return new_image


