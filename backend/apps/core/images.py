from django.conf import settings
from PIL import Image, ImageOps

def open_or_convert(content, ext):
    return Image.open(content)

def homothetical_transformation(pic, new_width=800):
    new_height = int(new_width * pic.height / pic.width)
    result = pic.copy()
    result = ImageOps.exif_transpose(result)
    result = convert_to_rgb(result)
    result.thumbnail((new_width, new_height))

    return result

def convert_to_rgb(image):
    if image.mode == 'P':
        image = image.convert('RGB')
        return image

    if image.mode not in ['RGBA', 'LA']:
        return image

    background = Image.new("RGB", image.size, (255, 255, 255))
    background.paste(image, mask=image.split()[3])  # better handling for transparent images

    return background