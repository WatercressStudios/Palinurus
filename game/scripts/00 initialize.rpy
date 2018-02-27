######################### 
# Character Declaration #
#########################
define v = Character(None, kind=nvl, what_xalign=0.5, window_xalign=0.5)
define b = Character("Budapest", color="#B33542", show_two_window=True, who_ypos=-2, voice_tag="budapest")
define p = Character("Passenger", color="#3b56c4", show_two_window=True, who_ypos=-2)
define i = Character("Illarion", color="#3b56c4", show_two_window=True, who_ypos=-2, voice_tag="illarion")


# Allows the NVL in the 1st 4 lines to be center aligned without doing it manually.
init:
    style nvl_vbox:
        xfill True

    $ c = Character(None, kind=nvl, what_prefix="", what_suffix="")

######################
# Sprite Declaration #
######################
#Blue Pearl
image budaconsad = im.Scale("cg/budaconsad.png", 1280, 720) 
image earth = "cg/venus.png"
#Additional
image bud angry                  = "sprites/bud_angry.png"
image bud angryfrown             = "sprites/bud_angryfrown.png"
image bud neutral                = "sprites/bud_neutral.png"
image bud neutralclosed          = "sprites/bud_neutralclosed.png"
image bud neutralhalf            = "sprites/bud_neutralhalf.png"
image bud neutralsmalltalk       = "sprites/bud_neutralsmalltalk.png"
image bud neutralsquint          = "sprites/bud_neutralsquint.png"
image bud neutraltalk            = "sprites/bud_neutraltalk.png"
image bud sad                    = "sprites/bud_sad.png"
image bud shock                  = "sprites/bud_shock.png"
image bud smile                  = "sprites/bud_smile.png"
image bud smiletalk              = "sprites/bud_smiletalk.png"
image bud smiletalkclosed        = "sprites/bud_smiletalkclosed.png"
image bud closedworryx           = "sprites/bud_closedworryx.png"
image bud worryx                 = "sprites/bud_worryx.png"
image bud panic                  = "sprites/bud_panic.png"
image bud panicfrown             = "sprites/bud_panicfrown.png"
image bud panicslight            = "sprites/bud_panicslight.png"
image bud panicsquintx           = "sprites/bud_panicsquintx.png"
image bud worryclosex            = "sprites/bud_worryclosex.png"
image bud neutralx               = "sprites/bud_neutralx.png"
image bud angrytalkx             = "sprites/bud_angrytalkx.png"
image bud angrytalk              = "sprites/bud_angrytalk.png"
image bud srsfaec                = "sprites/bud_srsfaec.png"
image bud normaltalkeyebrows     = "sprites/bud_normaltalkeyebrows.png"
image bud worrytalkx             = "sprites/bud_worrytalkx.png"
image bud panicx                 = "sprites/bud_panicx.png"
image bud worryyellhalfeye       = "sprites/bud_worryyellhalfeye.png"
image bud worryneutralhalfeye    = "sprites/bud_worryneutralhalfeye.png"
image bud worrysquintx           = "sprites/bud_worrysquintx.png"
image bud worrysquinttalkx       = "sprites/bud_worrysquinttalkx.png"
image bud panictalkx             = "sprites/bud_panictalkx.png"
image bud panicquietx            = "sprites/bud_panicquietx.png"
image bud weaksmile              = "sprites/bud_weaksmile.png"
image bud painfullook            = "sprites/bud_painfullook.png"
image bud painfullooksquint      = "sprites/bud_painfullooksquint.png"
image bud srsfaectalk            = "sprites/bud_srsfaectalk.png"
image bud devious                = "sprites/bud_devious.png"
image bud sassy                  = "sprites/bud_sassy.png"
image bud panicquietx            = "sprites/bud_panicquietx.png"
image bud excitedclosed          = "sprites/bud_excitedclosed.png"
image bud excitedsmileclosed     = "sprites/bud_excitedsmileclosed.png"
image bud shrugclosed            = "sprites/bud_shrugclosed.png"
image bud neutraleyebrowsx       = "sprites/bud_neutraleyebrowsx.png"
image bud blushstammer           = "sprites/bud_blushstammer.png"
image bud panicquiet             = "sprites/bud_panicquiet.png"
image bud neutralsilentx         = "sprites/bud_neutralsilentx.png"
image bud bigsmileneutral        = "sprites/bud_bigsmileneutral.png"
image bud bigsmile               = "sprites/bud_bigsmile.png"
image bud stare                  = "sprites/bud_stare.png"
image bud weaksmiletalksquint    = "sprites/bud_weaksmiletalksquint.png"
image bud smirkx                 = "sprites/bud_smirkx.png"
image bud worrysquinttalk        = "sprites/bud_worrysquinttalk.png"
image bud neutralupx             = "sprites/bud_neutralupx.png"
image bud depressedtalkx         = "sprites/bud_depressedtalkx.png"
image bud depressedclosed        = "sprites/bud_depressedclosed.png"
image bud depressedtalk          = "sprites/bud_depressedtalk.png"
image bud shocktalk              = "sprites/bud_shocktalk.png"
image bud painfullooktalk        = "sprites/bud_painfullooktalk.png"
image bud worryclosetalk         = "sprites/bud_worryclosetalk.png"
image bud surprise               = "sprites/bud_surprise.png"
image bud surpriseneutral        = "sprites/bud_surpriseneutral.png"
image bud surpriseneutraltalk    = "sprites/bud_surpriseneutraltalk.png"
image bud smileup                = "sprites/bud_smileup.png"
image bud bigsmileclosed         = "sprites/bud_bigsmileclosed.png"
image bud stammer                = "sprites/bud_stammer.png"
image bud neutralworry           = "sprites/bud_neutralworry.png"
image bud awkwardblush           = "sprites/bud_awkwardblush.png"
image bud awkwardblushtalk       = "sprites/bud_awkwardblushtalk.png"
image bud blush                  = "sprites/bud_blush.png"
image bud poutblush              = "sprites/bud_poutblush.png"
image bud smileclosed            = "sprites/bud_smileclosed.png"
image bud panicquiettalkx        = "sprites/bud_panicquiettalkx.png"
image bud bigworryx              = "sprites/bud_bigworryx.png"
image bud panicshout             = "sprites/bud_panicshout.png"
image bud panicsquinttalkx       = "sprites/bud_panicsquinttalkx.png"
image bud panicwincex            = "sprites/bud_panicwincex.png"
image bud babbleclosed           = "sprites/bud_babbleclosed.png"
image bud shametalk              = "sprites/bud_shametalk.png"
image bud forcedsmirk            = "sprites/bud_forcedsmirk.png"
image bud bigblush               = "sprites/bud_bigblush.png"
image bud bigblushquiet          = "sprites/bud_bigblushquiet.png"
image bud excitedtalk            = "sprites/bud_excitedtalk.png"
image bud panicquiettalkx        = "sprites/bud_panicquiettalkx.png"
image bud crysad                 = "sprites/bud_crysad.png"
image bud crysing                = "sprites/bud_crysing.png"
image bud cryslight              = "sprites/bud_cryslight.png"
image bud crysmile               = "sprites/bud_crysmile.png"
image bud cryyell                = "sprites/bud_cryyell.png"
image bud cryclosed              = "sprites/bud_cryclosed.png"
image bud cryclosedneutral       = "sprites/bud_cryclosedneutral.png"
image bud embarrassed            = "sprites/bud_embarrassed.png"
image bud sassyeyebrowsneutralx  = "sprites/bud_sassyeyebrowsneutralx.png"
image bud sassyeyebrowsx         = "sprites/bud_sassyeyebrowsx.png"
image bud devioussmilex          = "sprites/bud_devioussmilex.png"
image bud silentsurprisex        = "sprites/bud_silentsurprisex.png"
image bud awkwardchuckle         = "sprites/bud_awkwardchuckle.png"
image bud neutralupthinkx        = "sprites/bud_neutralupthinkx.png"
image bud smallsmile             = "sprites/bud_smallsmile.png"
image bud panicquieterx          = "sprites/bud_panicquieterx.png"
image bud lamentx                = "sprites/bud_lamentx.png"
image bud sweetsmileclosed       = "sprites/bud_sweetsmileclosed.png"
image bud sadsmilex              = "sprites/bud_sadsmilex.png"
image bud sadsmile               = "sprites/bud_sadsmile.png"
image bud worryyellhalfeyex      = "sprites/bud_worryyellhalfeyex.png"
image bud worryyellhalfeyequietx = "sprites/bud_worryyellhalfeyequietx.png"
image bud prodding               = "sprites/bud_prodding.png"
image bud feisty                 = "sprites/bud_feisty.png"
image bud smallsmileclosed       = "sprites/bud_smallsmileclosed.png"
image bud nostalgic              = "sprites/bud_nostalgic.png"
image bud peacefulsmile          = "sprites/bud_peacefulsmile.png"
image bud blushsurprise          = "sprites/bud_blushsurprise.png"
image bud blushcalming           = "sprites/bud_blushcalming.png"
image bud shockx                 = "sprites/bud_shockx.png"
image bud blushsmirk             = "sprites/bud_blushsmirk.png"
image bud angryclosedx           = "sprites/bud_angryclosedx.png"
image bud angryyellclosedx       = "sprites/bud_angryyellclosedx.png"
image bud closeneutralx          = "sprites/bud_closeneutralx.png"
image bud weaksmiletalk          = "sprites/bud_weaksmiletalk.png"
image bud smilewarmclosed        = "sprites/bud_smilewarmclosed.png"
image bud weaksmilesquint        = "sprites/bud_weaksmilesquint.png"
image bud blushwarmsmile         = "sprites/bud_blushwarmsmile.png"
image bud blushremember          = "sprites/bud_blushremember.png"
image bud blushremembertalk      = "sprites/bud_blushremembertalk.png"
image bud blushweaksmiletalk     = "sprites/bud_blushweaksmiletalk.png"
image bud acceptance             = "sprites/bud_acceptance.png"
image bud painfullookx           = "sprites/bud_painfullookx.png"
image bud sassysmirkx            = "sprites/bud_sassysmirkx.png"
image bud shrugneutralx          = "sprites/bud_shrugneutralx.png"
image bud blushbigsurprise       = "sprites/bud_blushbigsurprise.png"
image bud blushbigpanic          = "sprites/bud_blushbigpanic.png"
image bud blushhalfx             = "sprites/bud_blushhalfx.png"
image bud thinking               = "sprites/bud_thinking.png"
image bud bigsmilex              = "sprites/bud_bigsmilex.png"
image bud smilesquint            = "sprites/bud_smilesquint.png"
image bud smilesquinttalk        = "sprites/bud_smilesquinttalk.png"
image bud smileclosedcheery      = "sprites/bud_smileclosedcheery.png"
image bud whateven               = "sprites/bud_whateven.png"
image bud neutrallistening       = "sprites/bud_neutrallistening.png"
image bud clarity                = "sprites/bud_clarity.png"
image bud jawdropx               = "sprites/bud_jawdropx.png"
image bud neutralsquinty         = "sprites/bud_neutralsquinty.png"
image bud forcedsmirktalk        = "sprites/bud_forcedsmirktalk.png"
image bud secondguessx           = "sprites/bud_secondguessx.png"
image bud bigawkwardlaugh        = "sprites/bud_bigawkwardlaugh.png"
image bud stumblex               = "sprites/bud_stumblex.png"
image bud smilex                 = "sprites/bud_smilex.png"
image bud smilesclosedcheery     = "sprites/bud_smilesclosedcheery.png"

