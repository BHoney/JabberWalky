# You can place the script of your game in this file.
init python:
    menu = nvl_menu
    style.nvl_menu_choice.font = "OpenDyslexic3-Regular.ttf"
    style.nvl_menu_choice.color = "#20191C"
    style.nvl_menu_choice.drop_shadow = [(1,1)]
    style.nvl_menu_choice.drop_shadow_color = "#333333"
    style.nvl_menu_choice.hover_color = "#243914"
    style.nvl_menu_choice.size = 13
   # style.nvl_menu_choice.xalign

    #Beastiary array goes here
    beastiary = [False, False, False, False, False]
    #In Order: Slithy, Mome, Bander, Jub, Jabber
    is_wet = False
    is_itchy = False
    is_scratched = False

    #Need to create a function to print the player's status as they progress. Basically something to call every label with "if is_wet" or whatever.


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define n = Character(None, kind= nvl)
# The game starts here.
label start:

    ##Write all the areas in labels, so we can just point there when an option is selected
    #ILLUSTRATION NOTE: player character at mouth of a forest, maybe a low angle to look dramatic / make the forest seem imposing? we do not actually see the character clearly ever. Here they are shown from behind, mostly in silhouette. I imagine them as being pretty stocky but that's up to whoever ends up drawing this, really? they are carrying a pack or something with them but nothing super huge, no weapons

    n "You stand at the enterance of a forest."
    #Here's where Syd's waffle about the book comes in
    n "You Enter..."
    nvl clear
    jump enter

label enter:    
    #ILLUSTRATION NOTE: this might be where we use a panorama if we end up going with that; this is the right side of the panorama, showing... a crossroads. The trees here are a little twisty but not particularly dense; we're on the outskirts of the forest. 

    n "You travel a short while into the forest until you come to a crossroads"

    #status function here   

    n "From here, you can continue"
    menu:
        "North, deeper into the forest.":
            jump deep_forest

        "East, where you can see a pond.":
            jump pond

label deep_forest:
    #nvl clear at the start of every label
    nvl clear
    #ILLUSTRATION NOTE the trees here are starting to get denser and more rude and fucked up looking but still not like at their MOST rude and fucked up looking. Here there is one tree fallen over, covered in mushrooms and moss and whatnot. Again if we're using panoramas this will be the right side of one.

    if beastiary[1]== False:
        n "You follow a winding path deeper into the forest. There is a damp smell; a tree has fallen into the clearing and is rotting. You can see mome raths, small fungal creatures, in some of the hollows of the dead tree."
        #display status
        n "It sounds as if the mome raths are singing faintly. You can..."

        menu:
            "Move closer to listen or...":
                jump listen_mome

            "Write your dang notes.":
                jump write_mome

    else:
        n "You've already written your notes on the mome raths. From here you can go..."
    menu:
        "...South...":
            jump enter
        "...or follow the trail west":
            jump west_log    
return
