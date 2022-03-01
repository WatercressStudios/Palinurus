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
image budaconsad = im.Scale("cg/budaconsad.webp", 1280, 720) 
image earth = "cg/venus.webp"
#Additional
image bud angry                  = "sprites/bud_angry.webp"
image bud angryfrown             = "sprites/bud_angryfrown.webp"
image bud neutral                = "sprites/bud_neutral.webp"
image bud neutralclosed          = "sprites/bud_neutralclosed.webp"
image bud neutralhalf            = "sprites/bud_neutralhalf.webp"
image bud neutralsmalltalk       = "sprites/bud_neutralsmalltalk.webp"
image bud neutralsquint          = "sprites/bud_neutralsquint.webp"
image bud neutraltalk            = "sprites/bud_neutraltalk.webp"
image bud sad                    = "sprites/bud_sad.webp"
image bud shock                  = "sprites/bud_shock.webp"
image bud smile                  = "sprites/bud_smile.webp"
image bud smiletalk              = "sprites/bud_smiletalk.webp"
image bud smiletalkclosed        = "sprites/bud_smiletalkclosed.webp"
image bud closedworryx           = "sprites/bud_closedworryx.webp"
image bud worryx                 = "sprites/bud_worryx.webp"
image bud panic                  = "sprites/bud_panic.webp"
image bud panicfrown             = "sprites/bud_panicfrown.webp"
image bud panicslight            = "sprites/bud_panicslight.webp"
image bud panicsquintx           = "sprites/bud_panicsquintx.webp"
image bud worryclosex            = "sprites/bud_worryclosex.webp"
image bud neutralx               = "sprites/bud_neutralx.webp"
image bud angrytalkx             = "sprites/bud_angrytalkx.webp"
image bud angrytalk              = "sprites/bud_angrytalk.webp"
image bud srsfaec                = "sprites/bud_srsfaec.webp"
image bud normaltalkeyebrows     = "sprites/bud_normaltalkeyebrows.webp"
image bud worrytalkx             = "sprites/bud_worrytalkx.webp"
image bud panicx                 = "sprites/bud_panicx.webp"
image bud worryyellhalfeye       = "sprites/bud_worryyellhalfeye.webp"
image bud worryneutralhalfeye    = "sprites/bud_worryneutralhalfeye.webp"
image bud worrysquintx           = "sprites/bud_worrysquintx.webp"
image bud worrysquinttalkx       = "sprites/bud_worrysquinttalkx.webp"
image bud panictalkx             = "sprites/bud_panictalkx.webp"
image bud panicquietx            = "sprites/bud_panicquietx.webp"
image bud weaksmile              = "sprites/bud_weaksmile.webp"
image bud painfullook            = "sprites/bud_painfullook.webp"
image bud painfullooksquint      = "sprites/bud_painfullooksquint.webp"
image bud srsfaectalk            = "sprites/bud_srsfaectalk.webp"
image bud devious                = "sprites/bud_devious.webp"
image bud sassy                  = "sprites/bud_sassy.webp"
image bud panicquietx            = "sprites/bud_panicquietx.webp"
image bud excitedclosed          = "sprites/bud_excitedclosed.webp"
image bud excitedsmileclosed     = "sprites/bud_excitedsmileclosed.webp"
image bud shrugclosed            = "sprites/bud_shrugclosed.webp"
image bud neutraleyebrowsx       = "sprites/bud_neutraleyebrowsx.webp"
image bud blushstammer           = "sprites/bud_blushstammer.webp"
image bud panicquiet             = "sprites/bud_panicquiet.webp"
image bud neutralsilentx         = "sprites/bud_neutralsilentx.webp"
image bud bigsmileneutral        = "sprites/bud_bigsmileneutral.webp"
image bud bigsmile               = "sprites/bud_bigsmile.webp"
image bud stare                  = "sprites/bud_stare.webp"
image bud weaksmiletalksquint    = "sprites/bud_weaksmiletalksquint.webp"
image bud smirkx                 = "sprites/bud_smirkx.webp"
image bud worrysquinttalk        = "sprites/bud_worrysquinttalk.webp"
image bud neutralupx             = "sprites/bud_neutralupx.webp"
image bud depressedtalkx         = "sprites/bud_depressedtalkx.webp"
image bud depressedclosed        = "sprites/bud_depressedclosed.webp"
image bud depressedtalk          = "sprites/bud_depressedtalk.webp"
image bud shocktalk              = "sprites/bud_shocktalk.webp"
image bud painfullooktalk        = "sprites/bud_painfullooktalk.webp"
image bud worryclosetalk         = "sprites/bud_worryclosetalk.webp"
image bud surprise               = "sprites/bud_surprise.webp"
image bud surpriseneutral        = "sprites/bud_surpriseneutral.webp"
image bud surpriseneutraltalk    = "sprites/bud_surpriseneutraltalk.webp"
image bud smileup                = "sprites/bud_smileup.webp"
image bud bigsmileclosed         = "sprites/bud_bigsmileclosed.webp"
image bud stammer                = "sprites/bud_stammer.webp"
image bud neutralworry           = "sprites/bud_neutralworry.webp"
image bud awkwardblush           = "sprites/bud_awkwardblush.webp"
image bud awkwardblushtalk       = "sprites/bud_awkwardblushtalk.webp"
image bud blush                  = "sprites/bud_blush.webp"
image bud poutblush              = "sprites/bud_poutblush.webp"
image bud smileclosed            = "sprites/bud_smileclosed.webp"
image bud panicquiettalkx        = "sprites/bud_panicquiettalkx.webp"
image bud bigworryx              = "sprites/bud_bigworryx.webp"
image bud panicshout             = "sprites/bud_panicshout.webp"
image bud panicsquinttalkx       = "sprites/bud_panicsquinttalkx.webp"
image bud panicwincex            = "sprites/bud_panicwincex.webp"
image bud babbleclosed           = "sprites/bud_babbleclosed.webp"
image bud shametalk              = "sprites/bud_shametalk.webp"
image bud forcedsmirk            = "sprites/bud_forcedsmirk.webp"
image bud bigblush               = "sprites/bud_bigblush.webp"
image bud bigblushquiet          = "sprites/bud_bigblushquiet.webp"
image bud excitedtalk            = "sprites/bud_excitedtalk.webp"
image bud panicquiettalkx        = "sprites/bud_panicquiettalkx.webp"
image bud crysad                 = "sprites/bud_crysad.webp"
image bud crysing                = "sprites/bud_crysing.webp"
image bud cryslight              = "sprites/bud_cryslight.webp"
image bud crysmile               = "sprites/bud_crysmile.webp"
image bud cryyell                = "sprites/bud_cryyell.webp"
image bud cryclosed              = "sprites/bud_cryclosed.webp"
image bud cryclosedneutral       = "sprites/bud_cryclosedneutral.webp"
image bud embarrassed            = "sprites/bud_embarrassed.webp"
image bud sassyeyebrowsneutralx  = "sprites/bud_sassyeyebrowsneutralx.webp"
image bud sassyeyebrowsx         = "sprites/bud_sassyeyebrowsx.webp"
image bud devioussmilex          = "sprites/bud_devioussmilex.webp"
image bud silentsurprisex        = "sprites/bud_silentsurprisex.webp"
image bud awkwardchuckle         = "sprites/bud_awkwardchuckle.webp"
image bud neutralupthinkx        = "sprites/bud_neutralupthinkx.webp"
image bud smallsmile             = "sprites/bud_smallsmile.webp"
image bud panicquieterx          = "sprites/bud_panicquieterx.webp"
image bud lamentx                = "sprites/bud_lamentx.webp"
image bud sweetsmileclosed       = "sprites/bud_sweetsmileclosed.webp"
image bud sadsmilex              = "sprites/bud_sadsmilex.webp"
image bud sadsmile               = "sprites/bud_sadsmile.webp"
image bud worryyellhalfeyex      = "sprites/bud_worryyellhalfeyex.webp"
image bud worryyellhalfeyequietx = "sprites/bud_worryyellhalfeyequietx.webp"
image bud prodding               = "sprites/bud_prodding.webp"
image bud feisty                 = "sprites/bud_feisty.webp"
image bud smallsmileclosed       = "sprites/bud_smallsmileclosed.webp"
image bud nostalgic              = "sprites/bud_nostalgic.webp"
image bud peacefulsmile          = "sprites/bud_peacefulsmile.webp"
image bud blushsurprise          = "sprites/bud_blushsurprise.webp"
image bud blushcalming           = "sprites/bud_blushcalming.webp"
image bud shockx                 = "sprites/bud_shockx.webp"
image bud blushsmirk             = "sprites/bud_blushsmirk.webp"
image bud angryclosedx           = "sprites/bud_angryclosedx.webp"
image bud angryyellclosedx       = "sprites/bud_angryyellclosedx.webp"
image bud closeneutralx          = "sprites/bud_closeneutralx.webp"
image bud weaksmiletalk          = "sprites/bud_weaksmiletalk.webp"
image bud smilewarmclosed        = "sprites/bud_smilewarmclosed.webp"
image bud weaksmilesquint        = "sprites/bud_weaksmilesquint.webp"
image bud blushwarmsmile         = "sprites/bud_blushwarmsmile.webp"
image bud blushremember          = "sprites/bud_blushremember.webp"
image bud blushremembertalk      = "sprites/bud_blushremembertalk.webp"
image bud blushweaksmiletalk     = "sprites/bud_blushweaksmiletalk.webp"
image bud acceptance             = "sprites/bud_acceptance.webp"
image bud painfullookx           = "sprites/bud_painfullookx.webp"
image bud sassysmirkx            = "sprites/bud_sassysmirkx.webp"
image bud shrugneutralx          = "sprites/bud_shrugneutralx.webp"
image bud blushbigsurprise       = "sprites/bud_blushbigsurprise.webp"
image bud blushbigpanic          = "sprites/bud_blushbigpanic.webp"
image bud blushhalfx             = "sprites/bud_blushhalfx.webp"
image bud thinking               = "sprites/bud_thinking.webp"
image bud bigsmilex              = "sprites/bud_bigsmilex.webp"
image bud smilesquint            = "sprites/bud_smilesquint.webp"
image bud smilesquinttalk        = "sprites/bud_smilesquinttalk.webp"
image bud smileclosedcheery      = "sprites/bud_smileclosedcheery.webp"
image bud whateven               = "sprites/bud_whateven.webp"
image bud neutrallistening       = "sprites/bud_neutrallistening.webp"
image bud clarity                = "sprites/bud_clarity.webp"
image bud jawdropx               = "sprites/bud_jawdropx.webp"
image bud neutralsquinty         = "sprites/bud_neutralsquinty.webp"
image bud forcedsmirktalk        = "sprites/bud_forcedsmirktalk.webp"
image bud secondguessx           = "sprites/bud_secondguessx.webp"
image bud bigawkwardlaugh        = "sprites/bud_bigawkwardlaugh.webp"
image bud stumblex               = "sprites/bud_stumblex.webp"
image bud smilex                 = "sprites/bud_smilex.webp"
image bud smilesclosedcheery     = "sprites/bud_smilesclosedcheery.webp"

