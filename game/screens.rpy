#############################################
# /Rokhimin Wahid
# /17 Desember 2016
#############################################

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

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

screen choice:

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

screen input:

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

screen nvl:

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
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    tag menu 
    add  "mains" 

#Notice
    imagebutton auto "img/tb_warn_%s.png" xpos 1 ypos 1 focus_mask True action [Hide("gui_tooltip"),] hovered [ ] unhovered [Hide("gui_tooltip")] 
    

#MainMenu    
    imagebutton auto "img/tb_mulai_%s.png" xpos 5 ypos 110 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu('lang') ] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_start.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")] at main_eff6
    imagebutton auto "img/tb_lanjutkan_%s.png" xpos 5 ypos 200 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu('load' )] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_load.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")] at main_eff6
    imagebutton auto "img/tb_pengaturan_%s.png" xpos 5 ypos 290 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu('preferences')] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_config.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")] at main_eff6
    imagebutton auto "img/tb_tentang_%s.png" xpos 5 ypos 380 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("tentang")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_about.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")] at main_eff6
    imagebutton auto "img/tb_keluar_%s.png" xpos 5 ypos 470 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),Quit(confirm=True)] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_quit.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")] at main_eff6
    

#EasterEgg
    imagebutton auto "img/tb_sys_%s.png" xpos 920 ypos 213 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_sys.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/tb_pr_%s.png" xpos 382 ypos 213 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("prolog")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_pr.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/tb_ep_%s.png" xpos 408 ypos 293 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("epilog")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_ep.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/tb_ex_%s.png" xpos 720 ypos 273 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("extra")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_ex.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/tb_qu_%s.png" xpos 620 ypos 273 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_qu.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/tb_yad_%s.png" xpos 1048 ypos 203 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_yad.png", my_tt_xpos=400, my_tt_ypos=410) ] unhovered [Hide("gui_tooltip")]
                    

#SocialMedia    
    imagebutton auto "img/ico_t_%s.png" xpos 67 ypos 650 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),open_web] hovered [ ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/ico_fb_%s.png" xpos 7 ypos 650 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),open_fb] hovered [ ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/ico_ig_%s.png" xpos 127 ypos 650 focus_mask True action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),open_ig] hovered [ ] unhovered [Hide("gui_tooltip")]
   


    
init python :

    def open_web() :
        import webbrowser
        
        webbrowser.open_new('http://www.twitter.com/s3_rl')
    
    def open_fb() :
        import webbrowser
        
        webbrowser.open_new('http://www.facebook.com/whdeveloper')

    def open_ig() :
        import webbrowser
        
        webbrowser.open_new('http://www.instagram.com/mr.whd')


    
##############################################################################
#gambar tooltip

screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    
##############################################################################


screen lang :
    
    tag menu
    add "language_menu" 
    imagebutton auto "img/aind_%s.png" xpos 480 ypos 260 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),Start()] hovered [ ] unhovered [Hide("gui_tooltip")] at main_eff2
    imagebutton auto "img/aeng_%s.png" xpos 480 ypos 340 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),] hovered [ ] unhovered [Hide("gui_tooltip")] at main_eff2
    imagebutton auto "img/ajpn_%s.png" xpos 480 ypos 420 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),] hovered [ ] unhovered [Hide("gui_tooltip")] at main_eff2
    
    imagebutton auto "img/tb_kembali_%s.png" xpos -25 ypos 620 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("main_menu")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_kembali.png", my_tt_xpos=400, my_tt_ypos=660) ] unhovered [Hide("gui_tooltip")] at main_eff2
    



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # This ensures that any other menu screen is replaced.
    tag menu
    
    imagebutton auto "img/tb_kembali_%s.png" xpos -25 ypos 620 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),Return()] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_kembali.png", my_tt_xpos=400, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")] at main_eff2


##############################################################################
# Save, Load
#