# Console Sprites
image console warningneutral       = "sprites/console_warningneutral.png"
image console warningshout         = "sprites/console_warningshout.png"
image console warningangryshout    = "sprites/console_warningangryshout.png"
image console warningpause         = "sprites/console_warningpause.png"
image console loreyelluplook       = "sprites/console_loreyelluplook.png"
image console loreuplook           = "sprites/console_loreuplook.png"
image console loremad              = "sprites/console_loremad.png"
image console loremadlook          = "sprites/console_loremadlook.png"
image console lorewarmsmilelook    = "sprites/console_lorewarmsmilelook.png"
image console lorequestioninglook  = "sprites/console_lorequestioninglook.png"
image console loreyelllook         = "sprites/console_loreyelllook.png"
image console loresurprise         = "sprites/console_loresurprise.png"
image console lorepaniclook        = "sprites/console_lorepaniclook.png"
image console loreexcitelook       = "sprites/console_loreexcitelook.png"
image console loreexcite           = "sprites/console_loreexcite.png"
image console loreexcite2          = "sprites/console_loreexcite2.png"
image console loreexcite3          = "sprites/console_loreexcite3.png"
image console loresmile            = "sprites/console_loresmile.png"
image console loresmilelook        = "sprites/console_loresmilelook.png"
image console loretalk             = "sprites/console_loretalk.png"
image console loretalklook         = "sprites/console_loretalklook.png"
image console ameliasmilelook      = "sprites/console_ameliasmilelook.png"
image console lorechat             = "sprites/console_lorechat.png"
image console loadworrylook        = "sprites/console_loadworrylook.png"
image console load                 = "sprites/console_load.png"
image console loadworry            = "sprites/console_loadworry.png"
image console loadup               = "sprites/console_loadup.png"
image console loadfocus            = "sprites/console_loadfocus.png"
image console warningsoftsmilelook = "sprites/console_warningsoftsmilelook.png"
image console warningsoftsmiletalk = "sprites/console_warningsoftsmiletalk.png"
image console talklook             = "sprites/console_talklook.png"
image console smile                = "sprites/console_smile.png"
image console talk                 = "sprites/console_talk.png"
image console smileeyebrowslook    = "sprites/console_smileeyebrowslook.png"
image console warning              = "sprites/console_warning.png"
image console warningtalk          = "sprites/console_warningtalk.png"
image console warninglook          = "sprites/console_warninglook.png"
image console warningeyebrow       = "sprites/console_warningeyebrow.png"
image console warningworry         = "sprites/console_warningworry.png"
image console warningsmile         = "sprites/console_warningsmile.png"
image console warningsmilelook     = "sprites/console_warningsmilelook.png"
image console worrylook            = "sprites/console_worrylook.png"
image console warningworrytalk     = "sprites/console_warningworrytalk.png"
image console lorelook             = "sprites/console_lorelook.png"
image console worryyell            = "sprites/console_worryyell.png"