# Console Sprites
image console warningneutral       = "sprites/console_warningneutral.webp"
image console warningshout         = "sprites/console_warningshout.webp"
image console warningangryshout    = "sprites/console_warningangryshout.webp"
image console warningpause         = "sprites/console_warningpause.webp"
image console loreyelluplook       = "sprites/console_loreyelluplook.webp"
image console loreuplook           = "sprites/console_loreuplook.webp"
image console loremad              = "sprites/console_loremad.webp"
image console loremadlook          = "sprites/console_loremadlook.webp"
image console lorewarmsmilelook    = "sprites/console_lorewarmsmilelook.webp"
image console lorequestioninglook  = "sprites/console_lorequestioninglook.webp"
image console loreyelllook         = "sprites/console_loreyelllook.webp"
image console loresurprise         = "sprites/console_loresurprise.webp"
image console lorepaniclook        = "sprites/console_lorepaniclook.webp"
image console loreexcitelook       = "sprites/console_loreexcitelook.webp"
image console loreexcite           = "sprites/console_loreexcite.webp"
image console loreexcite2          = "sprites/console_loreexcite2.webp"
image console loreexcite3          = "sprites/console_loreexcite3.webp"
image console loresmile            = "sprites/console_loresmile.webp"
image console loresmilelook        = "sprites/console_loresmilelook.webp"
image console loretalk             = "sprites/console_loretalk.webp"
image console loretalklook         = "sprites/console_loretalklook.webp"
image console ameliasmilelook      = "sprites/console_ameliasmilelook.webp"
image console lorechat             = "sprites/console_lorechat.webp"
image console loadworrylook        = "sprites/console_loadworrylook.webp"
image console load                 = "sprites/console_load.webp"
image console loadworry            = "sprites/console_loadworry.webp"
image console loadup               = "sprites/console_loadup.webp"
image console loadfocus            = "sprites/console_loadfocus.webp"
image console warningsoftsmilelook = "sprites/console_warningsoftsmilelook.webp"
image console warningsoftsmiletalk = "sprites/console_warningsoftsmiletalk.webp"
image console talklook             = "sprites/console_talklook.webp"
image console smile                = "sprites/console_smile.webp"
image console talk                 = "sprites/console_talk.webp"
image console smileeyebrowslook    = "sprites/console_smileeyebrowslook.webp"
image console warning              = "sprites/console_warning.webp"
image console warningtalk          = "sprites/console_warningtalk.webp"
image console warninglook          = "sprites/console_warninglook.webp"
image console warningeyebrow       = "sprites/console_warningeyebrow.webp"
image console warningworry         = "sprites/console_warningworry.webp"
image console warningsmile         = "sprites/console_warningsmile.webp"
image console warningsmilelook     = "sprites/console_warningsmilelook.webp"
image console worrylook            = "sprites/console_worrylook.webp"
image console warningworrytalk     = "sprites/console_warningworrytalk.webp"
image console lorelook             = "sprites/console_lorelook.webp"
image console worryyell            = "sprites/console_worryyell.webp"

