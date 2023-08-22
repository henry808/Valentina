# ArtisticVisionary.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

class ArtGenerator:
    def __init__(self, canvas_size=800):
        self.canvas_size = canvas_size

    def generate_abstract_art(self, num_layers=3):
        canvas = np.zeros((self.canvas_size, self.canvas_size, 3))
        for _ in range(num_layers):
            color = self._generate_random_color()
            layer = self._generate_layer(color)
            canvas = np.add(canvas, layer)
        return np.clip(canvas, 0, 1)

    def _generate_random_color(self):
        return np.random.rand(3)

    def _generate_layer(self, color):
        layer = np.zeros((self.canvas_size, self.canvas_size, 3))
        num_shapes = np.random.randint(5, 20)
        for _ in range(num_shapes):
            shape_color = self._generate_random_color()
            shape_size = np.random.randint(10, 100)
            shape_x = np.random.randint(0, self.canvas_size)
            shape_y = np.random.randint(0, self.canvas_size)
            layer = self._draw_shape(layer, shape_x, shape_y, shape_size, shape_color)
        return layer

    def _draw_shape(self, layer, x, y, size, color):
        shape = np.random.rand(size, size, 3) * color
        x_end = min(x + size, self.canvas_size)
        y_end = min(y + size, self.canvas_size)
        layer[x:x_end, y:y_end, :] += shape[:x_end - x, :y_end - y, :]
        return layer

    def display_artwork(self, artwork):
        cmap = LinearSegmentedColormap.from_list("custom_cmap", [(0, 0, 0), (1, 1, 1)])
        plt.imshow(artwork, cmap=cmap)
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    canvas_size = 800
    num_layers = 5

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_abstract_art(num_layers)
    art_generator.display_artwork(artwork)
