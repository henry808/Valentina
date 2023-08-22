# ArtisticVisionary.py

import numpy as np
from PIL import Image, ImageDraw

class ArtGenerator:
    def __init__(self, canvas_size=1200):
        self.canvas_size = canvas_size

    def generate_abstract_art(self, num_layers=6):
        canvas = np.zeros((self.canvas_size, self.canvas_size, 3), dtype=np.uint8)
        for _ in range(num_layers):
            color = self._generate_random_color()
            canvas = self._generate_layer(canvas, color)
        return canvas

    def _generate_random_color(self):
        return np.random.randint(0, 256, size=3, dtype=np.uint8)

    def _generate_layer(self, canvas, color):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        num_shapes = np.random.randint(8, 20)
        for _ in range(num_shapes):
            shape_type = np.random.choice(["circle", "rectangle", "ellipse"], p=[0.5, 0.3, 0.2])
            shape_size = np.random.randint(20, 150)
            shape_x = np.random.randint(0, self.canvas_size - shape_size)
            shape_y = np.random.randint(0, self.canvas_size - shape_size)
            self._draw_shape(draw, shape_type, (shape_x, shape_y, shape_x + shape_size, shape_y + shape_size), color)
        return np.array(image)

    def _draw_shape(self, draw, shape_type, position, color):
        if shape_type == "circle":
            draw.ellipse(position, fill=tuple(color))
        elif shape_type == "rectangle":
            draw.rectangle(position, fill=tuple(color))
        else:  # "ellipse"
            draw.ellipse(position, fill=tuple(color))
            
    def display_artwork(self, artwork):
        Image.fromarray(artwork).show()

if __name__ == "__main__":
    canvas_size = 1200
    num_layers = 7

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_abstract_art(num_layers)
    art_generator.display_artwork(artwork)
