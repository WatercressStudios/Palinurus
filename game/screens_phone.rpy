##############################################################################
# These screens are for "android".

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    if persistent.ending == "Complete":
        use main_menu_bonus
    else:
        use main_menu_normies

screen main_menu_normies():

    # This ensures that any other menu screen is replaced.
    tag menu
    variant "android"

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .90

        has hbox
        
        textbutton _("Start") action Start() 
        textbutton _("Load") action ShowMenu("load") 
        textbutton _("Bonus Scenes") action ShowMenu("bonus") 
        textbutton _("CG Gallery") action ShowMenu("cg_gallery") 
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Credits") action Start("credits") 
        textbutton _("Quit") action Quit(confirm=False)

screen main_menu_bonus():
# This ensures that any other menu screen is replaced.
    tag menu
    variant "android"

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has hbox
        
        textbutton _("Start Game") action Start() 
        textbutton _("Load Game") action ShowMenu("load") 
        textbutton _("Bonus Scenes") action ShowMenu("bonus") 
        textbutton _("CG Gallery") action ShowMenu("cg_gallery") 
        textbutton _("Art Gallery") action ShowMenu("art_gallery") 
        textbutton _("Preferences") action ShowMenu("preferences") 
        textbutton _("Credits") action Start("credits") 
        textbutton _("Quit") action Quit(confirm=False) 


init -2:
    style mm_button:
        variant "android"
        yminimum 100

##############################################################################
# Navigation
#
screen navigation:
    
    tag menu
    variant "android"

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .5
        yalign .5
        xminimum .9
        yminimum .9

        has vbox

        hbox:
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
        hbox:
            textbutton _("Auto") action [Preference("auto-forward", "toggle"), Return()]
            textbutton _("Skip") action Skip()
            textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        hbox:
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Main Menu") action MainMenu()
            textbutton _("Return") action Return()
            textbutton _("Quit") action Quit()

init -1:

    style gm_nav_vbox:
        variant "android"
        spacing 60
    style gm_nav_hbox:
        variant "android"
        spacing 10
        xalign .5
    style gm_nav_button:
        variant "android"
        xminimum int(( config.screen_width / 4 ) - 20)
        yminimum int(( config.screen_height / 3 ) - 60)
    style gm_nav_button_text:
        variant "android"
        size 25
    # If "android", a "menu" button opens the "navigation" screen.
    if renpy.variant("android"):
        $ _game_menu_screen = "navigation"

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

    variant "android"
    key "game_menu" action Return()

    # The background of the game menu.
    window:
        style "gm_root"

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav1"
            xfill True
            # xalign .5

            textbutton _("Auto"):
                action FilePage("auto")
                xsize .5
                ysize .5
               
            textbutton _("Return"): 
                action Return()
                xsize .6
                ysize .5
                xalign .5
               

            textbutton _("Quick"):
                action FilePage("quick")
                xsize .7
                ysize .5
                xalign 1.0                
      
        # hbox:
        #     style_group "file_picker_nav2"
        #     xfill True
        #     xalign .5

        #     for i in range(1, 9):
        #         textbutton str(i):
        #             action FilePage(i)

        $ columns = 2
        $ rows = 4

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            yfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True
                    yfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)

screen save:

    # This ensures that any other menu screen is replaced.
    tag menu
    variant "android"

    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu
    variant "android"

    use file_picker

init -1:
    style file_picker_nav1_button:
        variant "android"
        xsize int(( config.screen_width / 4 ) - 5)
    style file_picker_nav2_button:
        variant "android"
        xsize int(config.screen_width / 8 - 5)

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preference_page:

    variant "pc" 
    key "game_menu" action Return()

    # The background of the game menu.
    window:
        style "gm_root"
    frame:
        style_group "pref_page"

        vbox:
            textbutton _("Display") action ShowMenu("preferences")
            textbutton _("Skip") action ShowMenu("preference2")
            textbutton _("Sound") action ShowMenu("preference3")




screen preference_page:

    variant "android" 
    key "game_menu" action Return()

    # The background of the game menu.
    window:
        style "gm_root"
    frame:
        style_group "pref_page"

        vbox:
            textbutton _("Display") action ShowMenu("preferences")
            textbutton _("Skip") action ShowMenu("preference2")
            textbutton _("Sound") action ShowMenu("preference3")
            textbutton _("Return") action Return()

screen preferences:

    variant "android"
    tag menu
    use preference_page

    vbox:
        style_group "prefs"
        xfill True

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

            label _("Auto-Forward Time")
            bar value Preference("auto-forward time")

            if config.has_voice:
                textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

screen preference2:

    tag menu
    variant "android"

    use preference_page

    vbox:
        style_group "prefs"
        xfill True

        frame:
            style_group "pref"
            has vbox

            label _("Skip")
            textbutton _("Seen Messages") action Preference("skip", "seen")
            textbutton _("All Messages") action Preference("skip", "all")

        frame:
            style_group "pref"
            has vbox

            label _("After Choices")
            textbutton _("Stop Skipping") action Preference("after choices", "stop")
            textbutton _("Keep Skipping") action Preference("after choices", "skip")

screen preference3:

    tag menu
    variant "android"

    use preference_page

    vbox:
        style_group "prefs"
        xfill True

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



init -1:
    style pref_button_text:
        variant "android"
        size 30
    style pref_button:
        variant "android"
        xminimum 300
        yminimum 100
    style pref_label_text:
        variant "android"
        size 30
    style pref_frame:
        variant "android"
        xsize int(config.screen_width - 350)
    style pref_page_frame:
        variant "android"
        xalign .98
        yalign .98
        xmaximum 340
    style pref_page_button:
        variant "android"
        xminimum 300
        yminimum 100
    style pref_slider:
        variant "android"
        xsize 350
    style pref_page_button_text:
        variant "android"
        size 30
##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True
    variant "android"

    # The background of the game menu.
    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        xalign .5
        yanchor 0
        ypadding .05
        xsize .99
        ysize .8

        label _(message):
            xalign 0.1
            yalign 0.1

        hbox:
            xalign 0.78
            yalign 0.68

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -1:
    style yesno_label_text:
        variant "android"
        size 30
    style yesno_button:
        variant "android"
        xminimum 300
        yminimum 100
    style yesno_button_text:
        variant "android"
        size 30

screen quick_menu():
    variant "android"

    # Add an in-game quick menu.
    vbox:
        style_group "quick"

        xalign 0.984
        yalign 1.0

        textbutton _("M") action ShowMenu('navigation') text_size 30
        textbutton _("E") action ShowMenu('navigation') text_size 30
        textbutton _("N") action ShowMenu('navigation') text_size 30
        textbutton _("U") action ShowMenu('navigation') text_size 30

init -2:
    style quick_button:
        is default
        background None
        ypadding 3
        xpadding 5
        xalign 0.5
        ypos -4

    style quick_button_text:
        is default
        size 12
        color "#ffffff"
        bold True