##################
# BG Declaration #
##################
image black                = "#000"
image white                = "#FFF"
image cockpit              = "bg/cockpit.png" # Cockpit with transparent surface
image cockpithangar        = "bg/cockpithangar.png"
image cockpit1             = "bg/cockpit1.png" # Cockpit in Scenes 1-4 and 7-10
image cockpit2             = "bg/cockpit2.png" # Cockpit in Scene 5 Parts 1-3
image cockpit3             = "bg/cockpit3.png" # Cockpit in Scene 5 Parts 4-5
image cockpit4             = "bg/cockpit4.png" # Cockpit in Scene 6
image space                = "bg/space.png"
image cockpitside          = "bg/cockpitside.png"
image cockpitsidehangar    = "bg/cockpitsidehangar.png"
image station              = "bg/station.png"
image shuttle              = "bg/shuttle.png"
image cabin                = "bg/cabin.png"
image cockpitemergency     = "bg/cockpitemergency.png"
image cockpitsideemergency = "bg/cockpitsideemergency.png"
image meteoroids           = "bg/meteoroids.png"
image cabinfire            = "bg/cabinfire.png"
image cockpitblackout      = "bg/cockpitblackout.png"
image nebula               = "bg/nebula.jpg"

image blackocean1          = "bg/blackocean1_ad.jpg"   
image blackocean2          = "bg/blackocean2_ad.jpg"   
image blackocean3          = "bg/blackocean3_ad.jpg"   
image blackocean4          = "bg/blackocean4_ad.jpg"  
image capepalinuro         = "bg/capepalinuro_ad.png"
image shuttle              = "bg/palinurushanger_ad.png"
image cabin                = "bg/shipcabin1_ad.png"
image cabin2                = "bg/shipcabin2_ad.png"
image cabin3                = "bg/shipcabin3_ad.png"
image offwhite             = "#A9A9A9"
image offred               = "#2F0D0D"
image stationdeparture     = "bg/mirabellestation window_ad.png"


