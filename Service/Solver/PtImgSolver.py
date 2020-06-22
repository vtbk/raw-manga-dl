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
            sourceX = movement[1]
            sourceY = movement[2]
            boxWidth = movement[3]
            boxHeight = movement[4]
            destinationX = movement[5]
            destinationY = movement[6]

            sourceBox = (int(sourceX), int(sourceY), int(sourceX) + int(boxWidth), int(sourceY) + int(boxHeight)) 
            destination = (int(destinationX), int(destinationY))
            tile = original_image.crop(sourceBox)
            new_image.paste(tile, destination)
            return new_image


