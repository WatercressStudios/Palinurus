# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        size 18
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu Init
#
# All this does is choose between the two menus, depending on whether or
# not the player has beaten the game once.

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    if persistent.ending == "Complete":
        use main_menu_bonus
    else:
        use main_menu_normies

##############################################################################
# Gallery Main Menu
#
# This replaces the main menu once the game has detected that
# the player has completed the game.  It unlocks the art gallery.
screen main_menu_bonus():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .02
        yalign .98
        
        has vbox
        
        textbutton _("Start Game") action Start() 
        textbutton _("Load Game") action ShowMenu("load") 
        textbutton _("Bonus Scenes") action ShowMenu("bonus") 
        textbutton _("CG Gallery") action ShowMenu("cg_gallery") 
        textbutton _("Art Gallery") action ShowMenu("art_gallery") 
        textbutton _("Preferences") action ShowMenu("preferences") 
        textbutton _("Credits") action Start("credits") 
        textbutton _("Quit") action Quit(confirm=False) 
        
init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"

screen main_menu_normies():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .02
        yalign .90

        has vbox:
            spacing 5

        textbutton _("Start") action Start() text_size 40
        textbutton _("Load") action ShowMenu("load") text_size 40
        textbutton _("Bonus Scenes") action ShowMenu("bonus") text_size 40
        textbutton _("CG Gallery") action ShowMenu("cg_gallery") text_size 40
        textbutton _("Preferences") action ShowMenu("preferences") text_size 40
        textbutton _("Credits") action Start("credits") text_size 40
        textbutton _("Quit") action Quit(confirm=False) text_size 40

screen the_img(img):
    add img pos (0, 0)
    

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"


##############################################################################
# Bonus Scene Menu
#
# Couldn't have said it better myself
screen bscenes():

    # The bonus scene buttons.
    frame:
        style_group "bonus"
        xalign .98
        yalign .02

        has hbox

        textbutton _("Blue Pearl") action Start("blue_pearl") hovered ShowTransient("the_img", img="Blue_Pearl_Icon_Test_1.png") unhovered Hide("the_img")

screen bonus():
    
    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use bscenes
    

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .02
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"



##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"


init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    vbox:
        style_group "quick"

        xalign 0.9927
        yalign 1.0

        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        ypadding 6
        xpadding 5
        xalign 0.5
        ypos -4

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


##############################################################################
# CG Nav
#
# This is the menu that shows while the player is in the CG gallery

screen cgnav():

    # The background of the game menu.
    window:
        style "gm_root"
        ysize 30

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .90
        yalign .99
        
        
        has hbox
        
        textbutton _("Preferences") action ShowMenu("preferences") 
        textbutton _("Return") action Return() 

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"

##############################################################################
# Gallery
#
# This section handles the creation of all galleries at once.