##################
# BG Declaration #
##################
image black                = "#000"
image white                = "#FFF"
image cockpit              = "bg/cockpit.webp" # Cockpit with transparent surface
image cockpithangar        = "bg/cockpithangar.webp"
image cockpit1             = "bg/cockpit1.webp" # Cockpit in Scenes 1-4 and 7-10
image cockpit2             = "bg/cockpit2.webp" # Cockpit in Scene 5 Parts 1-3
image cockpit3             = "bg/cockpit3.webp" # Cockpit in Scene 5 Parts 4-5
image cockpit4             = "bg/cockpit4.webp" # Cockpit in Scene 6
image space                = "bg/space.webp"
image cockpitside          = "bg/cockpitside.webp"
image cockpitsidehangar    = "bg/cockpitsidehangar.webp"
image station              = "bg/station.webp"
image shuttle              = "bg/shuttle.webp"
image cabin                = "bg/cabin.webp"
image cockpitemergency     = "bg/cockpitemergency.webp"
image cockpitsideemergency = "bg/cockpitsideemergency.webp"
image meteoroids           = "bg/meteoroids.webp"
image cabinfire            = "bg/cabinfire.webp"
image cockpitblackout      = "bg/cockpitblackout.webp"
image nebula               = "bg/nebula.webp"