###################
# Anniversary CGs #
###################
# These are under init so that they are loaded when the game starts, so they can be accessed from
# the gallery
init:

    image blush                    = "cg/blush.png" #Added
    image budablush                = "cg/budablush.png" #Added
    image budablush2               = "cg/budablush2.png" #Added
    image budablush3               = "cg/budablush3.png" #Added
    image budablush4               = "cg/budablush4.png" #Added
    image budablush5               = "cg/budablush5.png" #Added
    image budaproud                = "cg/budaproud.png" #Added
    image budasmile1               = "cg/budasmile.png" #Added
    image budasmile2               = "cg/budasmile2.png" #Added
    image budaspeak                = "cg/budaspeak.png" #Added
    image dream                    = "cg/dream.png" #Added
    image end1                     = "cg/end1.png" #Added
    image end2                     = "cg/end2.png" #Added
    image end3                     = "cg/end3.png" #Added
    image end4                     = "cg/end4.png" #Added
    image end5                     = "cg/end5.png" #Added
    image end6                     = "cg/end6.png" #Added
    image hours                    = "cg/hours.png" #Added
    image hug                      = "cg/hug.png" #Added
    image initialization           = "cg/initialization.png" #Added
    image prestasisangry           = "cg/prestasisangry.png" #Added
    image prestasisworried         = "cg/prestasisworried.png" #Added
    image prestasisworriedspeaking = "cg/prestasisworriedspeaking.png" #Added
    image joy1                     = "cg/Redo 1.png" #Added
    image joy2                     = "cg/Redo 2.png" #Added
    image joy3                     = "cg/Redo 3.png" #Added
    image joy4                     = "cg/Redo 4.png" #Added
    image joy5                     = "cg/Redo 5.png" #Added
    image sing1                    = "cg/Sing.png" #Added
    image sing2                    = "cg/sing2.png" #Added
    image surprised                = "cg/surprised.png" #Added
    
    image singingdreamgirl         = "cg/singingdreamgirl_ad.png"
    image starhands                = "cg/handsofstars_ad.png"
    image silouettebudapest        = "cg/silouettebudapest_ad.png"
    image broken                   = "cg/crackedwindshield_ad.png"


    # Art Gallery Images
    image art1    = "cg/artgal/001.jpg"
    image art2    = "cg/artgal/002.png"
    image art3    = "cg/artgal/003.png"
    image art3p2  = "cg/artgal/003-2.png"
    image art3p3  = "cg/artgal/003-3.png"
    image art3p4  = "cg/artgal/003-4.png"
    image art3p5  = "cg/artgal/003-5.png"
    image art3p6  = "cg/artgal/003-6.png"
    image art3p7  = "cg/artgal/003-7.png"
    image art4    = "cg/artgal/004.png"
    image art5    = "cg/artgal/005.png"
    image art5p2  = "cg/artgal/005-2.png"
    image art5p3  = "cg/artgal/005-3.png"
    image art6    = "cg/artgal/006.png"
    image art7    = "cg/artgal/007.png"
    image art8    = "cg/artgal/008.png"
    image art9    = "cg/artgal/009.png"
    image art10   = "cg/artgal/010.png"
    image art10p2 = "cg/artgal/010-2.png"
    image art10p3 = "cg/artgal/010-3.png"
    image art11   = "cg/artgal/011.png"
    image art12   = "cg/artgal/012.png"
    image art12p2 = "cg/artgal/012-2.png"
    image art13   = "cg/artgal/013.png"
    image art14   = "cg/artgal/014.png"
    image art14p2 = "cg/artgal/014-2.png"
    image art14p3 = "cg/artgal/014-3.png"
    image art14p4 = "cg/artgal/014-4.png"
    image art14p5 = "cg/artgal/014-5.png"
    image art14p6 = "cg/artgal/014-6.png"
    image art15   = "cg/artgal/015.png"
    image art15p2 = "cg/artgal/015-2.png"
    image art15p3 = "cg/artgal/015-3.png"
    image art16   = "cg/artgal/016.png"
    image art17   = "cg/artgal/017.png"
    image art17p2 = "cg/artgal/017-2.png"
    image art17p3 = "cg/artgal/017-3.png"
    image art17p4 = "cg/artgal/017-4.png"
    image art17p5 = "cg/artgal/017-5.png"
    image art18   = "cg/artgal/018.png"
    image art18p2 = "cg/artgal/018-2.png"
    image art18p3 = "cg/artgal/018-3.png"
    image art18p4 = "cg/artgal/018-4.png"
    image art18p5 = "cg/artgal/018-5.png"
    image art18p6 = "cg/artgal/018-6.png"
    image art19   = "cg/artgal/019.jpg"
    image art19p2 = "cg/artgal/019-2.jpg"
    image art20   = "cg/artgal/020.png"
    image art21   = "cg/artgal/021.jpg"
    image art22   = "cg/artgal/022.png"
    image art23   = "cg/artgal/023.png"
    image art24   = "cg/artgal/024.png"
    image art25   = "cg/artgal/025.jpg"

