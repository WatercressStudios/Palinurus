label scene2:

    play music "music/meteorstorm.mp3"

    p "A debris storm...?"

    scene cabin
    with dissolve

    "I hurried back to my seat in the cabin to look out the window, squinting my eyes to see through the blackness of space."

    "I could make out a few sparkling lights... reflections? Yeah. Reflections."

    "The ship itself had bright, powerful lights attached to its wings, tail and under the cockpit, and every time they flashed I got a peek at some sort of approaching mass."

    scene meteoroids
    with dissolve

    "Meteoroids. Hundreds, maybe thousands of meteoroids, drifting aimlessly through space, clustered together in a school."

    "A relentless, soaring landslide of steel, on a direct collision course with the shuttle."

    p "..."

    "My heart sank deep down my stomach. Actually, no, it went past that."

    "Plummeted straight down to my bowels."

    b "No cause for alarm, alright? I've got it under control."

    p "No cause for alarm."

    b "No cause for alarm."

    scene cabin
    with dissolve

    "I repeated those words to myself, more incredulously each time."

    "I took a deep breath, steeling myself for what I feared was to come."
    
    show blink1:                                                                   ##Blink/ Eyes drooping VFX
        xpos 0.0 ypos -1.0
        linear 1.0 xpos 0.0 ypos -0.1
    show blink2:
        xpos 0.0 ypos 1.0
        linear 1.0 xpos 0.0 ypos 0.1
    with dissolve
    
    "Still as a statue, I closed my eyes, content not to watch it go down."

    b "... Oh, that's not good."

    "'Tap tap tap tap.'"

    "I could hear the sound of particles impacting the hull, the constant whine of ringing metal."

    "They started sparse, spread out..."

    "'Tap tap tap TAP TAP TAP TAP!'"

    "Only a few minutes ago, the cabin had been eerily silent, and now a constant stream of sound filled it, like we'd flown into the midst of a typhoon."

    "I could imagine the cold wind hitting my face; the fury of Old Earth."

    "I think it was a better coping mechanism. I'd rather be lost in a thunderstorm on a terrestrial surface than weathering a debris storm in a dingy old shuttle in one of the most remote parts of charted space."
    
    show blink1:                                                                   ##Blink/ Eyes drooping VFX
        xpos 0.0 ypos -0.1
        linear 1.0 xpos 0.0 ypos -0.5
    show blink2:
        xpos 0.0 ypos 0.1
        linear 1.0 xpos 0.0 ypos 0.5
    with dissolve
    
    "I winced, popping an eye open. A heavier rock pounded against the hull, and the ship lurched to one side."

    "It didn't seem like we'd sustained any serious damage yet, so I sat there, clenching my legs, wringing my hands in desperation, hoping the storm would soon pass."

    scene white with dissolve
    scene cabin with vpunch
    show cabin2:
        alpha 0.0
        linear 1.0 alpha 0.0
        linear 20.0 alpha 1.0
    show firedown:
        alpha 0.2
    "'Wham! Wham!'"

    "Like fists driven by fury and rage, the meteoroids continued to pound against the shuttle."

    "With each impact, the rocks dug into the hull, denting it and pushing against the cabin walls."

    "The flooring pressed against my legs as a large divot was suddenly formed. That was too close for comfort."

    "Another larger meteoroid ricocheted off the window I was seated next to. I flinched and writhed in my seat."

    b "Look, I've been through worse than this before, alright?"

    b "Way, way worse than this."

    b "I'm a veteran of the trade; an unsung hero in the artificial intelligence community, you know?"

    b "This is nothing that I can't handle, so-"

    scene meteoroids
    with dissolve

    b "..."

    p "..."

    b "Oh."

    p "... That's bad."

    "They came into sight. I saw enormous meteoroids, the heavy hitters of the storm, hurling themselves directly in our path. Even the awe-inspiring, holy light of the distant stars cowered in the shadow of the meteoroids."

    "One was on a due course for the cabin. It was a monstrous, gray, jagged mass that glistened devilishly, its iron deposits reflecting the flashing emergency lights of our ship."

    "It was going to impact, and it was going to impact very soon."

    scene cabin2 with dissolve
    scene black with Dissolve(0.1)
    scene cabin2 with Dissolve(0.1)
    scene black with Dissolve(0.1)
    scene cabin3 with vpunch
    show wakingstatic:
        alpha 0.2

    "I swallowed hard and lowered my hands to undo my harness. My hands shook thunderously; I couldn't get at the switches and belts."
    
    show dust:
        alpha 0.1
    show dust2:
        alpha 0.1
    show dust3:
        alpha 0.1

    "I tugged at the straps, but they only seemed to tighten."

    p "Come on... come on, God damn it!"
    
    show redcabin:
        alpha 0.1
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.1
        repeat

    "Before all the strength had been drained from my arms, the belts miraculously disengaged."

    b "Passenger-sir, you need to get into the cockpit."
    
    show sparks:
        alpha 0.8

    b "It's the most isolated part of the ship, and we can seal it if worst comes to worst."
    
    show sparks2

    b "... Oh, dear."

    b "You need to get here now!"
    
    scene black
    show cabin3:
        zoom 1.0 xalign 0.5 yalign 0.5
        linear 2.0 zoom 2.5
    show sparks3
    show sparks4
    with dissolve

    "I exhaled, deeply, and darted towards the cockpit."

    scene black with dissolve
    show sparks3
    show sparks4
    show explosion2 at Position (xalign = 0.5, yalign = 0.5):
        alpha 1.0 rotate 0 zoom 0.7
        linear 0.4 rotate 360
        repeat
    show explosion1 at Position (xalign = 0.5, yalign = 0.5):
        alpha 1.0 rotate 0 zoom 0.7
        linear 0.4 rotate -360
        repeat
    with vpunch
    
    "'CRASH!'"

    "Shrapnel and sparks flew everywhere, lighting up the world in a blaze of yellow and orange. The entire cabin swayed and shook, and the horrendous sound of metal sheets rending apart filled my ears."
    show door1 behind explosion2
    show door2 behind explosion2
    with Dissolve(2.0)
    
    scene cockpitemergency
    show door1 at Position (xalign = 0.5, yalign = 0.5):
        xpos 0.5 ypos 0.5
        linear 0.5 xpos 0.5 ypos 0.5
        linear 2.0 xpos -1.0 ypos 0.5
    show door2 at Position (xalign = 0.5, yalign = 0.5):
        xpos 0.5 ypos 0.5
        linear 0.5 xpos 0.5 ypos 0.5
        linear 2.0 xpos 2.0 ypos 0.5
    show sparks3
    show sparks4
    
    "I slammed into the cockpit door, opened it, let myself fall through, and then kicked it shut."

    scene cockpitemergency
    with dissolve

    "Scrambling over to the console, I sealed the cockpit door and engaged all the airlocks."

    "My breathing was frantic, my vision blurred."

    scene cockpitsideemergency
    show console warning

    "I was in a panic, when I saw the pale figure of the Navigator scrolling through monitors and screens and spreadsheets."

    "It comforted me, at least a little bit."

    p "That one was... especially bad. Damage report?"

    show console warningtalk

    b "The hull's been breached. You're lucky you got here in time, sir."

    show console warninglook

    "I took some time so settle in, trying to find my footing in the cockpit as the shuttle rumbled in the midst of the storm."

    show console warning

    "I paused; I felt an odd sensation where my hand was resting on the windshield. I drifted my eyes down to take a look..."
    
    show broken with dissolve

    "A hairline fracture along the window pane. My finger ran along the thin, narrow line formed in the ultra-hardened glass. The splintered patterns it formed were remarkable, but..."

    "I was paralyzed with terror."
    
    scene cockpitsideemergency
    show console worrylook
    with vpunch
    
    "Suddenly, another lurch forwards. Another large collision."
    

    p "Ack! Damn it!"

    show console worryyell

    b "Please sir, take the co-pilot's seat and strap in! It's dangerous to remain standing at this time!"

    scene cockpitemergency
    with dissolve

    "Receptive to the machine's goading, I staggered to my feet, watching my footing in the lopsided cockpit."

    "Eventually, I sank into the plushy co-pilot's seat to the the Navigator's right. I glanced over to her."

    show bud closedworryx

    p "Hey, Navigator. Quick question."

    show bud worryx

    p "How in the HELL did you not notice that mess of meteoroid bullshit heading our way?"

    show bud panic

    b "They didn't show up on the short-range radar! Their iron compound deposits absorbed the signals, is what I'm thinking. The storm came in too fast to be traced."

    show bud panicfrown

    "I paused. So there was nothing we could have done about it? The storm had just been drifting through space and had just... decided to ravage us in its wake?"

    "What the hell kind of freak accident..."

    show bud panicslight

    b "Are you alright, Passenger-sir? Are you hurt? That was a nasty beating you took..."

    show bud panicfrown

    "The program looked so concerned for me. Still rubbing my forehead, I waved its concerns off, groaning to myself."

    p "Yeah, I ought to be fine... nothing I can't handle. What are we going to do now?"

    show bud panicsquintx

    b "Well, our vessel's sustained critical damage, and we've been knocked considerably off course."

    show bud worryclosex

    b "Both the navigational and communications systems are completely off-line, and I haven't been able to find a way to repair them..."

    show bud neutralx

    b "But for now, we need to do something about the damage."

    show bud angrytalkx

    b "Right now, the rest of the ship is nothing but sheared, hulking mass, adding unnecessary weight."

    show bud angrytalk

    b "Preparations for jettisoning the cockpit are under way. We should be far removed from the storm in due time."

    show bud srsfaec

    p "Understood. Proceed as you should, Navigator."

    p "..."

    p "Wait, what?"

    p "Jettisoning the cockpit!?"

    show bud neutraltalk

    b "This transit shuttle is of an older model, sir, previously designed for two human pilots. In the case of emergency, the ship-maker installed a simple mechanism to eject the cockpit, which contains a lavatory and necessary supplies for emergency survival."

    b "It was essentially a primitive form of an escape pod, except roomier and less reliable."

    show bud normaltalkeyebrows

    b "Although I believe the jettison system of this craft is still in working order. I do maintain it, after all."

    "... What?"

    "Well, when I thought about it... it wasn't such a strange thing to phase out, now that pilots were almost always Navigators."

    "Even then, I was glad it wasn't phased out entirely. The age of the ship may very well have been what saved me in that moment."

    p "Okay, well, that sounds... doable."

    p "When are we going to be performing that jettison, exactly?"

    show bud closedworryx

    b "..."

    "H-hey! Don't clam up on me now..."

    show bud worrytalkx

    b "It's not a sure thing, but... I'll have to inspect our subsystems to see if it's still in working order."

    show bud worryx

    p "I thought you said it was still in working order?"

    show bud panicx

    b "It is!"

    show bud panicsquintx

    b "..."

    show bud worryyellhalfeye

    b "Probably."

    show bud worryneutralhalfeye

    "The machine... lied to me?"

    p "'Probably' doesn't really-"

    show bud neutraltalk

    b "I'm going to need to inspect the circuitry in order to fire up the launch mechanism."

    b "This system was hard-wired in, before the time of Navigators, so it hasn't been restructured in software like most everything else has."

    show bud worrysquintx

    "The AI turned to me, an apprehensive look in its soft eyes."

    show bud worrysquinttalkx

    b "It's, ah, pretty scary down there, so..."

    show bud panictalkx

    b "Watch out for me, passenger-sir?"

    show bud panicquietx

    "It doesn't sound particularly confident right now..."

    show bud weaksmile

    "The program bowed stiffly with a weak smile. That sinking feeling in my gut stirred again."

    p "H-hey! Don't talk like that! You're a Personal Navigator, aren't you?"

    show bud painfullook

    "The AI's eyes drifted up to mine, wide like a child peeking at a scolding parent."

    "For whatever reason, I couldn't bring myself to match her gaze. I looked off to the side."

    p "Er... I mean... do your best down there... I'm counting on you?"

    show bud painfullooksquint

    b "..."

    "The program stared back at me for a few painful moments, as if figuring something out in its mind. Its eyes were piercing, serious... in time, its eyebrows furrowed, a fiery look bursting into its irises."

    show bud srsfaectalk

    b "Understood. I'm going in. Make sure your harness is correctly secured, and I'll be back soon."

    show bud srsfaec

    "I nodded."

    "'Click!'"

    "That was the fastest I'd ever fastened my seat-straps."

    scene white

    "The AI's holographic display switched off in a flash of white light, and its cameras retracted back into the inner workings of the console."

    scene cockpitemergency
    with dissolve

    "In that moment, I was left to my own devices in the face of death. The cockpit was a closed room, a frame of steel and dura-glass, the only things separating the pilots from the harsh, hellish vacuum of space."

    "I looked out at the infinite expanse before me, the distant flickering stars."

    "'Boom!'"

    "I felt the ship rumble with the impact of another massive meteoroid. I shivered. Was I going to die here? Alone? In the infinite vastness of space..."

    "No one would care."

    "No one would ever find me."

    "Maybe I'd end up drifting out here forever."

    "That scared me more than anything else."

    "'...Rrrrr...'"

    "I felt my seat vibrate. My hands fell instinctively to clasp the armrests, attempting to keep myself steady."

    p "Argh!"

    "The entire room was shaking. I felt like the harnesses were about to rip apart."

    "'Kachunk!'"

    p "Oh, shit!"

    "And then, like a ragdoll, I was flung back into my seat, sinking further and further into the stiff leather."

    "I couldn't move my head; the pressure was too forceful. I simply started out the front of the cockpit as I saw it shoot forwards..."

    "We'd definitely just been jettisoned."

    p "... The cockpit is...!?"

    "Small pebbles pelted the windshield, but I didn't care."

    "I was ecstatic, laughing to myself in giddy joy. The way was clearing up! The program had managed it! We were going to make it! We-"

    "... We were about to hit another enormous meteoroid."

    scene black

    "'SLAM!'"

    jump scene3
