
from PIL import Image


def process_image(input_path, output_path):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if r < 245 and g < 245 and b < 245:
                pixels[x, y] = (0, 0, 255-b)

    img.save(output_path)
    print(f"Processing finished. Saved as: {output_path}")


process_image("input.bmp", "output.bmp")
