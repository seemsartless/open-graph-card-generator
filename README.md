# open-graph-card-generator
Simple Python script that uses PIL to create an image with text on it to be used as an Open Graph card.

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

Find a suitable background image, change those variables and run the script! Well, after the...

## One time setup
Nothing is quite that easy - in Step 2 I include some variables that you will also need to set up once.

Folder locations should be straight forward - no slash at the end of the path names:
- `img_folder = 'input'  # or full path like '/Users/user1/web_pages/background'`
- `out_folder = 'output'  # or full path like '/Users/user1/web_pages/og-cards'`

The other variables deal with how much blur to add to the background image (`img_blur`) and colors to use (`font_color` and `fill_color_and_transparency`) and the overlay image to use, which we will cover next.

## Overlay image
I wanted enough control over the generated images to have an image I can use as an overlay - in this example it isn't very complicated, but you could add your logo, a more colorful image, etc. The png file I included here (`card-overlay-1200x630.xcf`) was generated with The Gimp and has a transparent background. It looks like the following:
![Simple overlay image](input/card-overlay-1200x630.png)

You can create your own image, again with lots of transparent empty sections, for your own use.

## Rest of the code
Once we have everything set up the rest of the code is pretty straightforward PIL code.