image blackocean1          = "bg/blackocean1_ad.webp"   
image blackocean2          = "bg/blackocean2_ad.webp"   
image blackocean3          = "bg/blackocean3_ad.webp"   
image blackocean4          = "bg/blackocean4_ad.webp"  
image capepalinuro         = "bg/capepalinuro_ad.webp"
image shuttle              = "bg/palinurushanger_ad.webp"
image cabin                = "bg/shipcabin1_ad.webp"
image cabin2                = "bg/shipcabin2_ad.webp"
image cabin3                = "bg/shipcabin3_ad.webp"
image offwhite             = "#A9A9A9"
image offred               = "#2F0D0D"
image stationdeparture     = "bg/mirabellestation window_ad.webp"
image sleepingpassenger    = "bg/sleepingpassenger_ad.webp"


###################
# Anniversary CGs #
###################
# These are under init so that they are loaded when the game starts, so they can be accessed from
# the gallery
init:

    image blush                    = "cg/blush.webp" #Added
    image budablush                = "cg/budablush.webp" #Added
    image budablush2               = "cg/budablush2.webp" #Added
    image budablush3               = "cg/budablush3.webp" #Added
    image budablush4               = "cg/budablush4.webp" #Added
    image budablush5               = "cg/budablush5.webp" #Added
    image budaproud                = "cg/budaproud.webp" #Added
    image budasmile1               = "cg/budasmile.webp" #Added
    image budasmile2               = "cg/budasmile2.webp" #Added
    image budaspeak                = "cg/budaspeak.webp" #Added
    image dream                    = im.Scale("cg/dream.webp", 1280, 720) 
    image end1                     = "cg/end1.webp" #Added
    image end2                     = "cg/end2.webp" #Added
    image end3                     = "cg/end3.webp" #Added
    image end4                     = "cg/end4.webp" #Added
    image end5                     = "cg/end5.webp" #Added
    image end6                     = "cg/end6.webp" #Added
    image hours                    = "cg/hours.webp" #Added
    image hug                      = "cg/hug.webp" #Added
    image initialization           = "cg/initialization.webp" #Added
    image prestasisangry           = "cg/prestasisangry.webp" #Added
    image prestasisworried         = "cg/prestasisworried.webp" #Added
    image prestasisworriedspeaking = "cg/prestasisworriedspeaking.webp" #Added
    image joy1                     = "cg/Redo 1.webp" #Added
    image joy2                     = "cg/Redo 2.webp" #Added
    image joy3                     = "cg/Redo 3.webp" #Added
    image joy4                     = "cg/Redo 4.webp" #Added
    image joy5                     = "cg/Redo 5.webp" #Added
    image sing1                    = "cg/Sing.webp" #Added
    image sing2                    = "cg/sing2.webp" #Added
    image surprised                = "cg/surprised.webp" #Added
    
    image singingdreamgirl         = "cg/singingdreamgirl_ad.webp"
    image starhands                = "cg/handsofstars_ad.webp"
    image silouettebudapest        = "cg/silouettebudapest_ad.webp"
    image broken                   = "cg/crackedwindshield_ad.webp"


    # Art Gallery Images
    image art1    = "cg/artgal/001.webp"
    image art2    = "cg/artgal/002.webp"
    image art3    = "cg/artgal/003.webp"
    image art3p2  = "cg/artgal/003-2.webp"
    image art3p3  = "cg/artgal/003-3.webp"
    image art3p4  = "cg/artgal/003-4.webp"
    image art3p5  = "cg/artgal/003-5.webp"
    image art3p6  = "cg/artgal/003-6.webp"
    image art3p7  = "cg/artgal/003-7.webp"
    image art4    = "cg/artgal/004.webp"
    image art5    = "cg/artgal/005.webp"
    image art5p2  = "cg/artgal/005-2.webp"
    image art5p3  = "cg/artgal/005-3.webp"
    image art6    = "cg/artgal/006.webp"
    image art7    = "cg/artgal/007.webp"
    image art8    = "cg/artgal/008.webp"
    image art9    = "cg/artgal/009.webp"
    image art10   = "cg/artgal/010.webp"
    image art10p2 = "cg/artgal/010-2.webp"
    image art10p3 = "cg/artgal/010-3.webp"
    image art11   = "cg/artgal/011.webp"
    image art12   = "cg/artgal/012.webp"
    image art12p2 = "cg/artgal/012-2.webp"
    image art13   = "cg/artgal/013.webp"
    image art14   = "cg/artgal/014.webp"
    image art14p2 = "cg/artgal/014-2.webp"
    image art14p3 = "cg/artgal/014-3.webp"
    image art14p4 = "cg/artgal/014-4.webp"
    image art14p5 = "cg/artgal/014-5.webp"
    image art14p6 = "cg/artgal/014-6.webp"
    image art15   = "cg/artgal/015.webp"
    image art15p2 = "cg/artgal/015-2.webp"
    image art15p3 = "cg/artgal/015-3.webp"
    image art16   = "cg/artgal/016.webp"
    image art17   = "cg/artgal/017.webp"
    image art17p2 = "cg/artgal/017-2.webp"
    image art17p3 = "cg/artgal/017-3.webp"
    image art17p4 = "cg/artgal/017-4.webp"
    image art17p5 = "cg/artgal/017-5.webp"
    image art18   = "cg/artgal/018.webp"
    image art18p2 = "cg/artgal/018-2.webp"
    image art18p3 = "cg/artgal/018-3.webp"
    image art18p4 = "cg/artgal/018-4.webp"
    image art18p5 = "cg/artgal/018-5.webp"
    image art18p6 = "cg/artgal/018-6.webp"
    image art19   = "cg/artgal/019.webp"
    image art19p2 = "cg/artgal/019-2.webp"
    image art20   = "cg/artgal/020.webp"
    image art21   = "cg/artgal/021.webp"
    image art22   = "cg/artgal/022.webp"
    image art23   = "cg/artgal/023.webp"
    image art24   = "cg/artgal/024.webp"
    image art25   = "cg/artgal/025.webp"