init python:
    # Each gallery item should be arranged in a list and assigned to a variable.
    # The files listed here should only be the pictures seen in the gallery, NO VARIANTS
    gallery_cg_items = ["initialization", "budasmile1", "budaproud", "hours", "surprised", "hug", "blush", "budablush", "prestasisangry", "dream", "joy1", "end1"]
    gallery_art_items = ["art1", "art2", "art3", "art4", "art5", "art6", "art7", "art8", "art9", "art10", "art11", "art12", "art13", "art14", "art15",
    "art16", "art17", "art18", "art19", "art20", "art21", "art22", "art23", "art24", "art25"]
    # The number of rows and columns for all galleries.
    gal_rows = 4
    gal_cols = 3
    # The size that thumbnails should be scaled to.
    thumbnail_x = 267
    thumbnail_y = 150
    # The setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.

    # Building the interface
    gal_cells = gal_rows * gal_cols
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item) # Uncommenting this makes the picture locked until viewed in the game.
        #Code for multiple variants of the same still
        if gal_item == "initialization":
            g_cg.image("sing1")
            g_cg.unlock("sing1")
        if gal_item == "budablush":
            g_cg.image("budablush2")
            g_cg.unlock("budablush2")
            g_cg.image("budablush3")
            g_cg.unlock("budablush3")
            g_cg.image("budablush4")
            g_cg.unlock("budablush4")
            g_cg.image("budablush5")
            g_cg.unlock("budablush5")
        if gal_item == "budasmile1":
            g_cg.image("budasmile2")
            g_cg.unlock("budasmile2")
            g_cg.image("budaspeak")
            g_cg.unlock("budaspeak")
        if gal_item == "end1":
            g_cg.image("end2")
            g_cg.unlock("end2")
            g_cg.image("end3")
            g_cg.unlock("end3")
            g_cg.image("end4")
            g_cg.unlock("end4")
            g_cg.image("end5")
            g_cg.unlock("end5")
            g_cg.image("end6")
            g_cg.unlock("end6")
        if gal_item == "prestasisangry":
            g_cg.image("prestasisworried")
            g_cg.unlock("prestasisworried")
            g_cg.image("prestasisworriedspeaking")
            g_cg.unlock("prestasisworriedspeaking")
        if gal_item == "joy1":
            g_cg.image("joy2")
            g_cg.unlock("joy2")
            g_cg.image("joy3")
            g_cg.unlock("joy3")
            g_cg.image("joy4")
            g_cg.unlock("joy4")
            g_cg.image("joy5")
            g_cg.unlock("joy5")
    g_cg.transition = dissolve
    cg_page=0

    g_art = Gallery()
    for gal_item in gallery_art_items:
        g_art.button(gal_item + " butt")
        g_art.image(gal_item)
        #g_art.unlock(gal_item)
        #if BGs have variations, such as night version, uncomment the lines below and include the code for each BG with variations
        if gal_item == "art3":
            g_art.image("art3p2")
            #g_art.unlock("art3p2")
            g_art.image("art3p3")
            #g_art.unlock("art3p3")
            g_art.image("art3p4")
            #g_art.unlock("art3p4")
            g_art.image("art3p5")
            #g_art.unlock("art3p5")
            g_art.image("art3p6")
            #g_art.unlock("art3p6")
            g_art.image("art3p7")
            #g_art.unlock("art3p7")
        if gal_item == "art5":
            g_art.image("art5p2")
            #g_art.unlock("art5p2")
            g_art.image("art5p3")
            #g_art.unlock("art5p3")
        if gal_item == "art10":
            g_art.image("art10p2")
            #g_art.unlock("art10p2")
            g_art.image("art10p3")
            #g_art.unlock("art10p3")
        if gal_item == "art12":
            g_art.image("art12p2")
            #g_art.unlock("art12p2")
        if gal_item == "art14":
            g_art.image("art14p2")
            #g_art.unlock("art14p2")
            g_art.image("art14p3")
            #g_art.unlock("art14p3")
            g_art.image("art14p4")
            #g_art.unlock("art14p4")
            g_art.image("art14p5")
            #g_art.unlock("art14p5")
            g_art.image("art14p6")
            #g_art.unlock("art14p6")
        if gal_item == "art15":
            g_art.image("art15p2")
            #g_art.unlock("art15p2")
            g_art.image("art15p3")
            #g_art.unlock("art15p3")
        if gal_item == "art17":
            g_art.image("art17p2")
            #g_art.unlock("art17p2")
            g_art.image("art17p3")
            #g_art.unlock("art17p3")
            g_art.image("art17p4")
            #g_art.unlock("art17p4")
            g_art.image("art17p5")
            #g_art.unlock("art17p5")
        if gal_item == "art18":
            g_art.image("art18p2")
            #g_art.unlock("art18p2")
            g_art.image("art18p3")
            #g_art.unlock("art18p3")
            g_art.image("art18p4")
            #g_art.unlock("art18p4")
            g_art.image("art18p5")
            #g_art.unlock("art18p5")
            g_art.image("art18p6")
            #g_art.unlock("art18p6")
        if gal_item == "art19":
            g_art.image("art19p2")
            #g_art.unlock("art19p2")

    g_art.transition = dissolve
    art_page=0

init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
    for gal_item in gallery_art_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))


screen cg_gallery: # The CG screen
    tag menu
    use cgnav
    frame background None xpos 00:
        grid gal_rows gal_cols:
            xpos 50
            ypos 50
            $ i = 0
            $ next_cg_page = cg_page + 1
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("ui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
        #Code for Next Button, uncomment if there are more CGs than can fit on one page.
        #frame:
            #yalign 0.97
            #vbox:
                #if len(gallery_cg_items)>gal_cells:
                    #textbutton _("Next Page") action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_gallery")]

screen art_gallery:
    tag menu
    use cgnav
    frame background None xpos 00:
        grid gal_rows gal_cols:
            xpos 50
            ypos 50
            $ i = 0
            $ next_art_page = art_page + 1
            if next_art_page > int(len(gallery_art_items)/gal_cells):
                $ next_art_page = 0
            for gal_item in gallery_art_items:
                $ i += 1
                if i <= (art_page+1)*gal_cells and i>art_page*gal_cells:
                    add g_art.make_button(gal_item + " butt", gal_item + " butt", im.Scale("ui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (art_page+1)*gal_cells): #we need this to fully fill the grid
                null
        #Code for Next Button, uncomment if there are more CGs than can fit on one page.
        frame:
            yalign 0.97
            xpos 50
            vbox:
                if len(gallery_art_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('art_page', next_art_page), ShowMenu("art_gallery")]
