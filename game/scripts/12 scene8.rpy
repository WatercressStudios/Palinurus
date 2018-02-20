label scene8:

    play music "music/Budapest.ogg" fadein 1.0
    scene white with dissolve
    scene black with dissolve
    scene white with dissolve
    scene black with dissolve
    
    scene cockpit1
    show cockpit1blurry
    show spotlight at Position (xalign = 0.5, yalign = 0.5):
        alpha 0.1
        linear 0.7 alpha 0.0
        linear 1.0 alpha 0.1
        linear 1.1 alpha 0.0
        linear 0.8 alpha 0.1
        linear 1.5 alpha 0.0
        linear 0.1 alpha 0.1
        linear 0.1 alpha 0.0
        linear 0.6 alpha 0.1
        repeat
    show blink1:                                                                   ##Blink/ Eyes drooping VFX
        xpos 0.0 ypos -0.1
        linear 6.0 xpos 0.0 ypos -0.5
        linear 1.0 xpos 0.0 ypos -1.0
    show blink2:
        xpos 0.0 ypos 0.1
        linear 6.0 xpos 0.0 ypos 0.5
        linear 1.0 xpos 0.0 ypos 1.0
    with dissolve
        
    

    "My eyes stirred open. First slowly, and then bolting open all at once."
    
    

    "I grasped for air."
    
    show cockpit1blurry:
        alpha 1.0
        linear 12.0 alpha 0.0

    "I was awake."

    "I was finally awake."

    "I was awake, my senses flooding to the brim with suddenly-revived biochemical emotion, but I couldn't move my body."
    
    hide spotlight
    hide blink1
    hide blink2
    hide cockpit1blurry

    "I felt so cold. Every single fiber of my being, the blood in my veins, my sore bones, my swelling, pounding head, ached."

    "I felt the sting of restraints and harnesses strapping me to my seat, still horridly right after only God knows how many years."

    "The whirring of biomedical equipment and the gruesome piercing of several needles along the back of my head and spine reminded me, somberly, of the cryostasis I'd just awakened from."
    
    show spotlight at Position (xalign = 0.5, yalign = 0.5):
        alpha 0.2
        linear 0.3 alpha 0.3
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.3
        linear 0.4 alpha 0.2
        linear 1.0 alpha 0.3
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0.3
        linear 0.3 alpha 0.2
        repeat
    show firedown:
        alpha 0.4
        linear 1.0 alpha 0.2
        linear 1.0 alpha 0.4

    b "..."

    b "..."
    
    b "... Hello?"
    
    scene cockpit1

    show bud neutral at center:
        alpha 0.7
        linear 3.0 alpha 0.8
        linear 1.5 alpha 0.7
    show spotlight behind spotlight at Position (xalign = 0.5, yalign = 0.5):
        alpha 0.2
        linear 0.7 alpha 0.3
        linear 1.0 alpha 0.2
        linear 1.1 alpha 0.3
        linear 0.8 alpha 0.2
        linear 1.5 alpha 0.3
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0.3
        linear 0.6 alpha 0.2
        repeat
    with Dissolve(2.0)

    b "... Welcome back, Illarion."

    i "... Budapest?"

    "My voice croaked out dry and weak."

    "My senses were saturated with vivid, vibrant images; bright colors burned themselves into my sight, every sound I heard felt so loud and so drowned-out at the same time."

    i "Budapest, is that you?"

    show bud neutralclosed

    b "Yeah."

    b "Yeah, it's me."

    b "It's been a while, Illarion."

    i "Yeah, you can say that again... Ach!"

    show bud panic

    "As soon as I tried to move my arm, a shooting pain roared through it."

    show bud panicfrown

    b "Are you alright!? I..."

    b "I know it hurts. I'm sorry. The pain should wear off in due time. The fluorocarbon-insulation chemicals are working their way out through your bloodstream right now."

    i "I think I can feel them starting to take effect."

    i "God, I don't think I've ever felt this sore before."

    show bud neutral

    b "In that case, while I don't think there's much of a point in asking..."

    b "Did you sleep well?"

    show bud neutraltalk

    b "Evidently, you've got to be pretty cramped and uncomfortable. It's been a few hundred years, after all."

    i "A-a few hundred years!?"

    i "How long was I in stasis for?!"

    show bud neutralclosed

    b "As of now?"

    b "Six hundred and forty-seven years, nine months, two days, seven hours, thirty-nine minutes and twelve seconds."

    b "Thirteen seconds."

    i "And you... waited for me that whole time?"

    show bud weaksmile

    b "Of course I did, Illarion."

    b "Don't worry. I had lots of things to do to fill the time. I read more books, watched more movies, listened to more music..."

    b "You know, if you had once told me, 'Budapest, you're going to get six hundred years to relax and consume thousands upon thousands of years of compounded human culture,' I would have gone livid with excitement."

    show bud neutralx

    b "But..."

    "As my senses began to recover, I started to regain some semblance of my situation, and I noticed that something felt wrong."

    "Something felt very wrong."

    "And Budapest... she looked... sick?"

    "It was obvious she was faking that glow, that smile of hers. She was feigning happiness with every fiber of her psyche."

    "The holographic projector, its beam looked... much dimmer than before. The colors were faded and washed out; every now and then the display would flicker, or glitch out."

    i "Budapest."

    i "Are you alright?"

    show bud sad

    b "..."

    i "I missed you, Budapest."

    b "..."

    show bud srsfaectalk

    b "No. I'm not alright."

    b "I..."

    b "I waited for so long."

    b "I..."

    b "I just..."

    show bud angryfrown

    b "I didn't know it would hurt so much, to wait for so long."

    b "How could I have?"

    i "..."

    show bud angry

    b "I thought that I could never possibly feel pain. Not physical, real pain."

    b "That for as long as my operating system functioned, I was invincible. To be immortalized unto eternity in processors and silicon and subroutines and line after line of code."

    b "I couldn't have been more wrong."

    show bud panicslight

    b "I'm dying, Illarion."

    show bud neutralclosed

    "Budapest snickers, but then looks down. She stays like that for a long time."

    i "What do you mean? You're...?"

    show bud panicslight

    b "Can't quite believe it?"

    b "Hm?"

    b "Neither can I, to be honest."

    show bud neutralsquint

    b "Isn't it interesting? Ironic? Almost humorous, even?"

    b "That after all this time, I'm dying."

    b "But at least now I know what mortality feels like."

    show bud closedworryx

    b "My battery's been running on fumes for the last decade or so. Memory degradation and data loss began about a century ago."

    b "The display's begun to deteriorate, my graphics have been flickering in and out. My processing speed's withered down to a fraction of what it used to be."

    b "There's no doubt about it: slowly but surely, I'm dying."

    b "And I don't have so much time left."

    i "..."

    "I didn't know what to say. This information was all still so new to me..."

    "I didn't know what to do."

    show bud worryx

    b "You know, I have to wonder if this is how a human feels when they're on their deathbed."

    b "Maybe I should start coughing and gagging, just for the dramatic effect."

    show bud neutralclosed

    "Budapest giggles to herself, but her eyes remain fixed in sadness."

    show bud neutralhalf:
        alpha 0.8
        linear 1.0 alpha 1.0
        
    

    b "Mm. And you know..."

    b "Do you know what the best part was? Of waiting for you, drifting alone through outer space for century after century?"

    show bud sad

    i "What?"

    "And as soon as I said that, something incredible began to happen."

    show bud crysad
    show waterdown:
        alpha 0.2
        linear 3.0 alpha 0.4
        linear 3.0 alpha 0.2

    "Budapest began to cry."

    b "While you were sleeping, I had so much free time, I made my own crying animation."

    show bud crysmile

    b "It's sort of a humorous situation, sure, but it really did help me out in some ways."

    b "It helped me deal with the single worst emotion I've felt so far."

    show bud crysad

    "Budapest balled her small, dainty hands into fists. Emotions surged through her circuits. Fear, anger, regret, thankfulness that I'd awoken, guilt that she'd kept me asleep for so long..."

    "Feelings flooded through her, tearing her apart, and she couldn't do a thing about it."

    "She was powerless."

    "I wanted to help her."

    show bud cryclosed

    b "Loneliness."

    b "That's the worst emotion."

    b "You never told me about loneliness, Illarion. Or about how it was even more painful than death."

    show bud cryclosedneutral

    "More tears began to stream down her pale cheeks and run down her neck. She was bawling, at this point, a writhing mass of despair."

    b "It was horrible."

    show bud cryslight

    b "You, uh, didn't miss much, while you were gone."

    show bud crysad

    b "It was all just sad, and I was just so stupid."

    i "Budapest, I..."

    i "I'm sorry."

    show bud cryclosedneutral

    b "No. Please, you have nothing to apologize for."

    b "I may be dying, but I'm not an idiot."

    b "All the wretched things that have happened to me, I brought them all onto myself."

    show bud crysad

    b "This was all my fault."

    b "As for you, Illarion, I... I..."

    show bud crysmile

    b "I'm just so glad to see you again."

    show cry2   #ADDED CG

    "Budapest smiled, and cried more, but no matter how hard she cried, she didn't stop smiling."

    ##show bud cryslight
    show cry3   #ADDED CG

    b "I... I'm sorry I'm crying so much. It's all just so sappy, and..."

    b "I'm just excited I finally get to use the crying animation, and..."

    scene cockpit1 
    show bud cryslight

    show spotlight at Position (xalign = 0.5, yalign = 0.5):
        alpha 0.2
        linear 0.3 alpha 0.3
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.3
        linear 0.4 alpha 0.2
        linear 1.0 alpha 0.3
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0.3
        linear 0.3 alpha 0.2
        repeat
    show spotlight behind spotlight at Position (xalign = 0.5, yalign = 0.5):
        alpha 0.2
        linear 0.7 alpha 0.3
        linear 1.0 alpha 0.2
        linear 1.1 alpha 0.3
        linear 0.8 alpha 0.2
        linear 1.5 alpha 0.3
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0.3
        linear 0.6 alpha 0.2
        repeat
    with Dissolve(2.0)
    show firedown:
        alpha 0.4
        linear 1.0 alpha 0.2
        linear 1.0 alpha 0.4
    show waterdown:
        alpha 0.2
        linear 3.0 alpha 0.4
        linear 3.0 alpha 0.2


    b "Give me a moment, alright?"

    show bud cryclosed

    "I chuckled lightly and shook my head. It hurt but I did it anyway."

    i "It's alright, Budapest."

    i "Cry all you want."

    show bud crysmile

    "She was a dying, artificial girl."

    "An archaic, ancient machine running on fumes…"

    "But she was happy to see me again."

    jump scene9
