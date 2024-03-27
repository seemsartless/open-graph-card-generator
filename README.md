# open-graph-card-generator
Simple Python script that uses PIL to create an image with text on it to be used as an Open Graph card.
  * [Our goal](#our-goal)
  * [One time setup](#one-time-setup)
  * [Overlay image](#overlay-image)
  * [Specific Pillow / PIL code](#specific-python-code)

## Our goal
I was looking for a fast, consistent way of generating Open Graph 'cards' for my Wordpress content. Nothing I found
online was quite what I was looking for, so decided to write my own in Python. Here is an example output file I created with this script:
![Sample image we are generating](output/card-cherry-blossoms.jpg)

Once the script is set up, I can change five variables in Step 1. to quickly generate a set of consistent looking 'cards':
- Three lines of text - in this example:
  - `text_1 = "Wholemap Toronto blog"`
  - `text_2 = "Mount Pleasant cemetery"`
  - `text_3 = "Cherry Blossoms"`
- Image to use as the background -  I use a different image for each blog post:
  - `background_file_name = 'wholemap-cherry-blossom.jpg'`
- Filename for the new image we're creating:
  - `out_file_name = 'card-cherry-blossoms.jpg'`

Find a suitable background image, change those variables and run the script and you're done! Well, after the...

## One time setup
Nothing is quite that easy - in Step 2 I include some variables that you will also need to set up before running the script for the first time.

Folder locations should be straight forward - no slash at the end of the path names:
- `img_folder = 'input'  # or full path like '/Users/user1/web_pages/background'`
- `out_folder = 'output'  # or full path like '/Users/user1/web_pages/og-cards'`

The other variables deal with how much blur to add to the background image (`img_blur`) and colors to use (`font_color` and `fill_color_and_transparency`) and the overlay image to use, which we will cover next.

## Overlay image
I wanted enough control over the generated images to have an image I can use as an overlay - in this example it isn't very complicated, but you could add your logo, a more colorful image, etc. The png file I included here (`card-overlay-1200x630.xcf`) was generated with The Gimp (see https://www.gimp.org/ ) and has a transparent background. It looks like the following:
![Simple overlay image](input/card-overlay-1200x630.png)

You can create your own image, again with lots of transparent empty sections so that the background image is visible in places, for your own use.

## Specific Python code
Once we have everything set up the Pillow PIL Python code is pretty straightforward.
We define the image we are working on with a `img = Image.open()` call to the Image Module

Once we have the `img` object we use the following attributes:
- `img.width` - number of pixels wide the image is
- `img.height` - number of pixels tall the image is
- `img.mode` - pixel format used by the image - we're assuming 'RGB' and use img.convert() if the image started out in greyscale (mode = "L")

And we call the following functions:
- `img.convert(mode="RGB")` - used to convert a greyscale image to RBG if necessary
- `img.resize()` - resize the image background image to the size we want
- `img.crop()` - crop the resized image if it wasn't originally the same aspect ratio that we want
- `img.filter()` - apply the `img_blur` amount of blur to the background image so that it isn't too distracting
- `img.paste()` - paste the foreground that we created on top of the background image
- `img.save()` - save the new image we created to disk
- `img.show()` - we also show the image once it is created, which is useful when you are getting things set up

I mentioned the 'foreground' that we pasted - that is the last element here - we created a 'draw' object with `draw = ImageDraw.Draw(img, "RGBA")` that we add various graphic elements to, with the following calls:
- `draw.rectangle()` the centre rectangle that makes the text easier to read over the blurred background image, and the center green line
- `draw.text()` to write the three lines of text

That's it! Clearly there should be more error checking, all of this could be made into a more flexible Python object, and so on. But the intent was a quick and easy to understand script. You can see the documentation for these attributes and functions at https://pillow.readthedocs.io/en/stable/reference/index.html
