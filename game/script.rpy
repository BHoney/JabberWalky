# You can place the script of your game in this file.
init python:
    menu = nvl_menu
    style.nvl_menu_choice.font = "OpenDyslexic3-Regular.ttf"
    style.nvl_menu_choice.color = "#20191C"
    style.nvl_menu_choice.drop_shadow = [(1,1)]
    style.nvl_menu_choice.drop_shadow_color = "#333333"
    style.nvl_menu_choice.hover_color = "#243914"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define n = Character(None, kind= nvl)
# The game starts here.
label start:

   n "He took his Vorpal Sword in hand; Long Time the Manxome Foe He Sought, 'Til He Rested By The Tum-Tum Tree And Stood A while In Thought"
   n "And As In Uffish Thought He Stood, The Jabberwock With Eyes Of Flame, Came Whiffling Through The Tulgy Wood and Burbled As It Came!"
   n "Obvious exits are..."
  
menu:

        "North":
            n "Move North"
          
        "South":
            n "Move South"
        "Dennis":
            n "Who's Dennis?"

#label after_menu:



return
