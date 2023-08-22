# ValentinaSultryArt.py

import numpy as np
from PIL import Image, ImageDraw

class ArtGenerator:
    def __init__(self, canvas_size=1000):
        self.canvas_size = canvas_size

    def generate_sultry_art(self, num_layers=4):
        canvas = np.zeros((self.canvas_size, self.canvas_size, 3), dtype=np.uint8)
        for _ in range(num_layers):
            color = self._generate_random_color()
            canvas = self._generate_layer(canvas, color)
        return canvas

    def _generate_random_color(self):
        return np.random.randint(50, 201, size=3, dtype=np.uint8)

    def _generate_layer(self, canvas, color):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        num_shapes = np.random.randint(5, 15)
        for _ in range(num_shapes):
            shape_type = np.random.choice(["circle", "ellipse"], p=[0.6, 0.4])
            shape_size = np.random.randint(50, 200)
            shape_x = np.random.randint(0, self.canvas_size - shape_size)
            shape_y = np.random.randint(0, self.canvas_size - shape_size)
            self._draw_shape(draw, shape_type, (shape_x, shape_y, shape_x + shape_size, shape_y + shape_size), color)
        return np.array(image)

    def _draw_shape(self, draw, shape_type, position, color):
        if shape_type == "circle":
            draw.ellipse(position, fill=tuple(color))
        else:  # "ellipse"
            draw.ellipse(position, fill=tuple(color))
            
    def display_artwork(self, artwork):
        Image.fromarray(artwork).show()

if __name__ == "__main__":
    canvas_size = 1000
    num_layers = 5

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_sultry_art(num_layers)
    art_generator.display_artwork(artwork)
