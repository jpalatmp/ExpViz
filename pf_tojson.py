import re
import json

def convert_to_json(script):
    # Remove leading and trailing whitespaces
    script = script.strip()

    # Split the script into talk turns
    talk_turns = re.split(r'\n\n\s*', script)

    json_output = {
        "talk_turns": [],
        "conversation_id": "121",
        "include_conversation": True,
        "include_suggestions": True,
        "include_tips": True,
        "include_definitions": True
    }

    for turn in talk_turns:
        # Extract speaker and dialogue
        match = re.match(r'^\s*([A-Z]+)\s+(.+)', turn, re.DOTALL)
        if match:
            speaker_id = match.group(1).strip()
            dialogue = match.group(2).strip()

            # Add talk turn to JSON output
            json_output["talk_turns"].append({
                "speaker": {
                    "id": speaker_id,
                    "role": ""
                },
                "input": dialogue
            })

    # Convert to JSON
    json_script = json.dumps(json_output, indent=2)
    return json_script

script_text = """

                                     VINCENT
                         Thanks a bunch.
                              (to Jules, who's 
                              nursing his coffee)
                         Want a sausage?

                                     JULES
                         Naw, I don't eat pork.


                                     VINCENT
                         Are you Jewish?

                                     JULES
                         I ain't Jewish man, I just don't dig 
                         on swine.

                                     VINCENT
                         Why not?

                                     JULES
                         They're filthy animals. I don't eat 
                         filthy animals.

                                     VINCENT
                         Sausages taste good. Pork chops taste 
                         good.

                                     JULES
                         A sewer rat may taste like pumpkin 
                         pie.  I'll never know 'cause even if 
                         it did, I wouldn't eat the filthy 
                         motherfucker. Pigs sleep and root in 
                         shit. That's a filthy animal. I don't 
                         wanna eat nothin' that ain't got 
                         enough sense to disregard its own 
                         feces.

                                     VINCENT
                         How about dogs? Dogs eat their own 
                         feces.

                                     JULES
                         I don't eat dog either.

                                     VINCENT
                         Yes, but do you consider a dog to be 
                         a filthy animal?

                                     JULES
                         I wouldn't go so far as to call a 
                         dog filthy, but they're definitely 
                         dirty. But a dog's got personality. 
                         And personality goes a long way.

                                     VINCENT
                         So by that rationale, if a pig had a 
                         better personality, he's cease to be 
                         a filthy animal?

                                     JULES
                         We'd have to be talkin' 'bout one 
                         motherfuckin' charmin' pig. It'd 
                         have to be the Cary Grant of pigs.

               The two men laugh.

                                     VINCENT
                         Good for you. Lighten up a little. 
                         You been sittin' there all quiet.

                                     JULES
                         I just been sittin' here thinkin'.

                                     VINCENT
                         About what?

                                     JULES
                         The miracle we witnessed.

                                     VINCENT
                         The miracle you witnessed. I witnessed 
                         a freak occurrence.

                                     JULES
                         Do you know that a miracle is?

                                     VINCENT
                         An act of God.

                                     JULES
                         What's an act of God?

                                     VINCENT
                         I guess it's when God makes the 
                         impossible possible. And I'm sorry 
                         Jules, but I don't think what happened 
                         this morning qualifies.

                                     JULES
                         Don't you see, Vince, that shit don't 
                         matter. You're judging this thing 
                         the wrong way. It's not about what. 
                         It could be God stopped the bullets, 
                         he changed Coke into Pepsi, he found 
                         my fuckin' car keys. You don't judge 
                         shit like this based on merit. Whether 
                         or not what we experienced was an 
                         according-to-Hoyle miracle is 
                         insignificant. What is significant 
                         is I felt God's touch, God got 
                         involved.

                                     VINCENT
                         But why?

                                     JULES
                         That's what's fuckin' wit' me! I 
                         don't know why. But I can't go back 
                         to sleep.

                                     VINCENT
                         So you're serious, you're really 
                         gonna quit?

                                     JULES
                         The life, most definitely.

                                     PATRON
                         Garcon! Coffee!


                                     VINCENT
                         So if you're quitting the life, 
                         what'll you do?

                                     JULES
                         That's what I've been sitting here 
                         contemplating. First, I'm gonna 
                         deliver this case to Marsellus. Then, 
                         basically, I'm gonna walk the earth.

                                     VINCENT
                         What do you mean, walk the earth?

                                     JULES
                         You know, like Caine in "KUNG FU." 
                         Just walk from town to town, meet 
                         people, get in adventures.

                                     VINCENT
                         How long do you intend to walk the 
                         earth?

                                     JULES
                         Until God puts me where he want me 
                         to be.

                                     VINCENT
                         What if he never does?

                                     JULES
                         If it takes forever, I'll wait 
                         forever.

                                     VINCENT
                         So you decided to be a bum?

                                     JULES
                         I'll just be Jules, Vincent – no 
                         more, no less.

                                     VINCENT
                         No Jules, you're gonna be like those 
                         pieces of shit out there who beg for 
                         change. They walk around like a bunch 
                         of fuckin' zombies, they sleep in 
                         garbage bins, they eat what I throw 
                         away, and dogs piss on 'em. They got 
                         a word for 'em, they're called bums. 
                         And without a job, residence, or 
                         legal tender, that's what you're 
                         gonna be – a fuckin' bum!

                                     JULES
                         Look my friend, this is just where 
                         me and you differ –

                                     VINCENT
                         – what happened was peculiar – no 
                         doubt about it – but it wasn't water 
                         into wine.

                                     JULES
                         All shapes and sizes, Vince.

                                     VINCENT
                         Stop fuckin' talkin' like that!

                                     JULES
                         If you find my answers frightening, 
                         Vincent, you should cease askin' 
                         scary questions.

                                     VINCENT
                         I gotta take a shit. To be continued.

                                     PUMPKIN
                         Everybody be cool, this is a robbery!

                                     YOLANDA
                         Any of you fuckin' pricks move and 
                         I'll execute every one of you 
                         motherfuckers!  Got that?!


                                     PUMPKIN
                         Customers stay seated, waitresses on 
                         the floor.

                                     YOLANDA
                         Now mean fuckin' now! Do it or die, 
                         do it or fucking die!


                                     PUMPKIN
                         You Mexicans in the kitchen, get out 
                         here!  Asta luego!


                                     PUMPKIN
                         On the floor or I'll cook you ass, 
                         comprende?


                                     MANAGER
                         I'm the manager here, there's no 
                         problem, no problem at all –


                                     PUMPKIN
                         You're gonna give me a problem?

                                     PUMPKIN
                         What? You said you're gonna give me 
                         a problem?

                                     MANAGER
                         No, I'm not. I'm not gonna give you 
                         any problem!

                                     PUMPKIN
                         I don't know, YOLANDA. He looks 
                         like the hero type to me!

                                     YOLANDA
                         Don't take any chances. Execute him!


                                     MANAGER
                         Please don't! I'm not a hero. I'm 
                         just a coffee shop manager. Take 
                         anything you want.

                                     PUMPKIN
                         Tell everyone to cooperate and it'll 
                         be all over.

                                     MANAGER
                         Everybody just be calm and cooperate 
                         with them and this will be all over 
                         soon!

                                     PUMPKIN
                         Well done, now git your fuckin' ass 
                         on the ground.


                                     PUMPKIN
                         Okay people, I'm going to go 'round 
                         and collect your wallets. Don't talk, 
                         just toss 'em in the bag. We clear?


                                     PUMPKIN
                         In the bag.

                                     PUMPKIN
                         What's in that?

                                     JULES
                         My boss' dirty laundry.

                                     PUMPKIN
                         You boss makes you do his laundry?

                                     JULES
                         When he wants it clean.

                                     PUMPKIN
                         Sounds like a shit job.

                                     JULES
                         Funny, I've been thinkin' the same 
                         thing.

                                     PUMPKIN
                         Open it up.

                                     JULES
                         'Fraid I can't do that.


                                     PUMPKIN
                         I didn't hear you.

                                     JULES
                         Yes, you did.


                                     YOLANDA
                         What's goin' on?

                                     PUMPKIN
                         Looks like we got a vigilante in our 
                         midst.

                                     YOLANDA
                         Shoot 'em in the face!

                                     JULES
                         I don't mean to shatter your ego, 
                         but this ain't the first time I've 
                         had gun pointed at me.

                                     PUMPKIN
                         You don't open up that case, it's 
                         gonna be the last.

                                     MANAGER
                              (on the ground)
                         Quit causing problems, you'll get us 
                         all killed! Give 'em what you got 
                         and get 'em out of here.

                                     JULES
                         Keep your fuckin' mouth closed, fat 
                         man, this ain't any of your goddamn 
                         business!

                                     PUMPKIN
                         I'm countin' to three, and if your 
                         hand ain't off that case, I'm gonna 
                         unload right in your fuckin' face. 
                         Clear? One...

                                     PUMPKIN
                         ...two... three.

                                     JULES
                         You win.

                                     JULES
                         It's all yours, Ringo.

                                     PUMPKIN
                         Open it.


                                     YOLANDA
                         What is it? What is it?

                                     PUMPKIN
                              (softly)
                         Is that what I think it is?

               Jules nods his head: "yes."

                                     PUMPKIN
                         It's beautiful.


                                     YOLANDA
                         Goddammit, what is it?



                                     YOLANDA
                         Let him go! Let him go! I'll blow 
                         your fuckin' head off! I'll kill ya! 
                         I'll kill ya! You're gonna die, you're 
                         gonna fuckin' die bad!

                                     JULES
                         Tell that bitch to be cool! Say, 
                         bitch be cool! Say, bitch be cool!

                                     PUMPKIN
                         Chill out, honey!

                                     YOLANDA
                         Let him go!

                                     JULES
                         Tell her it's gonna be okay.

                                     PUMPKIN
                         I'm gonna be okay.

                                     JULES
                         Promise her.

                                     PUMPKIN
                         I promise.

                                     JULES
                         Tell her to chill.

                                     PUMPKIN
                         Just chill out.

                                     JULES
                         What's her name?

                                     PUMPKIN
                         Yolanda.


                                     JULES
                         So, we cool Yolanda? We ain't gonna 
                         do anything stupid, are we?

                                     YOLANDA
                         Don't you hurt him.

                                     JULES
                         Nobody's gonna hurt anybody. We're 
                         gonna be like three Fonzies. And 
                         what' Fonzie like?

               No answer.

                                     JULES
                         C'mon Yolanda, what's Fonzie like?

                                     YOLANDA
                         He's cool?

                                     JULES
                         Correct-amundo! And that's what we're 
                         gonna be, we're gonna be cool.
                              (to Pumpkin)
                         Now Ringo, I'm gonna count to three 
                         and I want you to let go your gun 
                         and lay your palms flat on the table. 
                         But when you do it, do it cool. Ready?


                                     JULES
                         One... two... three.



                                     YOLANDA
                         Okay, now let him go!

                                     JULES
                         Yolanda, I thought you were gonna be 
                         cool.  When you yell at me, it makes 
                         me nervous.  When I get nervous, I 
                         get scared. And when motherfuckers 
                         get scared, that's when motherfuckers 
                         get accidentally shot.

                                     YOLANDA
                         Just know: you hurt him, you die.

                                     JULES
                         That seems to be the situation. Now 
                         I don't want that and you don't want 
                         that and Ringo here don't want that. 
                         So let's see what we can do.
                              (to Ringo)
                         Now this is the situation. Normally 
                         both of your asses would be dead as 
                         fuckin' fried chicken. But you 
                         happened to pull this shit while I'm 
                         in a transitional period. I don't 
                         wanna kill ya, I want to help ya. 
                         But I'm afraid I can't give you the 
                         case. It don't belong to me. Besides, 
                         I went through too much shit this 
                         morning on account of this case to 
                         just hand it over to your ass.

                                     VINCENT 
                         What the fuck's goin' on here?

     

                                     JULES
                         It's cool, Vincent! It's cool! Don't 
                         do a goddamn thing. Yolanda, it's 
                         cool baby, nothin's changed. We're 
                         still just talkin'.
                              (to Pumpkin)
                         Tell her we're still cool.

                                     PUMPKIN
                         It's cool, YOLANDA, we're still 
                         cool.

                                     VINCENT
                         What the hell's goin' on, Jules?

                                     JULES
                         Nothin' I can't handle. I want you 
                         to just hang back and don't do shit 
                         unless it's absolutely necessary.

                                     VINCENT
                         Check.

                                     JULES
                         Yolanda, how we doin, baby?

                                     YOLANDA
                         I gotta go pee! I want to go home.

                                     JULES
                         Just hang in there, baby, you're 
                         doing' great, Ringo's proud of you 
                         and so am I.  It's almost over.
                              (to Pumpkin)
                         Now I want you to go in that bag and 
                         find my wallet.

                                     PUMPKIN
                         Which one is it?

                                     JULES
                         It's the one that says Bad 
                         Motherfucker on it.


                                     JULES
                         That's my bad motherfucker. Now open 
                         it up and take out the cash. How 
                         much is there?

                                     PUMPKIN
                         About fifteen hundred dollars.

                                     JULES
                         Put it in your pocket, it's yours. 
                         Now with the rest of them wallets 
                         and the register, that makes this a 
                         pretty successful little score.

                                     VINCENT
                         Jules, if you give this nimrod fifteen 
                         hundred buck, I'm gonna shoot 'em on 
                         general principle.

                                     JULES
                         You ain't gonna do a goddamn thing, 
                         now hang back and shut the fuck up. 
                         Besides, I ain't givin' it to him. 
                         I'm buyin' somethin' for my money. 
                         Wanna know what I'm buyin' Ringo?

                                     PUMPKIN
                         What?

                                     JULES
                         Your life. I'm givin' you that money 
                         so I don't hafta kill your ass. You 
                         read the Bible?

                                     PUMPKIN
                         Not regularly.

                                     JULES
                         There's a passage I got memorized. 
                         Ezekiel 25:17. "The path of the 
                         righteous man is beset on all sides 
                         by the inequities of the selfish and 
                         the tyranny of evil men.  Blessed is 
                         he who, in the name of charity and 
                         good will, shepherds the weak through 
                         the valley of the darkness. For he 
                         is truly his brother's keeper and 
                         the finder of lost children. And I 
                         will strike down upon thee with great 
                         vengeance and furious anger those 
                         who attempt to poison and destroy my 
                         brothers. And you will know I am the 
                         Lord when I lay my vengeance upon 
                         you." I been sayin' that shit for 
                         years.  And if you ever heard it, it 
                         meant your ass. I never really 
                         questioned what it meant. I thought 
                         it was just a coldblooded thing to 
                         say to a motherfucker 'fore you popped 
                         a cap in his ass. But I saw some 
                         shit this mornin' made me think twice. 
                         Now I'm thinkin', it could mean you're 
                         the evil man. And I'm the righteous 
                         man.  And Mr. .45 here, he's the 
                         shepherd protecting my righteous ass 
                         in the valley of darkness. Or is 
                         could by you're the righteous man 
                         and I'm the shepherd and it's the 
                         world that's evil and selfish.  I'd 
                         like that. But that shit ain't the 
                         truth. The truth is you're the weak. 
                         And I'm the tyranny of evil men. But 
                         I'm tryin'. I'm tryin' real hard to 
                         be a shepherd.

"""
# Convert the script to JSON
json_script = convert_to_json(script_text)

# Print the JSON output
print(json_script)