#######
# VFX #
#######
image watercress = "vfx/watercress.webp"

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
    
image blackoceanlight = "vfx/blackoceanlight_ad.webp" #Used during the dream sequence as a blinking white light.

image blackoceanrain1 = "vfx/blackoceanrain1_ad.webp" #Black rain for your nightmare oceans    
image blackrain = SnowBlossom("blackoceanrain1", count=20, border=50, xspeed=(50, -50), yspeed=(1500, 1750), start=0, fast=True, horizontal=False)

image blackoceanrain2 = "vfx/blackoceanrain2_ad.webp" #Lighter rain for when the ocean consumes you   
image lightrain = SnowBlossom("blackoceanrain2", count=20, border=50, xspeed=(250, -250), yspeed=(1400, 1800), start=0, fast=True, horizontal=False)

image redrecoloredrain = im.Recolor("vfx/blackoceanrain2_ad.webp", 139, 0, 0, 255)
image bloodrain = SnowBlossom("redrecoloredrain", count=7, border=50, xspeed=(0, 0), yspeed=(1600, 2000), start=0, fast=True, horizontal=False)

image bubble1 = "vfx/bubble1_ad.webp" #Bubbles used during dream sequence  
image bubbles1 = SnowBlossom("bubble1", count=20, border=50, xspeed=(500, -500), yspeed=(-1400, -1800), start=0, fast=True, horizontal=False)
image bubbles2 = SnowBlossom("bubble1", count=10, border=50, xspeed=(500, -500), yspeed=(-900, -1200), start=0, fast=True, horizontal=False)

image spray = "vfx/spray_ad.webp" #Easiest Animation ever.
image sprayeffect = SnowBlossom("spray", count=20, border=50, xspeed=(1500, -1500), yspeed=(-900, -1000), start=0, fast=True, horizontal=False)
image dust = SnowBlossom("spray", count=10, border=10, xspeed=(-50, -125), yspeed=(50, 100), start=0, fast=True, horizontal=False)
image dust2 = SnowBlossom("spray", count=10, border=10, xspeed=(-50, 50), yspeed=(50, 70), start=0, fast=True, horizontal=False)
image dust3 = SnowBlossom("spray", count=50, border=10, xspeed=(1000, -1000), yspeed=(1000, -1000), start=0, fast=True, horizontal=False)

image blink movie = Movie(channel="blink", play="vfx/budapestblinking.m2t")     #Animation/Movie clip of  Budapest blinking during the protagonist's dream sequence



image freezing1 = "vfx/freezingeffect1_ad.webp"                          #Used for when Budapest administers the cyrostasis on the protagonist
image freezing2 = "vfx/freezingeffect2_ad.webp"
image needles = "vfx/needles_ad.webp"