#######
# VFX #
#######
image watercress = "vfx/watercress.png"

# Splash Screen
label splashscreen:
    play music "music/Ode To Joy.ogg"
    scene black
    with Pause(1)
    
    if persistent.ending  == "Complete":
        show watercresspalinurus with dissolve
        with Pause(2)

        scene watercress with dissolve
        with Pause(1)

        return
    else:
        show watercress with dissolve
        with Pause(2)

        scene black with dissolve
        with Pause(1)
        return
    
image blackoceanlight = "vfx/blackoceanlight_ad.png" #Used during the dream sequence as a blinking white light.

image blackoceanrain1 = "vfx/blackoceanrain1_ad.png" #Black rain for your nightmare oceans    
image blackrain = SnowBlossom("blackoceanrain1", count=20, border=50, xspeed=(50, -50), yspeed=(1500, 1750), start=0, fast=True, horizontal=False)

image blackoceanrain2 = "vfx/blackoceanrain2_ad.png" #Lighter rain for when the ocean consumes you   
image lightrain = SnowBlossom("blackoceanrain2", count=20, border=50, xspeed=(250, -250), yspeed=(1400, 1800), start=0, fast=True, horizontal=False)

image redrecoloredrain = im.Recolor("vfx/blackoceanrain2_ad.png", 139, 0, 0, 255)
image bloodrain = SnowBlossom("redrecoloredrain", count=7, border=50, xspeed=(0, 0), yspeed=(1600, 2000), start=0, fast=True, horizontal=False)

image bubble1 = "vfx/bubble1_ad.png" #Bubbles used during dream sequence  
image bubbles1 = SnowBlossom("bubble1", count=20, border=50, xspeed=(500, -500), yspeed=(-1400, -1800), start=0, fast=True, horizontal=False)
image bubbles2 = SnowBlossom("bubble1", count=10, border=50, xspeed=(500, -500), yspeed=(-900, -1200), start=0, fast=True, horizontal=False)

image spray = "vfx/spray_ad.png" #Easiest Animation ever.
image sprayeffect = SnowBlossom("spray", count=20, border=50, xspeed=(1500, -1500), yspeed=(-900, -1000), start=0, fast=True, horizontal=False)
image dust = SnowBlossom("spray", count=10, border=10, xspeed=(-50, -125), yspeed=(50, 100), start=0, fast=True, horizontal=False)
image dust2 = SnowBlossom("spray", count=10, border=10, xspeed=(-50, 50), yspeed=(50, 70), start=0, fast=True, horizontal=False)
image dust3 = SnowBlossom("spray", count=50, border=10, xspeed=(1000, -1000), yspeed=(1000, -1000), start=0, fast=True, horizontal=False)

