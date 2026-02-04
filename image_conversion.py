from PIL import Image

def wbr_colors(source_image):
    colors = [(255, 255, 255), (0, 0, 0), (255, 0, 0)]
    source = Image.open(source_image)
    source = source.resize((400, 300), resample = Image.BILINEAR)
    source = source.convert("RGB")
    width, height = source.size
    new_image = Image.new("RGB", (width, height))
    for i in range(width):
        for j in range(height):
            (r, g, b) = source.getpixel((i, j))
            new_pixel_color = (0, 0, 0)
            lowest_pixel_difference_index = 765
            for color in colors:
                pixel_difference_index = abs(r - color[0]) + abs(g - color[1]) + abs(b - color[2])
                if pixel_difference_index < lowest_pixel_difference_index:
                    lowest_pixel_difference_index = pixel_difference_index
                    new_pixel_color = color
            new_image.putpixel((i, j), new_pixel_color)
    new_image.save("wbr_image.png")


def get_bitmaps(source_image):
    source = Image.open(source_image)
    source = source.convert("RGB")
    width, height = source.size
    with open("black_bitmap.txt", "w", encoding="utf-8") as file_black_bitmap:
        binary_number = ""
        data_in_file = 0
        for i in range(height):
            for j in range(width):
                (r, g, b) = source.getpixel((j, i))
                if (r, g, b) == (0, 0, 0):
                    binary_number += "1"
                else:
                    binary_number += "0"
                if len(binary_number) == 8:
                    data_in_file += 1
                    hex_number = hex(int(binary_number, 2))
                    if len(hex_number) == 3:
                        hex_number = hex_number[:2] + "0" + hex_number[2] 
                    if data_in_file == (height * width / 8):
                        file_black_bitmap.write(hex_number)
                    else:
                        if data_in_file % 16 == 0:
                            file_black_bitmap.write(hex_number)
                            file_black_bitmap.write(",\n")
                        else:
                            file_black_bitmap.write(hex_number)
                            file_black_bitmap.write(", ")
                    binary_number = ""
    with open("red_bitmap.txt", "w", encoding="utf-8") as file_red_bitmap:
        binary_number = ""
        data_in_file = 0
        for i in range(height):
            for j in range(width):
                (r, g, b) = source.getpixel((j, i))
                if (r, g, b) == (255, 0, 0):
                    binary_number += "1"
                else:
                    binary_number += "0"
                if len(binary_number) == 8:
                    data_in_file += 1
                    hex_number = hex(int(binary_number, 2))
                    if len(hex_number) == 3:
                        hex_number = hex_number[:2] + "0" + hex_number[2] 
                    if data_in_file == (height * width / 8):
                        file_red_bitmap.write(hex_number)
                    else:
                        if data_in_file % 16 == 0:
                            file_red_bitmap.write(hex_number)
                            file_red_bitmap.write(",\n")
                        else:
                            file_red_bitmap.write(hex_number)
                            file_red_bitmap.write(", ")
                    binary_number = ""

wbr_colors("pampalini.jpg")
get_bitmaps("wbr_image.png")