screen file_picker :
    
    default current_file = 0
    if current_file != 0:
        add FileScreenshot(current_file) xalign 0.258 yalign 0.05

    frame:
        area (737, 5, 500, 655)
        style "file_picker_frame"
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            has vbox
            $ rows = 5
            for i in range(1, rows + 1):

              if delete == True :
                    button:
                            action FileDelete(i)
                            hovered SetScreenVariable("current_file", i)
                            unhovered SetScreenVariable("current_file", 0)
                            xfill True
                            has hbox
                            $ file_name = FileSlotName(i, rows)
                            $ file_time = FileTime(i, empty=_("{b}- {color=#00FF00}{vspace=3}{space=120}File Kosong{/b}{/color}"))
                            text "{color=#ffffff} ------------------------------------------{/color}{vspace=3}   File no : [file_name]{vspace=3}{space=75}Tanggal [file_time!t]{vspace=3}"

              else :
                    button:
                            action FileAction(i)
                            hovered SetScreenVariable("current_file", i)
                            unhovered SetScreenVariable("current_file", 0)
                            xfill True
                            has hbox
                            $ file_name = FileSlotName(i, rows)
                            $ file_time = FileTime(i, empty=_("{b}- {color=#00FF00}{vspace=3}{space=120}File Kosong{/b}{/color}"))
                            text "{color=#ffffff} ------------------------------------------{/color}{vspace=3}   File no : [file_name]{vspace=3}{space=75}Tanggal [file_time!t]{vspace=3}"
                            key "save_delete" action FileDelete(i)


    
screen save:
    tag menu
    add "simpan"
    $ delete = False
    use navigationsave
    use file_picker

screen load:
    tag menu
    add "lanjutkan"
    $ delete = False
    use navigationsave
    use file_picker

screen delete:
    tag menu
    add "hapus"
    $ delete = True
    use navigationsave
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