image blink movie = Movie(channel="blink", play="vfx/budapestblinking.m2t")     #Animation/Movie clip of  Budapest blinking during the protagonist's dream sequence



image freezing1 = "vfx/freezingeffect1_ad.png"                          #Used for when Budapest administers the cyrostasis on the protagonist
image freezing2 = "vfx/freezingeffect2_ad.png"
image needles = "vfx/needles_ad.png"

image life1 = im.Recolor("vfx/freezingeffect1_ad.png", 168, 0, 0, 255)
image life2 = im.Recolor("vfx/freezingeffect2_ad.png", 118, 6, 6, 255)


image redlight = "vfx/redlight_ad.png"                                  #Annoying red light, used in various scenes as a warning light
                             
image greenlight = "vfx/greenlight_ad.png"      #Used once when Budapest fixes te various errors popping up



image spotlight = "vfx/spotlight_ad.png"                                #Used for various scenes of Budapest appearing and reappearing as a subtle effect

image redscreens = "vfx/redscreens_ad.png"                              #Red error screens used for after asteroid sequence.

image map1 = "vfx/cyclemaps1_ad.png"                                    #Maps 1-3 are used for an animation, the 4th one is supposed to be the image with the 'Space Station'
image map2 = "vfx/cyclemaps2_ad.png"
image map3 = "vfx/cyclemaps3_ad.png"
image map4 = "vfx/cyclemaps4_ad.png"

image starslongtrip = "vfx/starspalinurus_ad.png"                       #Upon learning of their perdicament, the protagonist and Budapest look to the stars, this is used during that scene
image starsgazing = "vfx/starspalinurus2_ad.png"
image blink1 = Image("vfx/blink_ad.png",)
image blink2 = im.Flip("vfx/blink_ad.png", vertical=True,)              #Used for blinking/eyes closing animations, mirrored to save space

init:
    image mapchecks = Animation("vfx/cyclemaps1_ad.png", 0.1,           #Animation of Budapest flipping through star maps rapidly    
                                "vfx/cyclemaps2_ad.png", 0.1,
                                "vfx/cyclemaps3_ad.png", 0.1,)
    
init:
    image rebootscreens = Animation("vfx/reboot1_ad.png", 0.05,         #Green flickering screens after the asteroid scene when the computer reboots and before Budapest reappears
                                    "vfx/reboot2_ad.png", 0.05,
                                    "vfx/reboot3_ad.png", 0.05,
                                    "vfx/reboot4_ad.png", 0.05,)
    
image blackoceancorner1 = "vfx/blackoceancorner1_ad.png"
image blackoceancorner2 = "vfx/blackoceancorner2_ad.png"

image darkclouds = "vfx/darkdreamclouds_ad.png"
image stormclouds = im.MatrixColor("vfx/darkdreamclouds_ad.png", im.matrix.invert())

image budapestcorner = "vfx/budapestcorner_ad.png"

image budapestcity1 = "vfx/budapestcity1_ad.png"
image budapestcity2 = "vfx/budapestcity2_ad.png"
image budapestcity3 = "vfx/budapestcity3_ad.png"
image budapestcityzoom = "vfx/budapestzoom_ad.png"

image departlights = "vfx/departurelights_ad.png"

image sparkstrip = anim.Filmstrip("vfx/sparks_ad.png", (4,4), (1,500), 0.01) 
image sparks = SnowBlossom("sparkstrip", count=30, border=5, xspeed=(-300, 300), yspeed=(1300, 800), start=10, fast=True, horizontal=False)
image sparks2 = SnowBlossom("firefilmstrip", count=50, border=5, xspeed=(-300, 300), yspeed=(1000, 800), start=10, fast=True, horizontal=False)
image sparks3 = SnowBlossom("sparkstrip", count=30, border=5, xspeed=(-500, 500), yspeed=(1300, 2300), start=10, fast=True, horizontal=False)
image sparks4 = SnowBlossom("firefilmstrip", count=50, border=5, xspeed=(-500, 500), yspeed=(1000, 2300), start=10, fast=True, horizontal=False)
    
image firefilmstrip = anim.Filmstrip("vfx/fire.png", (2,2), (1,250), 0.1) 
image firedown = SnowBlossom("firefilmstrip", count=30, border=30, xspeed=(-150, 150), yspeed=(25, 75), start=10, fast=True, horizontal=True)           #Red Particle effects for Budapest
image fireup = SnowBlossom("firefilmstrip", count=70, border=4, xspeed=(-1500, 1500), yspeed=(-250, -500), start=10, fast=True, horizontal=False)
image firelast = SnowBlossom("firefilmstrip", count=70, border=4, xspeed=(-1500, 1500), yspeed=(250, 500), start=10, fast=True, horizontal=False)