image life1 = im.Recolor("vfx/freezingeffect1_ad.webp", 168, 0, 0, 255)
image life2 = im.Recolor("vfx/freezingeffect2_ad.webp", 118, 6, 6, 255)


image redlight = "vfx/redlight_ad.webp"                                  #Annoying red light, used in various scenes as a warning light
                             
image greenlight = "vfx/greenlight_ad.webp"      #Used once when Budapest fixes te various errors popping up



image spotlight = "vfx/spotlight_ad.webp"                                #Used for various scenes of Budapest appearing and reappearing as a subtle effect

image redscreens = "vfx/redscreens_ad.webp"                              #Red error screens used for after asteroid sequence.

image map1 = "vfx/cyclemaps1_ad.webp"                                    #Maps 1-3 are used for an animation, the 4th one is supposed to be the image with the 'Space Station'
image map2 = "vfx/cyclemaps2_ad.webp"
image map3 = "vfx/cyclemaps3_ad.webp"
image map4 = "vfx/cyclemaps4_ad.webp"

image starslongtrip = "vfx/starspalinurus_ad.webp"                       #Upon learning of their perdicament, the protagonist and Budapest look to the stars, this is used during that scene
image starsgazing = "vfx/starspalinurus2_ad.webp"
image blink1 = Image("vfx/blink_ad.webp",)
image blink2 = im.Flip("vfx/blink_ad.webp", vertical=True,)              #Used for blinking/eyes closing animations, mirrored to save space

init:
    image mapchecks = Animation("vfx/cyclemaps1_ad.webp", 0.1,           #Animation of Budapest flipping through star maps rapidly    
                                "vfx/cyclemaps2_ad.webp", 0.1,
                                "vfx/cyclemaps3_ad.webp", 0.1,)
    
init:
    image rebootscreens = Animation("vfx/reboot1_ad.webp", 0.05,         #Green flickering screens after the asteroid scene when the computer reboots and before Budapest reappears
                                    "vfx/reboot2_ad.webp", 0.05,
                                    "vfx/reboot3_ad.webp", 0.05,
                                    "vfx/reboot4_ad.webp", 0.05,)
    
image blackoceancorner1 = "vfx/blackoceancorner1_ad.webp"
image blackoceancorner2 = "vfx/blackoceancorner2_ad.webp"

image darkclouds = "vfx/darkdreamclouds_ad.webp"
image stormclouds = im.MatrixColor("vfx/darkdreamclouds_ad.webp", im.matrix.invert())

image budapestcorner = "vfx/budapestcorner_ad.webp"

image budapestcity1 = "vfx/budapestcity1_ad.webp"
image budapestcity2 = "vfx/budapestcity2_ad.webp"
image budapestcity3 = "vfx/budapestcity3_ad.webp"
image budapestcityzoom = "vfx/budapestzoom_ad.webp"

image departlights = "vfx/departurelights_ad.webp"

image sparkstrip = anim.Filmstrip("vfx/sparks_ad.webp", (4,4), (1,500), 0.01) 
image sparks = SnowBlossom("sparkstrip", count=30, border=5, xspeed=(-300, 300), yspeed=(1300, 800), start=10, fast=True, horizontal=False)
image sparks2 = SnowBlossom("firefilmstrip", count=50, border=5, xspeed=(-300, 300), yspeed=(1000, 800), start=10, fast=True, horizontal=False)
image sparks3 = SnowBlossom("sparkstrip", count=30, border=5, xspeed=(-500, 500), yspeed=(1300, 2300), start=10, fast=True, horizontal=False)
image sparks4 = SnowBlossom("firefilmstrip", count=50, border=5, xspeed=(-500, 500), yspeed=(1000, 2300), start=10, fast=True, horizontal=False)
    
image firefilmstrip = anim.Filmstrip("vfx/fire.webp", (2,2), (1,250), 0.1) 
image firedown = SnowBlossom("firefilmstrip", count=30, border=30, xspeed=(-150, 150), yspeed=(25, 75), start=10, fast=True, horizontal=True)           #Red Particle effects for Budapest
image fireup = SnowBlossom("firefilmstrip", count=70, border=4, xspeed=(-1500, 1500), yspeed=(-250, -500), start=10, fast=True, horizontal=False)
image firelast = SnowBlossom("firefilmstrip", count=70, border=4, xspeed=(-1500, 1500), yspeed=(250, 500), start=10, fast=True, horizontal=False)

image waterfilmstrip = anim.Filmstrip("vfx/water.webp", (2,2), (1,250), 0.1) 
image waterdown = SnowBlossom("waterfilmstrip", count=10, border=4, xspeed=(-150, 150), yspeed=(25, 75), start=10, fast=True, horizontal=True)                 #Blue Particle  effects for Budapest
image waterup = SnowBlossom("waterfilmstrip", count=70, border=4, xspeed=(-1500, 1500), yspeed=(-250, -500), start=10, fast=True, horizontal=False)
image waterlast = SnowBlossom("waterfilmstrip", count=70, border=4, xspeed=(-1500, 1500), yspeed=(250, 500), start=10, fast=True, horizontal=False)

