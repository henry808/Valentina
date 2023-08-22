# ValentinaCrowArtMystery.py

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

class ArtGenerator:
    def __init__(self, canvas_size=1000):
        self.canvas_size = canvas_size
        self.crow_silhouette = Image.open("flying_crow.png").convert('RGBA')  # Assuming you have a crow silhouette PNG image

    def generate_mysterious_art(self, num_crows=50, num_moons=3, num_swirls=5):
        canvas = self._generate_light_background()
        for _ in range(num_crows):
            canvas = self._add_crow(canvas)
        for _ in range(num_moons):
            canvas = self._add_moon(canvas)
        for _ in range(num_swirls):
            canvas = self._draw_swirl(canvas)
        canvas = self._add_stars(canvas)
        return np.array(canvas)

    def _generate_light_background(self):
        soft_palette = [(np.random.randint(180, 240), np.random.randint(180, 240), np.random.randint(180, 240)),  # darker grays
                        (np.random.randint(190, 240), np.random.randint(210, 240), np.random.randint(240, 255)),    # light blues
                        (np.random.randint(240, 255), np.random.randint(220, 235), np.random.randint(180, 200))]   # muted golds
        color = np.array(soft_palette[np.random.choice(len(soft_palette))], dtype=np.uint8)
        return np.full((self.canvas_size, self.canvas_size, 3), color, dtype=np.uint8)

    def _add_crow(self, canvas):
        image = Image.fromarray(canvas)
        crow_size = np.random.randint(20, 100)
        crow = self.crow_silhouette.resize((crow_size, int(crow_size * self.crow_silhouette.height / self.crow_silhouette.width)))
        if np.random.rand() > 0.5:
            crow = ImageOps.mirror(crow)
        position = (np.random.randint(0, self.canvas_size - crow.width), np.random.randint(0, self.canvas_size - crow.height))
        image.paste(crow, position, crow)
        return np.array(image)

    def _add_moon(self, canvas):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        diameter = np.random.randint(50, 200)
        position = (np.random.randint(0, self.canvas_size - diameter), np.random.randint(0, self.canvas_size - diameter))
        draw.ellipse([position[0], position[1], position[0] + diameter, position[1] + diameter], fill="white", outline="gray")
        return np.array(image)

    def _draw_swirl(self, canvas):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        center_pos = (np.random.randint(0, self.canvas_size), np.random.randint(0, self.canvas_size))
        num_turns = np.random.randint(3, 7)  # Decide how "swirly" the spiral is
        
        last_point = None
        for i in range(100):  # Drawing lines in a spiral using trigonometric functions
            angle = 0.1 * i
            x = center_pos[0] + (1 + angle) * np.sin(angle) * 20
            y = center_pos[1] + (1 + angle) * np.cos(angle) * 20
            current_point = (x, y)
            if last_point:
                swirl_color = (np.random.randint(80, 140), np.random.randint(80, 140), np.random.randint(80, 140))  # darker grays
                draw.line([last_point, current_point], fill=swirl_color, width=2)
            last_point = current_point
        return np.array(image)


    def _add_stars(self, canvas):
        image = Image.fromarray(canvas)
        draw = ImageDraw.Draw(image)
        for _ in range(500):  # Drawing 500 stars
            position = (np.random.randint(0, self.canvas_size), np.random.randint(0, self.canvas_size))
            star_size = np.random.randint(1, 3)  # Variable star size for depth
            draw.ellipse([position[0], position[1], position[0] + star_size, position[1] + star_size], fill="white")
        return np.array(image)


    def display_artwork(self, artwork):
        Image.fromarray(artwork).show()

if __name__ == "__main__":
    canvas_size = 1000
    num_crows = 60

    art_generator = ArtGenerator(canvas_size)

    artwork = art_generator.generate_mysterious_art(num_crows)
    art_generator.display_artwork(artwork)
