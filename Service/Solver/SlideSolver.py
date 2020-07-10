from PIL import Image

class SlideSolver():
    '''
    Solves scrambled image split into a 4x4 grid where the (x, y) coordinates of each tile has been swapped to (y, x)
    Right side of the scrambled image contains a z pixel wide strip which has not been scrambled. 
    "z" corresponds the floor of the width divided by 32, multiplied by 8.
    Tested images suggest that this does not occur vertically 
    '''
    def solve(self, scrambled_images, instructions):
        images = []
        for image, instruction in zip(scrambled_images, instructions):
            image_width, image_height = instruction['width'],  instruction['height']
            tile_width, tile_height = image_width // 32 * 8, image_height // 4 
            unscrambled_image = Image.new(mode='RGB', size=image.size)
            unscrambled_image.paste(image.copy())
            for x in range(0, 4):
                for y in range(0, 4):
                    source_x = x * tile_width
                    source_y = y * tile_height
                    box = (source_x, source_y, source_x + tile_width, source_y + tile_height)
                    tile = image.crop(box)
                    unscrambled_image.paste(tile, (tile_width * y, tile_height * x))
            images.append(unscrambled_image)
        return images