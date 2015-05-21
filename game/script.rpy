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

label pond:
    #ILLUSTRATION NOTE: A pond, its banks are steeply sloped and it is surrounded by trees. There are rocks visible on the side furthest away from the 'camera'. If we're going with a panorama this will be to the right of the illustration for the previous passage.

    n "Down a small slope you find a pond."
    n "On some rocks on the far side of the pond are some slithy toves."

    if beastiary[0] == False:
        n "You can..."
        menu:
            "observe from here..."
            jump observe_slithy

            "or try to get closer."
            jump closer_slithy

    else:
    n "You have already written your notes on them. From here you can go..."
    menu:
    "West, where the skies are blue."
    jump enter

label observe_slithy:
    n "The pond's banks are quite steep and you have a good view from here anyway. You successfully take your notes on slithy toves."
    beastiary[0] = True
    menu:
        "return to the crossroads"
        jump enter

label closer_slithy:
#Include a screenshake here and hopefully a splash sound if someone's kind enough to supply us with one :v
    n "The sides of the pond are treacherous! You fall in like a dingus. You are unharmed, but once you get out you have to wait a while for the toves to reappear so that you may observe them."
    is_wet = True
    beastiary[0] = True
    #Slithy Get!!

    menu:
        "Return to the crossroads"
        jump enter


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

label listen_mome:

    #SYD: Screenshake or similar here, maybe see if renpy's recolouring command works on the background to briefly make it go green or something? that might be tacky, we'll figure something out.
    #Bloody: Green flash is cooked into the ren'py documentation, so we'll get to this eventually
    #We might not need to clear here? If the text fits at the bottom we should be fine. Just call the jump after and we can progress

    n "Mome raths release spores, silly! They are harmless but now you are super itchy and it is gross."
    is_itchy = True #We need to redo this and the variables, but later
    beastiary[1] = True
    jump deep_forest

label write_mome:
    n "You uneventfully write your notes about Mome Raths."
    beastiary[1] = True
    jump deep_forest             

label west_log:
    nvl clear
    #ILLUSTRATION NOTE this is probably one of the easier ones? just a little hillock with a hole in it, surrounded by similar trees to the rotting one in the previous passage. If we're using panoramas this will be the center of the image featuring the rotting log.
   
        n "While walking deeper into the forest you almost trip over a hole in the ground! This is where a bandersnatch lives. It looks like it's still in use; earth has been disturbed recently."
        #display status

        #Bloody: Did a quick script edit here -- it seems like the above paragraph should be displayed before the check is made, otherwise you get a blank screen right here.

        if beastiary[2] == False:
        menu:
            "Inspect the hole...":
                jump inspect_hole
            "...Or move away to wait and watch from a distance":
                jump wait_hole    

        else:
            n "You have already written your notes on the bandersnatch. From here you can..."
            menu:
                "Follow the trail further west...":
                    jump west_trail
                "Or go back east.":
                    jump deep_forest


label inspect_hole:
#SCREENSHAKE, SCATCH SOUND
n "You kneel down and put your face down to the hole. Shockingly this is unwise and a bandersnatch scratches your face to buggery. You retire further away and wait for it to settle down before observing it to write your notes."
is_scratched = True
beastiary[2] = True
menu:
    "return to the log"
    jump west_log


label wait_hole:
    n "You settle in at a safe distance to write your notes."
    beastiary[2] = True
    menu:
        "return to the log"
        jump west_log

label west_trail:
    nvl clear
    #ILLUSTRATION NOTE: the player character peering at a giant pile of bones through the trees, atop which is perched a jub-jub bird
    #If we're going with panoramas this is the leftmost of the last two illustrations (so from left to right we go pile o'skulls >> bandersnatch den >> rotting log )

    if beastiary[3] == False:
        n "The trail starts west then winds northwards, the trees are becoming thick and twisted and tulgy. You smell something sickly -- carrion. Through a tiny gap in the trees you see its source; the nest of the jub-jub bird, which it builds from the bones of its prey. It is like super gross but also incredibly metal."
        #display status
    n "You can..."
    menu:
        "squeeze in a little closer to the tree line to write your notes":
            jump jub_jub_notes
        "Or you can try to push into the grisly nest istelf.":
            jump grisly_nest_DEATH_FLAG

    else:
    n "The woods are beginning to become quite thick, but there are gaps here just big enough for you to be able to see the macabre jub jub bird's nest."
    #display status
    n "You do not want to hang around any longer than you have to. You can push on..."
    menu:
        "further north"
        jump further_north

        "or go back southeast."
        jump west_log

label jub_jub_notes:
    n "You write your notes as quickly as you can- you can't stomach staying here any longer than you have to. Some of these bones look distinctly... human."
        beastiary[3] = True
    menu:
        "return to the western trail."
        jump west_trail

label grisly_nest_DEATH_FLAG:
    #SCREENSHAKE
    #RED FLASH??
    #ILLUSTRATION NOTE a big scary fuckin bird attacking the player (in silhouette, again) or just flying straight at the viewer, whichever's easiest / looks cooler.

    n "Jub-jub birds are incredibly territorial! this one fucks you right up and now you are dead"
    jump retry


label further_north:
    #Illustration note: I don't think it's too far out of scope to kinda animate this? This can be a composite image; two layers of thick trees (one on the left and one on the right) which are slid out of frame to reveal a clearing part way thru this passage. The clearing is surrounded by the thickest + spookiest trees (possible to have them almost completely silhouetted, probably?) but in the centre is a beautiful tree that literally glows. I was thinking of modelling it after a weeping willow bc those are my fav but it's up to whoever draws this. 
    nvl clear
    n "The woods become thicker and twistier as you move further north. Just as you think you will soon be able to go no further, you push through into a beautiful clearing at the centre of which is a great, bioluminescent tree. The tum-tum tree!"
    #display status
    n "Perhaps you should get some rest before you try to find the jabberwock. You could..."
    menu:
        "settle at he base of the tree"
        jump base_tree_DEATH_FLAG

        "or climb into it's branches, if you think that'd be safer."
        jump tum_branches

label base_tree_DEATH_FLAG:
    nvl clear
        n "You sit between two big, solid roots of the tum-tum tree to catch your breath. You begin to doze off but are suddenly awoken by the burbling sound of {b}THE JABBERWOCK{/b} whiffling through the tulgy wood!"

        #SCREENSHAKE

        #illustration note: similar to the jub-jub bird ending, an image of the jabberwocky either attacking the player in silhouette or lunging at the viewer.

        n "You do not stand a chance."
        n "It fucks you right up and you are dead."
        jump retry

label tum_branches:
    nvl clear
    n "You aren't sure it's safe to just sleep on the floor in a place as treacherous as this, so you climb up into the branches of the tum-tum tree to rest. You doze off..."
    #SCREENSHAKE??
    n"But suddenly you are awoken by the burbling sound of {b}THE JABBERWOCKY{/b} whiffling through the tulgy wood! From your vantage point in the tum-tum tree you can see it in all its terrifying glory as it fucks some shit up idk. You write your notes, a little shaken, but otherwise completely unharmed."
    beastiary[4] = True

    #NOTE FROM SYD: from here (and also when adding any other animal to the bestiary) there is logic I can't really be bothered to code in twine; basically if the bestiary is now completed you go to the ending, if not you are dumped back to the clearing with the tum-tum tree (but now the jabberwocky variable will be set to 'true' so that passage will be written differently.)

    #Bloody: So basically, a for loop will go here
    #Loop through beastiary and if it returns false every, jump to further_north_alt or maybe put an if statement in further_north
    #Else, we go right into the ending

    #jump good_end

label good_end        

return
