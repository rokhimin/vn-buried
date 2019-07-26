#############################################
# /Rokhimin Wahid
# /17 Desember 2016
#############################################

##############################################################################
# Mendeklarasikan data Gambar atau animasi.
##############################################################################

#Definisi Transisi tambahan
define trans = Dissolve(0.5)
define transdis = Dissolve(1.0)
define transdisl = Dissolve(2.0)
define circleirisout = ImageDissolve("img/t/id_circleiris.png", 1.0, 8)
define circleirisin = ImageDissolve("img/t/id_circleiris.png", 1.0, 8, reverse=True)
define circlewipe = ImageDissolve("img/t/id_circlewipe.png", 1.0, 8)
define teleport = ImageDissolve("img/t/id_teleport.png", 1.0, 0)
image bg circleiris = "img/t/id_circleiris.png"
image bg teleport = "img/t/id_teleport.png"
##############################################################################    
init  -10 :


#splashscreen
    image splash = "img/splashscreen.jpg"

#Gambar Tampilan Menu
    image about ="img/about.jpg"
    image language_menu ="img/lang_menu.jpg"
    image pengaturan ="img/pengaturan.png"
    image mains ="img/main.jpg"
    image yesno = "img/yesno_ground.png"
    image hapus = "img/bghapus.jpg"
    image simpan = "img/bgsimpan.jpg"
    image lanjutkan = "img/bglanjutkan.jpg"
    image transparan = "img/transparan.png"
    image transparan2 = "img/transparan2.png"
    
#Gambar saat main game
    image bg black ="img/black.jpg"
    image bg satu = "bg/1.jpg"
    image bg korek = "bg/korek.jpg"
##############################################################################
# ANIMASI
##############################################################################

init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 1.8
        easein 2.4 zoom 1.8
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
    transform main_eff6:
        zoom 1.7
        easein 2.4 zoom 1.8

    transform config_eff:
        on idle:
            easein 0.4 rotate 5
            easein 0.4 rotate -5
            repeat
        on selected_idle:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat
        on hover:
            easein 0.2 rotate 5
            easein 0.2 rotate -5
            repeat
        on selected_hover:
            easein 0.1 rotate 8
            easein 0.1 rotate -8
            repeat

    transform config_eff2:
        on idle:
            easein 0.5 rotate 0
        on selected_idle:
            easein 0.5 rotate 0
        on hover:
            easein 0.3 rotate 0
            easein 0.3 rotate 0
            repeat
        on selected_hover:
            easein 0.3 rotate 0
            easein 0.3 rotate 0
            repeat

    transform nav_eff:
        on idle:
            easein 0.5 xpos 552
        on selected_idle:
            easein 0.5 xpos 515
        on hover:
            easein 0.3 xpos 535
            easein 0.3 xpos 495
            easein 0.3 xpos 535
        on selected_hover:
            easein 0.3 xpos 535
            easein 0.3 xpos 495
            easein 0.3 xpos 535

    transform nav_effp:
        on idle:
            easein 0.5 ypos 15
        on selected_idle:
            easein 0.5 ypos 25
        on hover:
            easein 0.3 ypos 15
            easein 0.3 ypos 30
            easein 0.3 ypos 15
        on selected_hover:
            easein 0.3 ypos 15
            easein 0.3 ypos 30
            easein 0.3 ypos 15