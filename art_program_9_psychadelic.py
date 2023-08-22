# ValentinaPsychedelicArt.py

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

class ArtGenerator:
    def __init__(self, canvas_size=1000):
        self.canvas_size = canvas_size

    def generate_balanced_art(self, num_layers=7):
        canvas = self._generate_dark_background()
        for _ in range(num_layers):
            color = self._generate_sultry_color()
            canvas = self._generate_layer(canvas, color)
        canvas = Image.fromarray(canvas).filter(ImageFilter.GaussianBlur(2))
        return np.array(canvas)

    def _generate_sultry_color(self):
        sultry_palette = [(np.random.randint(140, 210), np.random.randint(0, 60), np.random.randint(100, 170)),  # sultry reds
                          (np.random.randint(80, 130), np.random.randint(0, 50), np.random.randint(140, 200)),   # sultry purples
                          (np.random.randint(180, 230), np.random.randint(160, 220), 0)]                        # gold
        return np.array(sultry_palette[np.random.choice(len(sultry_palette))], dtype=np.uint8)

    def _generate_dark_background(self):
        dark_shades = np.random.randint(0, 60, size=(self.canvas_size, self.canvas_size, 3), dtype=np.uint8)
        return dark_shades

    def _generate_layer(self, canvas, color):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        num_shapes = np.random.randint(4, 9)
        for _ in range(num_shapes):
            shape_type = np.random.choice(["circle", "swirl", "curve"], p=[0.3, 0.4, 0.3])
            shape_size = np.random.randint(50, 300)
            shape_x = np.random.randint(0, self.canvas_size - shape_size)
            shape_y = np.random.randint(0, self.canvas_size - shape_size)
            self._draw_shape(draw, shape_type, (shape_x, shape_y, shape_x + shape_size, shape_y + shape_size), color)
        return np.array(image)

    def _draw_shape(self, draw, shape_type, position, color):
        if shape_type == "circle":
            draw.ellipse(position, fill=tuple(color), outline=tuple(color), width=5)
        elif shape_type == "swirl":
            for i in range(3):  # Repeated patterns for the psychedelic effect
                offset = i * 20
                draw.arc([position[0] + offset, position[1] + offset, position[2] - offset, position[3] - offset], 
                         start=np.random.randint(0, 360), end=np.random.randint(0, 360), fill=tuple(color), width=8)
        else:  # "curve"
            control_x = position[0] + (position[2] - position[0]) / np.random.uniform(1.2, 2.5)
            control_y = position[1] + (position[3] - position[1]) / np.random.uniform(1.2, 2.5)
            draw.line([position[0], position[1], control_x, control_y, position[2], position[3]],
                      fill=tuple(color), width=15)

    def display_artwork(self, artwork):
        Image.fromarray(artwork).show()

if __name__ == "__main__":
    canvas_size = 1000
    num_layers = 6

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_balanced_art(num_layers)
    art_generator.display_artwork(artwork)
