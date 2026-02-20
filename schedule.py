from PIL import Image, ImageDraw, ImageFont  

width = 400
height = 300
image = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

header = ImageFont.truetype("Rubik-ExtraBold.ttf", size = 30)
standart_text = ImageFont.truetype("Rubik-Medium.ttf", size = 20)
italic = ImageFont.truetype("Rubik-LightItalic.ttf", size = 15)
small_text = ImageFont.truetype("Rubik-Medium.ttf", size = 15)

def following_lesson(y, time, teacher, subject_abb, students_class):
    draw.text((5, y), time, font = small_text, fill = (0, 0, 0))
    draw.text((width // 3, y), teacher, font = small_text, fill = (0, 0, 0))
    draw.text((width * 3 // 5, y), subject_abb, font = small_text, fill = (0, 0, 0))
    draw.text((width * 4 // 5, y), students_class, font = small_text, fill = (0, 0, 0))

draw.rectangle((0, 0, width, 40), fill = (255, 0, 0))
draw.text((5, 5), "6. A", font = header, fill = (255, 255, 255))

draw.text((5, 45), "aktuálně: 8:05 - 8:50", font = italic, fill = (0, 0, 0))
draw.text((5, 70), "Český jazyk a literatura", font = header, fill = (255, 0, 0))
draw.text((5, 110), "třída: 6. A", font = standart_text, fill = (0, 0, 0))
draw.text((5, 140), "učitel: Mgr. Martin Boček", font = standart_text, fill = (0, 0, 0))

draw.line(((0, 180), (width, 180)), width = 2, fill = (255, 0, 0))

draw.text((5, 200), "následující hodiny:", font = small_text, fill = (0, 0, 0))
following_lesson(225, "9:00 - 9:45", "Boček", "CL", "6. A")
following_lesson(245, "10:00 - 10:45", "Boček", "D", "6. A")
following_lesson(265, "10:55 - 11:40", "Harničárová", "A", "6. A")

image.save("schedule.png")