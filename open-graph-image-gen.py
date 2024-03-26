from PIL import Image
from PIL import ImageFilter
from PIL import ImageFont
from PIL import ImageDraw
import PIL

#
# Generate an image for Open Graph cards with three lines of text
#
# Simple Python script by David Sky - david.s.toronto@gmail.com
#

#
# Step 1: Variables to change each time you create a new image
#
background_file_name = 'wholemap-cherry-blossom.jpg'

text_1 = "Wholemap Toronto blog"
text_2 = "Mount Pleasant cemetery"
text_3 = "Cherry Blossoms"

out_file_name = 'card-cherry-blossoms.jpg'

#
# Step 2: One-time setup
#
img_folder = 'input'  # or full path like '/Users/user1/web_pages/background'
out_folder = 'output'  # or full path like '/Users/user1/web_pages/og-cards'

# Will create an image using the dimensions as suggested by Meta Card og:image documentation
img_out_width = 1200
img_out_height = 630

img_blur = 3  # Will blur the background image

font_color = (11, 136, 18)  # A dark green color
fill_color_and_transparency = (217, 254, 215, 140)  # Similar to my image overlay, with transparency though
img_overlay = Image.open(f"{img_folder}/card-overlay-1200x630.png")

#
# Step 3: More variables you may want to change
#
# Define the fonts to use - you will likely need to change this for your local TrueType font installation
font_large = ImageFont.truetype("Supplemental/DIN Condensed Bold.ttf", 90)
font_medium = ImageFont.truetype("Supplemental/DIN Condensed Bold.ttf", 80)

background_full_file_name = f"{img_folder}/{background_file_name}"
output_full_file_name = f"{out_folder}/{out_file_name}"

# Should do more error checking, but at least make sure we aren't
# going to overwrite the input background image with the new image we create!
if background_full_file_name == output_full_file_name:
    print(f"Error: do not overwrite the original background image with the new image:\n\t{background_full_file_name}")
    print("\nChange the value for the variable out_file_name or use a different output folder and re-run.")
    exit(-10)

print(f"Open the background image to use:\n\tFile: {background_full_file_name}")
img = Image.open(background_full_file_name)  # Open the background image

i_width = img.width
i_height = img.height
i_ratio = i_height / i_width
print(f"\tSize:  {i_width} by {i_height} for a ratio of {i_ratio}")
print(f"\tMode: Original image mode: {img.mode}")
if img.mode == 'L':  # Greyscale image that we will need to convert
    img = img.convert(mode="RGB")
    print("\t\tConverted to {img.mode}")

# Scale the background image - want an image of img_out_width x img_out_height
multiplier_w = img_out_width / i_width
multiplier_h = img_out_height / i_height
multiplier_max_val = max(multiplier_h, multiplier_w)

print(f"Multiplier to use: w={multiplier_w} h={multiplier_h} so scale by the max = {multiplier_max_val}")
img = img.resize((int(multiplier_max_val * i_width), int(multiplier_max_val * i_height)), PIL.Image.NEAREST)
# Likely bigger in one dimension than we need, so crop from the top left
# Could change the 0,0 if you wanted to be more sophisticated, taking the center of the image, say
img = img.crop((0, 0, img_out_width, img_out_height))
img = img.filter(ImageFilter.GaussianBlur(radius=img_blur))

# Now add the simple image we're using to add a border
img.paste(img_overlay, (0, 0), mask=img_overlay)

# Create a ImageDraw.Draw() object to add text and graphic elements to the image
draw = ImageDraw.Draw(img, "RGBA")

# Fill in the center space to make the text easier to read (sorry the size is hard-coded)
draw.rectangle((90,90,  1110,540), fill=fill_color_and_transparency)

# Calculate the width of the text so we can center it
text_1_start_location = int((img_out_width - font_large.getlength(text_1)) / 2)
text_2_start_location = int((img_out_width - font_medium.getlength(text_2)) / 2)
text_3_start_location = int((img_out_width - font_medium.getlength(text_3)) / 2)

# And draw the text (sorry the top values are hard-coded - 140, 300, 420 look good to me)
draw.text((text_1_start_location, 140), text_1, font_color, font=font_large)
draw.text((text_2_start_location, 300), text_2, font_color, font=font_medium)
draw.text((text_3_start_location, 420), text_3, font_color, font=font_medium)

# And a rectangle between the larger top text and the two lines of medium text
draw.rectangle((200, 250, img_out_width - 200, 258), fill=font_color, outline=font_color)

print(f"\nNew image {img.width} x {img.height} ready to save to:\n\t{output_full_file_name}")
img.save(output_full_file_name)
img.show()  # Show the image after it is generated, too

# Done