image cockpit1blurry = "vfx/cockpit1blurry.webp"                            #Used during the final scenes when the protagonist wakes from his slumber

image finalspotlight = "vfx/finalspotlight_ad.webp"

image map zoom1 = "vfx/zoommaps1_ ad.webp"                                  #Used for when Budapest shows the protagonist the space maps
image map zoom2 = "vfx/zoommaps2_ ad.webp"
image map zoom3 = "vfx/zoommaps3_ ad.webp"
image map zoom4 = "vfx/zoommaps4_ ad.webp"

image dreamhands = "vfx/starhands_ad.webp"

image airescaping = "vfx/airescaping_ad.webp"

image osb 1 = "vfx/osreboot1_ad.webp"                                       #Used for the scene of the computer rebooting and before Budapest reappears
image osb 2 = "vfx/osreboot2_ad.webp"
image osb 3 = "vfx/osreboot3_ad.webp"
image osb 4 = "vfx/osreboot4_ad.webp"
image osb 5 = "vfx/osreboot5_ad.webp"
image osb 6 = "vfx/osreboot6_ad.webp"
image osb 7 = "vfx/osreboot7_ad.webp"
image osb 8 = "vfx/osreboot8_ad.webp"
image osb 9 = "vfx/osreboot9_ad.webp"

image pole1 = SnowBlossom("vfx/pole_ad.webp", count=6, border=30, xspeed=(-450, 450), yspeed=(1000, 1200), start=1, fast=True, horizontal=False)
image redrocks = SnowBlossom("vfx/redrock_ad.webp", count=3, border=30, xspeed=(-500, 500), yspeed=(1000, 1200), start=1, fast=True, horizontal=False)
init:
    image emotionaleyes = Animation("vfx/emoeyes1_ad.webp", 0.05,           #Subtle glint when Budapest loses part of herself; her eyes glint upon the mention of "Emotion"
                                    "vfx/emoeyes2_ad.webp", 0.05,
                                    "vfx/emoeyes3_ad.webp", 0.05,
                                    "vfx/emoeyes4_ad.webp", 0.05,
                                    "vfx/emoeyes5_ad.webp", 0.05,
                                    "vfx/emoeyes6_ad.webp", 0.05,
                                    "vfx/emoeyes7_ad.webp", 0.05,)
    
init:
    image shipflight = Animation("vfx/shipwarp1_ad.webp", 0.1,           #Subtle glint when Budapest loses part of herself; her eyes glint upon the mention of "Emotion"
                                    "vfx/shipwarp2_ad.webp", 0.1,
                                    "vfx/shipwarp3_ad.webp", 0.1,
                                    "vfx/shipwarp4_ad.webp", 0.1,
                                    "shipwarp5", 0.1,
                                    "shipwarp6", 0.1,
                                    "shipwarp7", 0.1,
                                    "shipwarp8", 0.1,)
    
init:
    image filmgrains = Animation("vfx/filmgrain1_ad.webp", 0.05,           #Subtle glint when Budapest loses part of herself; her eyes glint upon the mention of "Emotion"
                                    "vfx/filmgrain2_ad.webp", 0.05,
                                    "vfx/filmgrain3_ad.webp", 0.05,
                                    "vfx/filmgrain4_ad.webp", 0.05,
                                    "vfx/filmgrain5_ad.webp", 0.05,
                                    "vfx/filmgrain6_ad.webp", 0.05,)
    
image desertsky = "vfx/deserthorizon_ad.webp"

image emptypod = "vfx/stasispod_ad.webp"

image budapestface = "vfx/facezoom_ad.webp"
    
image shipwarp5 = im.Flip("vfx/shipwarp1_ad.webp",horizontal=True)
image shipwarp6 = im.Flip("vfx/shipwarp2_ad.webp",horizontal=True)
image shipwarp7 = im.Flip("vfx/shipwarp3_ad.webp",horizontal=True)
image shipwarp8 = im.Flip("vfx/shipwarp4_ad.webp",horizontal=True)
    
image helmet = "vfx/helmet_ad.webp"                                         #Used for the final scene when the cockpit breaks.

image unumpromultisdabiturcaput  = "cg/bottomofthesea_ad.webp"  

image hallway = "vfx/hallway_ad.webp"

image explosion1 = "vfx/explode1_ad.webp"
image explosion2 = "vfx/explode2_ad.webp"
image door1 = "vfx/door1_ad.webp"
image door2 = "vfx/door2_ad.webp"


