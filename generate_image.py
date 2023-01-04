from PIL import Image, ImageDraw, ImageFont

def create_image(size, bgColor, message, font, fontColor):
    W, H = size
    image = Image.new('RGB', size, bgColor)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)/2, (H-h)/2), message, font=font, fill=fontColor)
    return image


def get_scaled_font(fontName, text, imageWidth, maxSpanPercentage=0.75, startingSize=16):
    maxTextWidth = imageWidth * maxSpanPercentage
    fontsize = startingSize
    font = ImageFont.truetype(fontName, fontsize)
    while font.getsize(text)[0] < maxTextWidth:
        # iterate until the text size is just larger than the target max size
        fontsize += 1
        font = ImageFont.truetype(fontName, fontsize)
    return font


def draw_text(image, font, text, color, y=20):
    W, H = image.size
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), text, font=font)
    # draw.text(((W-w)/2, (H-h)/2), text, font=font,
    #           fill=color, stroke_width=3, stroke_fill="black")
    draw.text(((W-w)/2, y), text, font=font,
              fill=color, stroke_width=3, stroke_fill="black")
    return image


def generate_image(bgName, fontName, text, outputName):
    img = Image.open(bgName, mode="r")
    font = get_scaled_font(fontName, text, img.size[0])
    new_img = draw_text(img, font, text, "white")
    new_img.save(outputName, "PNG")
