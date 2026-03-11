from PIL import Image

def get_binary_files(source_image):
    source = Image.open(source_image)
    source = source.convert("RGB")
    width, height = source.size
    pixel_data = []
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
                pixel_data.append(int(hex_number, 16))
                binary_number = ""
    binary_data = bytes(pixel_data)
    with open("black_binary.bin", "wb") as file_black_binary:
        file_black_binary.write(binary_data)
    pixel_data = []
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
                pixel_data.append(int(hex_number, 16))
                binary_number = ""
    binary_data = bytes(pixel_data)
    with open("red_binary.bin", "wb") as file_red_binary:
        file_red_binary.write(binary_data)