screen navigationsave:
    #tag menu
    imagebutton auto "img/tb_menu_manual_%s.png" xpos 100 ypos 220 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),FilePage(1)] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_manual.png", my_tt_xpos=-50, my_tt_ypos=670) ] unhovered [Hide("gui_tooltip")] at main_eff2
    imagebutton auto "img/tb_otomatis_%s.png" xpos 100 ypos 290 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),FilePage("auto")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_otomatis.png", my_tt_xpos=-50, my_tt_ypos=670) ] unhovered [Hide("gui_tooltip")] at main_eff2
    imagebutton auto "img/tb_kembali_%s.png" xpos -25 ypos 620 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),Return()] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_kembali.png", my_tt_xpos=-50, my_tt_ypos=670) ] unhovered [Hide("gui_tooltip")] at main_eff2
    imagebutton auto "img/tb_simpan_%s.png" xpos 100 ypos 360 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("save")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_simpan.png", my_tt_xpos=-50, my_tt_ypos=670) ] unhovered [Hide("gui_tooltip")] at main_eff2
    imagebutton auto "img/tb_lanjutkan_%s.png" xpos 100 ypos 150 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("load")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_load.png", my_tt_xpos=-50, my_tt_ypos=670) ] unhovered [Hide("gui_tooltip")] at main_eff2
    imagebutton auto "img/tb_hapus_%s.png" xpos 100 ypos 430 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("delete")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_hapus.png", my_tt_xpos=-50, my_tt_ypos=670) ] unhovered [Hide("gui_tooltip")] at main_eff2
   

    frame:
        xalign .98
        yalign .99
        has hbox
        textbutton ("{size=+14}◄{/size}"):
              action FilePagePrevious()

        for i in range(1, 10):
              textbutton ("{size=+14}[i]{/size}"):
                    action FilePage(i)

        textbutton ("{size=+14}►{/size}"):
              action FilePageNext()

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:
    tag menu
    add "pengaturan"
    use navigation
    # Display windowed/full screen:
    #imagebutton auto "gambar/fullno_%s.png" xpos 390 ypos 215 focus_mask True action void() at config_eff2 hovered [ Show("gui_tooltip", my_picture="gambar/config_window.png", my_tt_xpos=46, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    #imagebutton auto "gambar/full_%s.png" xpos 530 ypos 215 focus_mask True action void() at config_eff2 hovered [ Show("gui_tooltip", my_picture="gambar/config_fullscr.png", my_tt_xpos=46, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    
    imagebutton auto "img/p/fullno_%s.png" xpos 290 ypos 100 focus_mask True action [Play ("test_one", "snd/click.wav"),Preference('display', 'window')]  at config_eff2 hovered [ Show("gui_tooltip", my_picture="img/p/config_window.png", my_tt_xpos=300, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/p/full_%s.png" xpos 350 ypos 100 focus_mask True action [Play ("test_one", "snd/click.wav"),Preference('display', 'fullscreen')] at config_eff2 hovered [ Show("gui_tooltip", my_picture="img/p/config_fullscr.png", my_tt_xpos=300, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    
    # Transitions on/off:
    imagebutton auto "img/p/transno_%s.png" xpos 278 ypos 284 focus_mask True action [Play ("test_one", "snd/click.wav"),Preference('transitions', 'none')] at config_eff2 hovered [ Show("gui_tooltip", my_picture="img/p/trans_off.png", my_tt_xpos=300, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/p/trans_%s.png" xpos 350 ypos 284 focus_mask True action [Play ("test_one", "snd/click.wav"),Preference('transitions', 'all')] at config_eff2 hovered [ Show("gui_tooltip", my_picture="img/p/trans_on.png", my_tt_xpos=300, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    # Stop/continue skipping after choices
    imagebutton auto "img/p/skipstop_%s.png" xpos 550 ypos 100 focus_mask True action [Play ("test_one", "snd/click.wav"),Preference('after choices', 'stop')] at config_eff2 hovered [ Show("gui_tooltip", my_picture="img/p/stopskip.png", my_tt_xpos=300, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/p/skipkeep_%s.png" xpos 635 ypos 100 focus_mask True action [Play ("test_one", "snd/click.wav"),Preference('after choices', 'skip')] at config_eff2 hovered [ Show("gui_tooltip", my_picture="img/p/skipkeep.png", my_tt_xpos=300, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    # Skip all/seen text
    imagebutton auto "img/p/skipread_%s.png" xpos 840 ypos 100 focus_mask True action [Play ("test_one", "snd/click.wav"),Preference('skip', 'seen')] at config_eff2 hovered [ Show("gui_tooltip", my_picture="img/p/skipread.png", my_tt_xpos=300, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "img/p/skipall_%s.png" xpos 910 ypos 100 focus_mask True action [Play ("test_one", "snd/click.wav"),Preference('skip', 'all')] at config_eff2 hovered [ Show("gui_tooltip", my_picture="img/p/skipall.png", my_tt_xpos=300, my_tt_ypos=600) ] unhovered [Hide("gui_tooltip")]
   
    frame xpos 600 ypos 280:
        style_group "pref"
        has vbox
        label "Volume Musik" 
        bar value Preference("music volume")
    frame xpos 600 ypos 350:
        style_group "pref"
        has vbox
        label "Volume Suara" 
        bar value Preference("sound volume")
    frame xpos 600 ypos 420:
        style_group "pref"
        has vbox
        label "Kecepatan Teks"
        bar value Preference("text speed")
        
init -2 python: 
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "img/p/config_bar_full.png"
    style.pref_slider.right_bar = "img/p/config_bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 223
    style.pref_slider.ymaximum = 36    

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 0.5

    style pref_slider:
        xmaximum 225
        xalign 0.0

    style soundtest_button:
        xalign 0.0

##############################################################################
# Prolog
#
#

screen prolog:

        tag menu
        add "about"
        frame :
            area (460, 10, 1000, 650)
            viewport  :
              draggable True
              scrollbars "vertical"
              mousewheel True
              frame:
                has vbox
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("Sorry Prolog not available")

        imagebutton auto "img/tb_kembali_%s.png" xpos -25 ypos 620 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("main_menu")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_kembali.png", my_tt_xpos=400, my_tt_ypos=660) ] unhovered [Hide("gui_tooltip")] at main_eff2
    
##############################################################################
# Epilog
#
#

screen epilog:

        tag menu
        add "about"
        frame :
            area (460, 10, 1000, 650)
            viewport  :
              draggable True
              scrollbars "vertical"
              mousewheel True
              frame:
                has vbox
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("Sorry Epilog not available")

        imagebutton auto "img/tb_kembali_%s.png" xpos -25 ypos 620 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("main_menu")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_kembali.png", my_tt_xpos=400, my_tt_ypos=660) ] unhovered [Hide("gui_tooltip")] at main_eff2
    
##############################################################################
# Extra
#
#

screen extra:

        tag menu
        add "about"
        frame :
            area (460, 10, 1000, 650)
            viewport  :
              draggable True
              scrollbars "vertical"
              mousewheel True
              frame:
                has vbox
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("")
                label _("Sorry Extra not available")

        imagebutton auto "img/tb_kembali_%s.png" xpos -25 ypos 620 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("main_menu")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_kembali.png", my_tt_xpos=400, my_tt_ypos=660) ] unhovered [Hide("gui_tooltip")] at main_eff2
    

##############################################################################
# Tentang
#
# Screen yang memunculkan About.

screen tentang:

        tag menu
        add "about"
        frame :
            area (160, 10, 1000, 650)
            viewport  :
              draggable True
              scrollbars "vertical"
              mousewheel True
              frame:
                has vbox
                label _("Visual Novel Buried") xalign 0.5
                label _("v 1.1") xalign 0.5
                label _("________________________________________________________________________________") xalign 0.5
                label _("")
                label _("Written         : Rokhimin Wahid")
                label _("Programmer : Rokhimin Wahid")
                label _("Design          : Rokhimin Wahid")
                label _("Create          : 18 Desember 2016")
                label _("Thanks To     :")
                label _("                       -Renpy (Engine with Python Language)")
                label _("                       -Sublime (Text Editor)")
                label _("                       -GIMP2 (Alternative Photoshop)")
                label _("                       -ApacheAnt ,JDK ,SDK ,Google")
                label _("Image          : All image ,icon ,background ,etc edited by software GIMP2")
                label _("Sound          : All Sound free license from internet")
                label _("")
                label _("License Game")
                label _("________________")
                label _("© 2016, Whdeveloper")
                label _("Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions aremet: Redistributions of source code must retain the above copyright")

        imagebutton auto "img/tb_kembali_%s.png" xpos -25 ypos 620 focus_mask True  action [Hide("gui_tooltip"),Play ("test_one", "snd/click.wav"),ShowMenu("main_menu")] hovered [ Show("gui_tooltip", my_picture="img/tooltip_main_menu_kembali.png", my_tt_xpos=400, my_tt_ypos=660) ] unhovered [Hide("gui_tooltip")] at main_eff2
    
##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    # Right-click and escape answer "no".
    key "game_menu" action no_action

    on "show" action Play("sound", "snd/click.wav")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.
    add "transparan2"
    add "yesno"
    imagebutton auto "img/tb_ya_%s.png" xpos 370 ypos 450 action yes_action hover_sound "snd/click.wav" at main_eff2
    imagebutton auto "img/tb_tidak_%s.png" xpos 670 ypos 450 action no_action hover_sound "snd/click.wav" at main_eff2
    
    if message == layout.ARE_YOU_SURE:
        add "img/yesno_are_you_sure.png"
    elif message == layout.DELETE_SAVE:
        add "img/yesno_delete_save.png"
    elif message == layout.OVERWRITE_SAVE:
        add "img/yesno_overwrite_save.png"
    elif message == layout.LOADING:
        add "img/yesno_loading.png"
    elif message == layout.QUIT:
        add "img/yesno_quit.png"
    elif message == layout.MAIN_MENU:
        add "img/yesno_main_menu.png"



##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.95
        yalign 1.0

        textbutton _("Back",) action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Setting") action ShowMenu('preferences')
        textbutton _("MainMenu") action MainMenu()

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 21
        idle_color "#000000"
        hover_color "#ff0000"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"