# You can place the script of your game in this file.

init python:

    # Set the background of the NVL window; this image should be the
    # same size as the screen.
   # style.nvl_window.background = "nvl_window.png"

    # Add some additional padding around the contents of the NVL window.
    # This keeps the text inside the borders of our image.
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55

    # Set the spacing between each block of text on the page.
    # The default is 10 pixels.
    style.nvl_vbox.box_spacing = 10


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define n = Character(None, kind= nvl)
# The game starts here.
label start:

   n "This is a test of the nvl system."
   n "This should be on screen as a novel block as opposed to a text box."
   nvl clear

   n "Hopefully this is the first line on screen."


return
