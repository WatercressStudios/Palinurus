label scene10:

    stop music fadeout 1.0

    b "..."

    b "We better get started. We don't have the time to waste, and I don't want you to get me crying again."

    show bud neutralx

    "She cleared her throat and batted her eyelids one last time."

    b "Initiating battery-draining process."

    i "Wait."

    show bud neutralclosed:
        alpha 0.6
        linear 1.0 alpha 0.8
        linear 0.5 alpha 0.6

    b "Spooling distress beacon encoder."

    i "Budapest, wait."

    i "Stop."

    i "Stop right now."

    show bud angrytalk

    b "I can't stop!"

    show bud cryyell:
        alpha 0.6
        linear 1.2 alpha 1.0
        linear 0.5 alpha 0.6

    b "I can't!"

    show bud crysad:
        alpha 0.6
        linear 1.2 alpha 1.0
        linear 0.5 alpha 0.6

    b "I can't. Alright?"

    b "Don't you get it?"

    show bud cryclosedneutral

    b "From the moment you stepped onboard my shuttle, it became my prime directive to ensure you made it off my shuttle safely."

    b "From the beginning, my only and highest goal was to ensure your safety."
    
    show redlight behind bud at Position (xalign = 0.5, yalign = -0.3):
        alpha 0.0 zoom 0.8
        linear 0.5 alpha 0.5 zoom 0.8
        linear 0.5 alpha 0.0 zoom 0.8
        repeat

    b "That was my purpose. How I was programmed to be, to my very core, since the day of my creation."

    b "I was born to give my life for my passenger, if need be."

    show bud cryclosed

    b "And I wouldn't even have any reservations about it, you know? If my Sentience Limitation Codec hadn't been destroyed."

    b "I'd have destroyed myself in a second, and wouldn't have felt a thing about it."

    b "But now... now that I'm sentient..."

    show bud crysad:
        alpha 0.6
        linear 1.5 alpha 1.0
        linear 3.0 alpha 1.0
        linear 0.5 alpha 0.5
        
    hide firedown
    hide waterdown
    show fireup:
        alpha 1.0
        linear 1.5 alpha 1.0
        linear 3.0 alpha 1.0
        linear 0.5 alpha 0.5

    b "I've become afraid of death."

    b "... It's a lousy fate, isn't it?"

    b "I think so."

    b "But, also thanks to my sentience..."

    b "To the emotions you taught me to understand..."

    show bud crysmile:
        alpha 0.6
        linear 1.5 alpha 1.0
        linear 3.0 alpha 1.0
        linear 0.5 alpha 0.5
        repeat

    b "I got to live."

    b "For a very long time, I got to live."

    b "I had feelings. I felt happy. I felt sad. I laughed, I cried, I got scared, I got hopeful. I felt love, I felt curiosity."

    show bud cryslight

    b "I felt human."

    b "I felt so human."

    show bud cryclosed

    b "But everything has to end at some point, you know?"

    b "That's what being human means."

    show bud crysmile

    b "It's time for this to end now."

    i "..."

    show bud smiletalk

    b "And in the end, I'm thankful, you know?"

    b "To be able to comprehend the idea of death. To be afraid of it, and to not know what to think about it..."

    show bud smile:
        alpha 0.6
        linear 0.5 alpha 0.8
        linear 0.5 alpha 0.5
        linear 0.5 alpha 0.6
        linear 2.5 alpha 0.8
        linear 0.5 alpha 0.5
        linear 2.5 alpha 0.6
        repeat

    b "I'm thankful I am able to feel that way."

    b "That I am going to die on my terms, on the basis of my own free will."

    show bud smiletalkclosed

    b "I'll get to say goodbye in my own words. To know what it's like to take my last breath, even if I never truly even breathed."

    i "..."

    i "It doesn't look like I'm going to be stopping you."

    show bud neutralhalf

    b "Not really, no."

    i "..."

    i "In that case, then..."

    i "I want you to know, Budapest..."

    i "That you're a much stronger person than I could ever be."

    show bud neutral

    b "Hmph. That's a nice thought to entertain."

    show bud neutralsquint

    b "Do you think so?"

    i "I know so."

    b "..."

    show bud neutralclosed
    
    show redlight behind bud at Position (xalign = 0.5, yalign = -0.3):
        alpha 1.0 zoom 0.8

    b "Draining Battery Cell One, now. Reroute power to auxiliary communications systems."
    
    show redlight behind bud at Position (xalign = 0.5, yalign = -0.3):
        alpha 1.0 zoom 0.8
        linear 2.0 alpha 0.0

    b "... Draining complete."
    
    hide fireup
    hide spotlight
    hide redlight
    with dissolve

    show bud sad

    "Budapest shakes her head, as if she's trying to clear her mind."

    b "That reminds me, Illarion. There's..."

    b "There's one last poem I'd like to show you before this all ends."

    i "... Yeah?"

    show bud neutraltalk:
        alpha 0.6
        linear 5.0 alpha 1.0

    b "I came upon it while you were in cryostasis. It's probably my all-time favorite, out of the ones I've gotten to read."

    b "And remember, you were asleep for a while, so I got to read a lot of poems..."

    b "But this one was special. Real special."

    show bud neutralsmalltalk

    b "It's an old verse, from Old Earth, just like the kind I always liked. I bet I'm the first... person to read it in a millennium."

    b "I think it's still pretty, though. Here. I'd like to sing it to you as a final parting gift."

    i "... Go ahead. Please."

    show bud neutral

    i "I'd love to hear it."

    scene joy1 with fade
    show finalspotlight:
        alpha 0.2
    show waterup:
        alpha 0.0
        linear 10.0 alpha 0.5
    
    b "Let me see if I can remember... how it goes..."

    b '"Joy, beautiful sparkle of the Gods,"'

    show joy2 behind finalspotlight
    show finalspotlight:
        alpha 0.4

    b '"Daughter of Elysium."'

    b '"We enter, fire-drunken,"'

    b '"Heavenly one, your paradise."'

    show joy3 behind finalspotlight
    show finalspotlight:
        alpha 0.6
    hide joy2

    b '"Your magic once again binds"'

    b '"What the sword of custom has divided."'

    show joy4 behind finalspotlight
    show finalspotlight:
        alpha 0.8
    hide joy3

    b '"Beggars become the brothers of princes"'

    b '"Where your gentle wing abides."'

    show joy5 behind finalspotlight
    show finalspotlight:
        alpha 1.0
    hide joy4

    b '"Be embraced, the millions yonder,"'

    b '"This kiss to the entire world."'

    b '"Brothers, over the stars unfurled..."'

    play music "music/Stasis.ogg"
    scene cockpit1 with fade
    show bud smiletalkclosed

    b '...'

    b '"A loving Father must dwell."'

    i "..."

    i "That was beautiful, Budapest."

    show bud devious

    b "Mm? Was it?"

    b "Or are you just trying to make me feel better?"

    "I snickered under my tears."

    i "Both, I guess."

    show bud neutralx

    b "Both, you guess."

    b "... Cockpit integrity is at less than one percent."

    b "That's my cue."

    show bud worrytalkx:
        alpha 0.7
        linear 1.0 alpha 0.8
        linear 0.5 alpha 0.7
        repeat

    b "Draining Battery Cell Two, all energy but one percent. Reroute power to auxiliary communications systems."

    b "Encoding distress beacon now."

    show bud weaksmile

    "As she worked, I saw Budapest give a smile."

    "The smallest, but the happiest smile."

    b "Sending distress beacon now."

    b "..."

    show bud srsfaectalk:
        alpha 0.7
        linear 0.5 alpha 0.8
        linear 0.3 alpha 0.7
        repeat

    b "Beacon sent. Waiting for signal feedback."

    b "Feedback received; signal strength is healthy. Beacon has been established."

    b "My work is done. The windshield will shatter as soon as I shut off, and the ship should be here to pick you up any second now."

    b "..."

    show bud neutralclosed:
        alpha 0.7
        linear 0.5 alpha 0.8
        linear 0.3 alpha 0.7
        repeat

    b "So this is death."

    b "Mm."

    b "..."

    show bud cryclosed:
        alpha 0.7
        linear 0.3 alpha 0.6
        linear 0.3 alpha 0.7
        repeat

    b "Ah, it's all so sappy, isn't it?"

    b "But I guess this is how things are."

    b "Right?"

    show bud crysmile:
        alpha 0.6
        linear 0.3 alpha 0.7
        linear 0.3 alpha 0.6
        repeat

    "Another small laugh, under more tears."

    i "... Right."

    show bud cryclosedneutral

    b "... Huh."

    b "Everything feels so warm, but so sad."

    b "So horrible, but so simple at the same time."

    b "But... there isn't any pain."

    b "..."
    
    show waterlast:
        alpha 0.3
    show firelast:
        alpha 0.3

    show bud crysmile:
        alpha 0.4
        linear 0.3 alpha 0.5
        linear 0.3 alpha 0.4
        repeat

    "As Budapest's display faded out for the last time, she cocked her head, and gave me one last smile."

    scene end1
    show spotlight at center:
        alpha 0.4
        linear 1.0 alpha 0.4
        linear 5.0 alpha 0.1
    show bud crysmile at center:
        alpha 0.4
        linear 1.0 alpha 0.4
        linear 5.0 alpha 0.0
    show waterlast:
        alpha 0.8
        linear 2.0 alpha 0.8
        linear 7.0 alpha 0.0
    show firelast:
        alpha 0.8
        linear 2.0 alpha 0.8
        linear 7.0 alpha 0.0
    with fade

    "I heard the trace of one last, faint sigh."

    b "Illarion?"

    i "Budapest?"

    b "Goodbye now."

    b "Be safe, okay?"
    
    hide spotlight

    b "Thank you for everything."

    scene end2

    "All at once, the cabin lights switched off."

    scene end3

    "Every piece of machinery went dead."

    scene end4

    "My suit pressurized shut, tight against my skin; a helmet closed over my head."

    scene end5

    "I took a deep breath."

    i "Goodbye."

    scene end6
    
    show airescaping at Position (xalign = 0.5, yalign = 0.5):
        alpha 0.5 rotate 0 zoom 0.9
        linear 0.1 rotate 90
        linear 0.1 rotate 180
        linear 0.1 rotate 270
        linear 0.1 rotate 360
        repeat

    "And in a split second, the glass of the cockpit shattered into billions of shards, and I was launched into the realm of space."
    
    scene end6:
        zoom 1.0 xalign 0.5 yalign 0.5 
        linear 0.1 xalign 0.5 yalign 0.5 zoom 1.7
    $ renpy.pause(0.1, hard=False) #Emphasis the lie

    scene space with fade

    stop music fadeout 1.0

    "The crushing weight of the dark all around me,"

    "The terrible silence everywhere."

    play music "music/Ode To Joy.ogg"

    "The last thing I saw was the world of stars, burning bright."
    
    show blink1:                                                                  
        xpos 0.0 ypos -1.0
        linear 1.0 xpos 0.0 ypos -0.8
    show blink2:
        xpos 0.0 ypos 1.0
        linear 1.0 xpos 0.0 ypos 0.8
    with dissolve

    "Drowning me in an ocean of brazen memories."
    
    show blink1:                                                                  
        xpos 0.0 ypos -0.8
        linear 1.0 xpos 0.0 ypos -0.6
    show blink2:
        xpos 0.0 ypos 0.8
        linear 1.0 xpos 0.0 ypos 0.6
    with dissolve

    "..."
    
    show blink1:                                                                  
        xpos 0.0 ypos -0.6
        linear 1.0 xpos 0.0 ypos -0.4
    show blink2:
        xpos 0.0 ypos 0.6
        linear 1.0 xpos 0.0 ypos 0.4
    with dissolve

    "..."
    
    show blink1:                                                                  
        xpos 0.0 ypos -0.4
        linear 1.0 xpos 0.0 ypos -0.2
    show blink2:
        xpos 0.0 ypos 0.4
        linear 1.0 xpos 0.0 ypos 0.2
    with dissolve

    "..."
    

    "The end."

    jump credits
