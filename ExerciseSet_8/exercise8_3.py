from PIL import Image, ImageDraw

# create a picture that has the size of 500 x 300 and has purple
# as the background color
img = Image.new('RGB', (500, 300), color=(148, 0, 211))

# Ask the user for some text
text = input("Give some text\n")

# draw the text into the lower left corner in orange color
d = ImageDraw.Draw(img)
d.text((40, 230), text, fill="orange")

# Draw also a white triangle that contains a blue circle inside it
draw = ImageDraw.Draw(img)
draw.polygon([(200, 100), (400, 100), (300, 250)], fill="white")
draw2 = ImageDraw.Draw(img)
draw2.ellipse((250, 100, 350, 200), fill='blue', outline='blue')

img.save('pil_text.png')
