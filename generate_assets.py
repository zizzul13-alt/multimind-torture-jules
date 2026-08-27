import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def generate_textures():
    # 1. Tactical grid texture for Arknights reference & Morphology 1
    img1 = Image.new('RGBA', (400, 400), (10, 15, 24, 255))
    draw1 = ImageDraw.Draw(img1)
    for x in range(0, 400, 20):
        draw1.line([(x, 0), (x, 400)], fill=(30, 45, 65, 120), width=1)
    for y in range(0, 400, 20):
        draw1.line([(0, y), (400, y)], fill=(30, 45, 65, 120), width=1)
    # Add tactical hazard stripes & crosshairs
    for i in range(-400, 800, 40):
        draw1.line([(i, 0), (i + 20, 400)], fill=(255, 180, 0, 15), width=2)
    draw1.rectangle([180, 180, 220, 220], outline=(0, 230, 200, 180), width=1)
    img1.save('static/images/tactical_grid.png')

    # 2. Luxury paper/sand texture for Dioriviera reference & Morphology 2
    img2 = Image.new('RGBA', (500, 500), (247, 245, 240, 255))
    draw2 = ImageDraw.Draw(img2)
    # Subtle noise / material grain
    import random
    random.seed(42)
    for _ in range(15000):
        x = random.randint(0, 499)
        y = random.randint(0, 499)
        val = random.randint(220, 240)
        draw2.point((x, y), fill=(val, val - 10, val - 20, 40))
    img2.save('static/images/luxury_paper.png')

    # 3. Ambient animated gradient frames (GIF) for loading state
    frames = []
    for f in range(20):
        frame = Image.new('RGBA', (300, 300), (5, 8, 15, 255))
        d = ImageDraw.Draw(frame)
        angle = (f / 20.0) * 2 * math.pi
        cx, cy = 150 + int(40 * math.cos(angle)), 150 + int(40 * math.sin(angle))
        d.ellipse([cx - 80, cy - 80, cx + 80, cy + 80], fill=(0, 210, 255, 60))
        cx2, cy2 = 150 - int(50 * math.cos(angle)), 150 - int(50 * math.sin(angle))
        d.ellipse([cx2 - 60, cy2 - 60, cx2 + 60, cy2 + 60], fill=(255, 0, 110, 50))
        frame = frame.filter(ImageFilter.GaussianBlur(15))
        frames.append(frame)
    frames[0].save('static/images/ambient_loader.gif', save_all=True, append_images=frames[1:], loop=0, duration=50)

    print("Material assets generated successfully!")

if __name__ == '__main__':
    generate_textures()