init:
    image appleblossumsspin = Animation("vfx/blossum_ad1.webp", 0.6,
                                    "vfx/blossum_ad2.webp", 0.4,
                                    "vfx/blossum_ad3.webp", 0.6,
                                    "vfx/blossum_ad2.webp", 0.4,
                                    "vfx/blossum_ad1.webp", 0.6,
                                    "vfx/blossum_ad2.webp", 0.4,
                                    "vfx/blossum_ad3.webp", 0.4,
                                    "vfx/blossum_ad4.webp", 0.4,
                                    "vfx/blossum_ad5.webp", 0.4,
                                    "vfx/blossum_ad6.webp", 0.4,
                                    "vfx/blossum_ad7.webp", 0.4,
                                    "vfx/blossum_ad8.webp", 0.4,)
image blossums1 = SnowBlossom("appleblossumsspin", count=7, border=100, xspeed=(-300, 300), yspeed=(50, 150), start=1, fast=True, horizontal=False)
image blossums3 = SnowBlossom("appleblossumsspin", count=4, border=100, xspeed=(-200, -400), yspeed=(-100, -150), start=1, fast=True, horizontal=False)
    
image wakingstatic = Animation("vfx/wakingstatic1_ad.webp", 0.1,                 
                                "vfx/wakingstatic2_ad.webp", 0.1,
                                "vfx/wakingstatic3_ad.webp", 0.1,
                                "wakingstatic1v", 0.1,                 
                                "wakingstatic2v", 0.1,
                                "wakingstatic3v", 0.1,
                                "wakingstatic1h", 0.1,                 
                                "wakingstatic2h", 0.1,
                                "wakingstatic3h", 0.1)

image wakingstatic1v = im.Flip("vfx/wakingstatic1_ad.webp", vertical=True)     
image wakingstatic2v = im.Flip("vfx/wakingstatic2_ad.webp", vertical=True)
image wakingstatic3v = im.Flip("vfx/wakingstatic3_ad.webp", vertical=True)
image wakingstatic1h = im.Flip("vfx/wakingstatic1_ad.webp", horizontal=True)
image wakingstatic2h = im.Flip("vfx/wakingstatic2_ad.webp", horizontal=True)
image wakingstatic3h = im.Flip("vfx/wakingstatic3_ad.webp", horizontal=True)

image blurryvision = "vfx/blurryvision_ad.webp"  

image budapestrise = "vfx/elysianghostbudapest_ad.webp"
    
init:
    image appleblossumssway = Animation("vfx/blossum_ad1.webp", 0.5,           
                                    "vfx/blossum_ad2.webp", 0.5,
                                    "vfx/blossum_ad3.webp", 0.5,
                                    "vfx/blossum_ad2.webp", 0.5,)
image blossums2 = SnowBlossom("appleblossumssway", count=13, border=100, xspeed=(-300, 300), yspeed=(50, 150), start=1, fast=True, horizontal=False)
image blossums4 = SnowBlossom("appleblossumssway", count=4, border=100, xspeed=(-200, -400), yspeed=(-100, -150), start=1, fast=True, horizontal=False)


image watercresspalinurus = "vfx/watercresspalinurus.webp"                  #Used as an alternate unlock screen after the game is completed

image dessertdream = "vfx/dessertdream_ad.webp"  
image elysianclouds = "vfx/elysianclouds_ad.webp"
image 2015 = "vfx/2015_ad.webp"
image estars = SnowBlossom("vfx/elysianstar_ad.webp", count=200, border=100, xspeed=(0, 0), yspeed= (-300, -300), start=1, fast=False, horizontal=False)
image departurestars = SnowBlossom("vfx/elysianstar_ad.webp", count=100, border=10, xspeed=(1500, 1700), yspeed= (-300, -550), start=1, fast=False, horizontal=True)

image london = "vfx/london_ad.webp"
image abbotsford = "vfx/abbotsford_ad.webp"
image athens = "vfx/athens_ad.webp"

image myanton1 = "vfx/alberta1_ad.webp"
image myanton2 = "vfx/alberta2_ad.webp"
image myanton3 = "vfx/alberta3_ad.webp"
image myanton4 = "vfx/alberta4_ad.webp"
image myanton5 = "vfx/alberta5_ad.webp"

image shipcabinframe = "vfx/cabinwindowframe_ad.webp"

image glare = SnowBlossom("vfx/glare_ad.webp", count=13, border=100, xspeed=(-150, 150), yspeed=(50, -50), start=1, fast=True, horizontal=False)

image redcabin = "vfx/cabinredlight_ad.webp"

########################
# Added by InstantRiot #
########################

image budastareout = im.Scale("cg/budastareout.webp", 1280, 720)
image cry1 = im.Scale("cg/Cry1.webp", 1280, 720) 
image cry2 = im.Scale("cg/Cry2.webp", 1280, 720)
image cry3 = im.Scale("cg/Cry3.webp", 1280, 720)
image smilescene6 = im.Scale("cg/budascene6.webp", 1280, 720) 

image cryglitch = Animation("cry2", 0.5,                 
                                "cry3", 0.5)

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