image waterfilmstrip = anim.Filmstrip("vfx/water.png", (2,2), (1,250), 0.1) 
image waterdown = SnowBlossom("waterfilmstrip", count=10, border=4, xspeed=(-150, 150), yspeed=(25, 75), start=10, fast=True, horizontal=True)                 #Blue Particle  effects for Budapest
image waterup = SnowBlossom("waterfilmstrip", count=70, border=4, xspeed=(-1500, 1500), yspeed=(-250, -500), start=10, fast=True, horizontal=False)
image waterlast = SnowBlossom("waterfilmstrip", count=70, border=4, xspeed=(-1500, 1500), yspeed=(250, 500), start=10, fast=True, horizontal=False)

image cockpit1blurry = "vfx/cockpit1blurry.png"                            #Used during the final scenes when the protagonist wakes from his slumber

image finalspotlight = "vfx/finalspotlight_ad.png"

image map zoom1 = "vfx/zoommaps1_ ad.png"                                  #Used for when Budapest shows the protagonist the space maps
image map zoom2 = "vfx/zoommaps2_ ad.png"
image map zoom3 = "vfx/zoommaps3_ ad.png"
image map zoom4 = "vfx/zoommaps4_ ad.png"

image dreamhands = "vfx/starhands_ad.png"

image airescaping = "vfx/airescaping_ad.png"

image osb 1 = "vfx/osreboot1_ad.png"                                       #Used for the scene of the computer rebooting and before Budapest reappears
image osb 2 = "vfx/osreboot2_ad.png"
image osb 3 = "vfx/osreboot3_ad.png"
image osb 4 = "vfx/osreboot4_ad.png"
image osb 5 = "vfx/osreboot5_ad.png"
image osb 6 = "vfx/osreboot6_ad.png"
image osb 7 = "vfx/osreboot7_ad.png"
image osb 8 = "vfx/osreboot8_ad.png"
image osb 9 = "vfx/osreboot9_ad.png"

image pole1 = SnowBlossom("vfx/pole_ad.png", count=6, border=30, xspeed=(-450, 450), yspeed=(1000, 1200), start=1, fast=True, horizontal=False)
image redrocks = SnowBlossom("vfx/redrock_ad.png", count=3, border=30, xspeed=(-500, 500), yspeed=(1000, 1200), start=1, fast=True, horizontal=False)
init:
    image emotionaleyes = Animation("vfx/emoeyes1_ad.png", 0.05,           #Subtle glint when Budapest loses part of herself; her eyes glint upon the mention of "Emotion"
                                    "vfx/emoeyes2_ad.png", 0.05,
                                    "vfx/emoeyes3_ad.png", 0.05,
                                    "vfx/emoeyes4_ad.png", 0.05,
                                    "vfx/emoeyes5_ad.png", 0.05,
                                    "vfx/emoeyes6_ad.png", 0.05,
                                    "vfx/emoeyes7_ad.png", 0.05,)
    
init:
    image shipflight = Animation("vfx/shipwarp1_ad.png", 0.1,           #Subtle glint when Budapest loses part of herself; her eyes glint upon the mention of "Emotion"
                                    "vfx/shipwarp2_ad.png", 0.1,
                                    "vfx/shipwarp3_ad.png", 0.1,
                                    "vfx/shipwarp4_ad.png", 0.1,
                                    "shipwarp5", 0.1,
                                    "shipwarp6", 0.1,
                                    "shipwarp7", 0.1,
                                    "shipwarp8", 0.1,)
    
init:
    image filmgrains = Animation("vfx/filmgrain1_ad.png", 0.05,           #Subtle glint when Budapest loses part of herself; her eyes glint upon the mention of "Emotion"
                                    "vfx/filmgrain2_ad.png", 0.05,
                                    "vfx/filmgrain3_ad.png", 0.05,
                                    "vfx/filmgrain4_ad.png", 0.05,
                                    "vfx/filmgrain5_ad.png", 0.05,
                                    "vfx/filmgrain6_ad.png", 0.05,)
    
image desertsky = "vfx/deserthorizon_ad.png"

image emptypod = "vfx/stasispod_ad.png"

image budapestface = "vfx/facezoom_ad.png"
    
image shipwarp5 = im.Flip("vfx/shipwarp1_ad.png",horizontal=True)
image shipwarp6 = im.Flip("vfx/shipwarp2_ad.png",horizontal=True)
image shipwarp7 = im.Flip("vfx/shipwarp3_ad.png",horizontal=True)
image shipwarp8 = im.Flip("vfx/shipwarp4_ad.png",horizontal=True)
    
image helmet = "vfx/helmet_ad.png"                                         #Used for the final scene when the cockpit breaks.

image unumpromultisdabiturcaput  = "cg/bottomofthesea_ad.png"  

image hallway = "vfx/hallway_ad.png"

