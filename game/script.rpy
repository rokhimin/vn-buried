#############################################
# /Rokhimin Wahid
# /17 Desember 2016
#############################################

#############################################
# Splash Screen
#############################################

label splashscreen :
    scene splash with fade
    $renpy.pause(1.55)
return

#############################################
# Character
#############################################

define a = Character('???', color="#ffffff", window_background="img/talkbox1.png")
define j = Character('John', color="#ffffff", window_background="img/talkbox1.png")
define z = Character('911', color="#ffffff", window_background="img/talkbox1.png")
define f = Character('fax', color="#ffffff", window_background="img/talkbox1.png")
define v = Character('FBI', color="#ffffff", window_background="img/talkbox1.png")
define p = Character('OP', color="#ffffff", window_background="img/talkbox1.png")
define h = Character('Harris', color="#ffffff", window_background="img/talkbox1.png")
define x = Character('Terroris', color="#ffffff", window_background="img/talkbox1.png")
define d = Character('Dept. Nation', color="#ffffff", window_background="img/talkbox1.png")






#############################################
# main game
#############################################

label start:


scene bg black with dissolve
centered"di Iraq"
centered"10 november 2016,"
centered"jam 15:10"
scene bg satu with fade

#jam 15:10
a "Di mana ini"
a "Sempit sekali"
a "Aku tdk bisa keluar"
a "Hei..."
a "Tolong"
# menyalakan korek *sring sring
scene bg black with fade
centered"Menyalakan Korek"
scene bg korek with fade
a "Sial"
a "Apa aku sudah mati?"
a "Tolong... Tolong... Tolong"
# Bunyi telpon
# telpon mati
a "... Ada hp?"
a "siapa yang menelpon?"
a "..."
a "Aku akan mencoba menelpon 911"
# sedang menelpon 911 *bunyik tit tut tit
z "911, tunggu sebentar"
a "Tunggu! Tolong!!"
z "Ya 911?"
a "halo aku terkubur"
a "Kau harus menolongku, aku tidak bisa bernafas"
z "Pak?"
a "Aku terkubur dalam peti"
a "Tolong aku! kirim seseorang mencariku"
z "Pak... Tenanglah"
z "Siapa nama anda?"
a "John. John Connor"
z "oke Tn. John, Bisa kau katakan dimana lokasimu?"
j "Aku tidak tahu, aku terkubur di dalam peti"
j "Aku ketakutan. kau harus tolong aku"
z "Kau di dalam Peti?"
j "ya, petinya sepertinya terbuat dari kayu tua"
z "apa kau berada di pemakaman?"
j "Tidak,... aku tidak tahu"
z "bagaimana caramu menghubungiku?"
j "Apa?"
z "Kau terkubur di dalam peti, bagaimana caramu menelpon?"
j "Handphone,... Ada handphone tua di dalam peti ini"
z "Kau menelpon Menggunakan Handphone?"
j "Ya, ya. Tidak ini bukan Handphone ku"
j "Tapi ya aku menelpon dari handphone ini"
z "Ada handphone di dalam peti saat kau masuk ke dalam?"
j "Ya... apa?"
z "Bagaimana Kau bisa masuk ke peti pak?"
j "Aku tak masuk sendirian ke dalam peti"
j "Ada Seseorang yang memasukanku"
j "Kumhon Tolong aku!"
z "Dan kau berkata petinya dikubur?"
j "Ya, aku pengemudi truck dan aku orang amerika"
j "disini... disini panas, aku tak bisa bernafas, cepat tolonglah?"
z "kau tahu lokasimu pak?"
j "Su...Sudah kubilang, suatu tempat di irak "
z "Irak?"
j "Ya aku pengemudi truck, aku orang amerika. aku bekerja untuk CRT"
z "Apa kau tentara pak?"
j "Tidak... aku pengemudi truck"
j "Aku bekerja untuk kontraktor sipil di irak. kita diserang di Baqubah. mereka menembaki kami semua"
z "Mereka menembak siapa, pak?"
j "Semua pengemudi"
z "Dan kau bilang semua itu terjadi di irak?"
j "Ya. kumohon dengarkan aku, oke?"
j "Dengar, mereka memberikan aku nomor darurat dan itu ada di dompetku. dan aku tak tahu berada dimana"
z "Tn. John, ini nomor darurat 911 di Youngstown,Ohio"
j "Ohio?"
z "Ya pak, aku tak yakin bagaimana kau menelpon kami dari negara lain. aku bisa menyambungkan langsung ke kantor Sherif"
j "Tidak. kau tidak paham, lupakan"
# Melihat battry hpp tinggal sedikit
# mematikan korek
j "Oke. oke. oke"
# menyalakan korek
# menelpon linda isti
j "kumohon angkat... angkat"
j "angkatlah"
f "Terima kasih sudah menghubungi kediaman Connor. Kita tidak ada di rumah sekarang..."
f "Tolong tinggalkan pesan setelah nada *Beep .Terima Kasih"
# Bunyi beep
j "Linda. Linda sayang ini aku"
j "Aku perlu kau menghubungi national guard sekarang..."
j "atau Pentagon"
j "Katakan ke merekan, kita diserang di provinsi di Baqubah"
j "Mereka harus menemukan aku, oke?"
j "Kumohon sayang, bantu mereka menemukan aku"
# mematikan telepon
scene bg black with fade
centered"10 november 2016, Jam 15.35"
#menelpon FBI
p "Apa nama kota dan negara bagian nya?"
j "Aku tak tahu. FBI di manapun mereka berada"
p "Kau punyak nomor spesifik yang ingin langsung dihubungi?"
j "Terserah kota mana saja. tolong hubungkan aku ke FBI"
p "Pak, kita punya kantor FBI di Boston,Chicago,Newyork,Texas"
j "tak masalah, terserah kota mana saja!!!"
p "maafkan aku pak, tapi aku tak boleh melakukannya"
j "CHICAGO, OKE!!!"
p "Tak perlu kasar, pak"
p "nomor yang kau minta"
p "3"
p "1"
p "2"
p "4"
p "2"
p "1"
p "6"
p "7"
p "0"
p "0"
p "Bisa dihubungi dengan biaya 25sen, dengan menekan nomor 1"
v "Chicago field office. spesial agent Harris"
p "Apa ini FBI?"
h "Ya, pak?"
j "Oke, aku menelpon dari irak"
j "Aku terkubur di suatu gurun"
h "Whoa..whoa.. Tenanglah pak"
h "Kapan kau di irak?"
j "Sekarang"
j "Aku disini sekarang, aku seorang pengemudi truck untuk CRT. aku sudah bekerja selama 9 bulan"
h "Bisa kutahu namamu pak?"
j "John Connor"
h "Oke, John jelaskan kepadaku apa yang terjadi?"
j "Baiklah, baiklah oke"
j "Aku dan rombongan pengemudi lainya..."
j "Sedang mengantarkan suplai dapur ke komunitas pusat"
j "Beberapa anak mulai melempar truck dengan batu"
j "Lalu bom meledak dan menghancurkan salah satu truck"
j "Lalu ada orang yang keluar dari belakang rumah dan mulai menembak semua orang, tepat ditengah jalan"
h "Apa kau tertembak"
j "Aku tak tahu!"
j "Aku tak tahu, aku berada paling belakang"
J "Kurasa kepalaku terkena lemparan batu dan aku pingsan, itu hal terakhir yang kuingat dan aku terbangun dan terikat di peti"
h "Siapa yang menaruhmu dalam peti?"
j "Kurasa orang yang menyerang kami"
h "Segrombolan Anak?"
j "Tidak, tidak. anak-anak hanya melempar batu lalu muncul orang irak... mungkin pemberontak. Aku tak tahu"
j "Mereka tiba-tiba muncul dan langsung menembaki semua orang"
h "Di jalan? Kau bilang mereka tidak menembakmu?"
j "Mereka tak menembakku, entahlah! Tapi mereka menembak rombonganku"
j "Aku perlu kau menolongku"
h "Oke, oke, oke1"
j "bisa kau lacak teleponku? GPS atau semacamnya?"
h "Ya,kami akan........."
# telp terputus karena sinyal
# mencari sinyal
# mencoba menelpon nomer terroris yg tidak terjawab tadi
j "Halo?"
x "Bernafas tak bernafas, orang amerika? hah?"
x "Bernafas tak bernafas?"
j "Aku tak tahu apa yang kau katakan? Siapa ini?"
x "Orang amerika bisa bernafas tak bisa bernafas?"
j "Aku tak bisa bernafas. tolong keluarkan aku dari sini"
x "Keluar?"
j "Ya, Keluarkan aku. kumohon"
x "Tentara?"
j "Bukan, aku bukan tentara"
j "Aku pengemudi truck untuk kontraktor"
x "Blackwater?"
j "Bukan, bukan untuk blackwater. aku bukan satpam untuk kontraktor"
j "Aku hanya pengemudi truck"
x "Kau orang amerika?"
j "Ya"
x "Berarti aku tentara?"
j "Bukan, aku bukan tentara. aku tak bersenjata. tapi kau menembaki kami"
x "Dalam hati dan pikiran. jangan berkata bohong"
j "Aku tak berbohong, kita semua pengemudi truck"
x "Pengemudi apa?"
j "Truck. Truck"
x "Uang 5 juta dollar"
j "apa?"
x "Sediakan uang 5 juta dollar malam ini jam 9 atau kau tetap disana, terkubur seperti anjing"
j "5 juta? dari siapa?"
x "Keluargamu"
j "keluargaku tak punya uang 5 juta dollar. jika mereka punya , maka aku tak disini"
x "Dari kedutaan"
j "Aku tak tahu, ya. ya... dari kedutaan"
x "9 malam. 5 juta dollar"
# telp diputus
j "fuck you terroris"
# selang 30 menit
# menghubungi departemen negara
d "Departemen pemerintahan amerika serikat"
j "Aku warga negara amerika, bekerja di irak. aku sedang disandra"
j "Aku perlu berbicara ke seseorang segera"
d "Anda menelpon dari mana pak, Pak?"






scene bg black with fade
centered"END"
return

#############################################