image explosion1 = "vfx/explode1_ad.png"
image explosion2 = "vfx/explode2_ad.png"
image door1 = "vfx/door1_ad.png"
image door2 = "vfx/door2_ad.png"


init:
    image appleblossumsspin = Animation("vfx/blossum_ad1.png", 0.6,
                                    "vfx/blossum_ad2.png", 0.4,
                                    "vfx/blossum_ad3.png", 0.6,
                                    "vfx/blossum_ad2.png", 0.4,
                                    "vfx/blossum_ad1.png", 0.6,
                                    "vfx/blossum_ad2.png", 0.4,
                                    "vfx/blossum_ad3.png", 0.4,
                                    "vfx/blossum_ad4.png", 0.4,
                                    "vfx/blossum_ad5.png", 0.4,
                                    "vfx/blossum_ad6.png", 0.4,
                                    "vfx/blossum_ad7.png", 0.4,
                                    "vfx/blossum_ad8.png", 0.4,)
image blossums1 = SnowBlossom("appleblossumsspin", count=7, border=100, xspeed=(-300, 300), yspeed=(50, 150), start=1, fast=True, horizontal=False)
image blossums3 = SnowBlossom("appleblossumsspin", count=4, border=100, xspeed=(-200, -400), yspeed=(-100, -150), start=1, fast=True, horizontal=False)
    
image wakingstatic = Animation("vfx/wakingstatic1_ad.png", 0.1,                 
                                "vfx/wakingstatic2_ad.png", 0.1,
                                "vfx/wakingstatic3_ad.png", 0.1,
                                "wakingstatic1v", 0.1,                 
                                "wakingstatic2v", 0.1,
                                "wakingstatic3v", 0.1,
                                "wakingstatic1h", 0.1,                 
                                "wakingstatic2h", 0.1,
                                "wakingstatic3h", 0.1)

image wakingstatic1v = im.Flip("vfx/wakingstatic1_ad.png", vertical=True)     
image wakingstatic2v = im.Flip("vfx/wakingstatic2_ad.png", vertical=True)
image wakingstatic3v = im.Flip("vfx/wakingstatic3_ad.png", vertical=True)
image wakingstatic1h = im.Flip("vfx/wakingstatic1_ad.png", horizontal=True)
image wakingstatic2h = im.Flip("vfx/wakingstatic2_ad.png", horizontal=True)
image wakingstatic3h = im.Flip("vfx/wakingstatic3_ad.png", horizontal=True)

image blurryvision = "vfx/blurryvision_ad.png"  

image budapestrise = "vfx/elysianghostbudapest_ad.png"
    
init:
    image appleblossumssway = Animation("vfx/blossum_ad1.png", 0.5,           
                                    "vfx/blossum_ad2.png", 0.5,
                                    "vfx/blossum_ad3.png", 0.5,
                                    "vfx/blossum_ad2.png", 0.5,)
image blossums2 = SnowBlossom("appleblossumssway", count=13, border=100, xspeed=(-300, 300), yspeed=(50, 150), start=1, fast=True, horizontal=False)
image blossums4 = SnowBlossom("appleblossumssway", count=4, border=100, xspeed=(-200, -400), yspeed=(-100, -150), start=1, fast=True, horizontal=False)


image watercresspalinurus = "vfx/watercresspalinurus.png"                  #Used as an alternate unlock screen after the game is completed

image dessertdream = "vfx/dessertdream_ad.png"  
image elysianclouds = "vfx/elysianclouds_ad.png"
image 2015 = "vfx/2015_ad.png"
image estars = SnowBlossom("vfx/elysianstar_ad.png", count=200, border=100, xspeed=(0, 0), yspeed= (-300, -300), start=1, fast=False, horizontal=False)
image departurestars = SnowBlossom("vfx/elysianstar_ad.png", count=100, border=10, xspeed=(1500, 1700), yspeed= (-300, -550), start=1, fast=False, horizontal=True)

image london = "vfx/london_ad.png"
image abbotsford = "vfx/abbotsford_ad.png"
image athens = "vfx/athens_ad.png"

image myanton1 = "vfx/alberta1_ad.png"
image myanton2 = "vfx/alberta2_ad.png"
image myanton3 = "vfx/alberta3_ad.png"
image myanton4 = "vfx/alberta4_ad.png"
image myanton5 = "vfx/alberta5_ad.png"

image shipcabinframe = "vfx/cabinwindowframe_ad.png"

image glare = SnowBlossom("vfx/glare_ad.png", count=13, border=100, xspeed=(-150, 150), yspeed=(50, -50), start=1, fast=True, horizontal=False)

image redcabin = "vfx/cabinredlight_ad.png"

# Applies transitions to all characters

init python:
    def callback_transition(event, interact=True, **kwargs):
        if event == "begin":
            renpy.transition(dissolve, layer="master")

    config.all_character_callbacks = [callback_transition]

# Game starts here
# Shortest scene ever

label start:

    jump scene1
