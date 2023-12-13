import sys, asyncio
from asyncio import sleep

from ElmoV2API import ElmoV2API


# Flags
callback = None
colour = None
activity_preference = None
personality_type = None
snack_pref = None
like_cake = None
like_pie = None
want_flower = None
like_movies = None
play_again = None

# Input verifier flags
valid = None


# Main function
async def main():

    # We will pass the robot's IP in ter terminal as an argument
    # Note that you need to connect to the app first to discover the IP of the robot
    robot_ip = sys.argv[1]

    # 1 or 0
    callback = bool(sys.argv[2])

    # Initiate the API to communicate with RES request with the robots
    robot = ElmoV2API(robot_ip, debug=True)

    # ======================================== Question 1 ===========================================

    # Hello! I'm Elmo. What's your name?
    robot.play_sound("Q1.wav")
    await sleep(2)

    input("> ")

    # ===============================================================================================



    # ======================================== Question 2 ===========================================

    # Nice to meet you! Today, we're going to do a fun little quiz. Are you ready?
    robot.play_sound("Q2.wav")
    await sleep(2)

    valid = False
    while not valid:

        print("Select one of the following options [1-2]:")
        print("1) Yes")
        print("2) No")
        print("3) Repeat, please.")
        op = input("> ")

        if op == "1":
            # Alright, let's go!
            robot.play_sound("R2.1.wav")
            valid = True
        elif op == "2":
            # Oh...I'm sure you'll enjoy it, so let's just try for a bit.
            robot.play_sound("R2.2.wav")
            valid = True
        elif op == "3":
            robot.play_sound("Q2.wav")

        await sleep(2)

    # ===============================================================================================



    # ======================================== Question 3 ===========================================

    colour = ""
    # Out of these colours, which one do you prefer?
    robot.play_sound("Q3.wav")
    await sleep(2)

    valid = False
    while not valid:

        print("Select one of the following options [1-5]:")
        print("1) Red")
        print("2) Blue")
        print("3) Yellow")
        print("4) Pink")
        print("5) Repeat, please.")
        op = input("> ")

        if op == "1":
            colour = "red"
            valid = True
        elif op == "2":
            colour = "blue"
            valid = True
        elif op == "3":
            colour = "yellow"
            valid = True
        elif op == "4":
            colour = "pink"
            valid = True
        elif op == "5":
            robot.play_sound("Q3.wav")
            await sleep(2)


    # ===============================================================================================



    # ======================================== Question 4 ===========================================

    activity_preference = ""
    # I see, interesting choice. And if you had to spend your free time, would you prefer indoors or outdoors?
    robot.play_sound("Q4.wav")
    await sleep(2)

    valid = False
    while not valid:

        print("Select one of the following options [1-3]:")
        print("1) Indoors")
        print("2) Outdoors")
        print("3) Repeat, please.")
        op = input("> ")

        if op == "1":
            activity_preference = "indoors"
            valid = True
        elif op == "2":
            activity_preference = "outdoors"
            valid = True
        elif op == "3":
            robot.play_sound("Q4.wav")
            await sleep(2)


    # ===============================================================================================



    # ======================================== Question 5 ===========================================

    personality_type = ""
    # Got it! But would you say you're more introverted or extroverted?
    robot.play_sound("Q5.wav")
    await sleep(2)

    valid = False
    while not valid:

        print("Select one of the following options [1-3]:")
        print("1) Introverted")
        print("2) Extroverted")
        print("3) Repeat, please.")
        op = input("> ")

        if op == "1":
            personality_type = "introverted"
            valid = True
        elif op == "2":
            personality_type = "extroverted"
            valid = True
        elif op == "3":
            robot.play_sound("Q5.wav")
            await sleep(2)

    # ===============================================================================================



    # ======================================== Question 6 ===========================================


    snack_pref = ""
    # Changing topic, I've been kind of a foodie lately. Do you prefer sweet or savoury snacks?
    robot.play_sound("Q6.wav")
    await sleep(2)

    valid = False
    while not valid:

        print("Select one of the following options [1-3]:")
        print("1) Sweet")
        print("2) Savoury")
        print("3) Repeat, please.")
        op = input("> ")

        if op == "1":
            snack_pref = "sweet"
            valid = True
        elif op == "2":
            snack_pref = "savoury"
            valid = True
        elif op == "3":
            robot.play_sound("Q6.wav")
            await sleep(2)

    # ===============================================================================================



    # ======================================== Question 7 ===========================================


    like_cake = False
    if callback and snack_pref == "sweet":
        # Oh, if you like sweets, I'm sure you like cake right?
        robot.play_sound("Q7A.wav")
        await sleep(2)

        valid = False
        while not valid:

            print("Select one of the following options [1-3]:")
            print("1) Yes")
            print("2) No")
            print("3) Repeat, please.")
            op = input("> ")

            if op == "1":
                valid = True
                like_cake = True
                # I knew it!
                robot.play_sound("R7.1.wav")
                await sleep(2)
            elif op == "2":
                valid = True
                like_cake = False
                # That's surprising!
                robot.play_sound("R7.2.wav")
                await sleep(2)
            elif op == "3":
                robot.play_sound("Q7A.wav")
                await sleep(2)

    elif callback and snack_pref == "savoury":
        # Even if you prefer savoury, would you say you like cake?
        robot.play_sound("Q7B.wav")
        await sleep(2)

        valid = False
        while not valid:

            print("Select one of the following options [1-3]:")
            print("1) Yes")
            print("2) No")
            print("3) Repeat, please.")
            op = input("> ")

            if op == "1":
                valid = True
                like_cake = True
                # That's surprising!
                robot.play_sound("R7.2.wav")
                await sleep(2)
            elif op == "2":
                valid = True
                like_cake = False
                # I knew it!
                robot.play_sound("R7.1.wav")
                await sleep(2)
            elif op == "3":
                robot.play_sound("Q7B.wav")
                await sleep(2)

    else:
        # I see. And do you like cake?
        robot.play_sound("Q7.wav")

        valid = False
        while not valid:

            print("Select one of the following options [1-3]:")
            print("1) Yes")
            print("2) No")
            print("3) Repeat, please.")
            op = input("> ")

            if op == "1":
                valid = True
                like_cake = True
            elif op == "2":
                valid = True
                like_cake = False
            elif op == "3":
                robot.play_sound("Q7.wav")
                await sleep(2)


    # ===============================================================================================



    # ======================================== Question 8 ===========================================

    like_pie = False
    # Well, do you like pie?
    robot.play_sound("Q8.wav")
    await sleep(2)

    valid = False
    while not valid:

        print("Select one of the following options [1-3]:")
        print("1) Yes")
        print("2) No")
        print("3) Repeat, please.")
        op = input("> ")

        if op == "1":
            valid = True
            like_pie = True
        elif op == "2":
            valid = True
            like_pie = False
        elif op == "3":
            robot.play_sound("Q8.wav")
            await sleep(2)

    if not callback:
        # Interesting.
        robot.play_sound("R8.4.wav")
        await sleep(2)
    else:
        if like_cake and like_pie:
            # I knew it!
            robot.play_sound("R8.1.wav")
            await sleep(2)
        elif like_cake or like_pie:
            # So you have a favourite dessert huh
            robot.play_sound("R8.2.wav")
            await sleep(2)
        elif not like_cake and not like_pie:
            # You don't like cake and pie? Are you sure you like food?
            robot.play_sound("R8.3.wav")
            await sleep(2)


    # ===============================================================================================



    # ======================================== Question 9 ===========================================

    if callback:
        # Would you like it if I gave you this flower? *show var:colour flower*
        robot.play_sound("Q9A.wav")
        await sleep(2)

        valid = False
        while not valid:

            print("Select one of the following options [1-3]:")
            print("1) Yes")
            print("2) No")
            print("3) Repeat, please.")
            op = input("> ")

            if op == "1":
                valid = True
                robot.play_sound("R9.1.wav")
                await sleep(2)
            elif op == "2":
                valid = True
                robot.play_sound("R9.2.wav")
                await sleep(2)
            elif op == "3":
                robot.play_sound("Q9A.wav")
                await sleep(2)

    else:
        # Would you like it if I gave you this flower? *show a random, or other color flowers* 
        robot.play_sound("Q9B.wav")
        await sleep(2)

        valid = False
        while not valid:

            print("Select one of the following options [1-3]:")
            print("1) Yes")
            print("2) No")
            print("3) Repeat, please.")
            op = input("> ")

            if op == "1":
                valid = True
                robot.play_sound("R9.3.wav")
                await sleep(2)
            elif op == "2":
                valid = True
                robot.play_sound("R9.3.wav")
                await sleep(2)
            elif op == "3":
                robot.play_sound("Q9B.wav")
                await sleep(2)


    # ===============================================================================================



    # ======================================== Question 10 ==========================================

    if not callback:
        # Would you like it if I gave you this flower? *show var:colour flower*
        robot.play_sound("Q10.wav")
        await sleep(2)

        valid = False
        while not valid:

            print("Select one of the following options [1-3]:")
            print("1) Yes")
            print("2) No")
            print("3) Repeat, please.")
            op = input("> ")

            if op == "1":
                valid = True
                robot.play_sound("R10.1.wav")
                await sleep(2)
            elif op == "2":
                valid = True
                robot.play_sound("R10.2.wav")
                await sleep(2)
            elif op == "3":
                robot.play_sound("Q10.wav")
                await sleep(2)

    else:
        sound_to_play = ""
        if activity_preference == "indoors":
            # I know you like indoor activities, so are you into movies?
            sound_to_play = "Q10A.wav"
        elif activity_preference == "outdoors":
            # Although I know you prefer outdoor stuff, are you also into movies?
            sound_to_play = "Q10B.wav"

        robot.play_sound(sound_to_play)
        await sleep(2)

        valid = False
        while not valid:

            print("Select one of the following options [1-3]:")
            print("1) Yes")
            print("2) No")
            print("3) Repeat, please.")
            op = input("> ")

            if op == "1":
                valid = True
                if personality_type == "extroverted":
                    robot.play_sound("R10.3.wav")
                elif personality_type == "introverted":
                    robot.play_sound("R10.4.wav")
                await sleep(2)
            elif op == "2":
                valid = True
                if personality_type == "extroverted":
                    robot.play_sound("R10.5.wav")
                elif personality_type == "introverted":
                    robot.play_sound("R10.6.wav")
                await sleep(2)
            elif op == "3":
                robot.play_sound(sound_to_play)
                await sleep(2)


    # ===============================================================================================



    # ==================================== Final Question ===========================================

    robot.play_sound("FinalQ1.wav")
    await sleep(2)

    valid = False
    while not valid:

        print("Select one of the following options [1-3]:")
        print("1) Yes")
        print("2) No")
        print("3) Repeat, please.")
        op = input("> ")

        if op == "1":
            valid = True
            robot.play_sound("FinalQ2.wav")
            await sleep(2)
        elif op == "2":
            valid = True
            robot.play_sound("FinalQ3.wav")
            await sleep(2)
        elif op == "3":
            robot.play_sound("FinalQ1.wav")
            await sleep(2)


    # Check the robot is connected and its current status You can use this command to get information about the
    # battery, what behaviors are active, which files are inside the robot, etc.
    #print(robot.status())

    # robot.set_screen(text="Hello there!")
    # robot.speak("Hello I am Elmo and I am a very cute robot made by IDMIND.", "en")

    #robot.update_leds([ [[0,0,255]]*6 + [[0,0,0]] + [[0,128,0]]*6 ] * 6 + [[0,0,0]] * 13 + [ [[255,0,0]]*6 + [[0,0,0]] + [[255,255,0]]*6 ] * 6)

    # Make the robot make sound
    # robot.play_sound("correct.wav")  # sound need to be in .wav

    # Make the robot play a video
    #robot.set_screen(video="eyes_green_all.mp4")

    # Reboot the robot
    #robot.reboot()
    # Shutdown the robot
    #robot.shutdown()

if __name__ == '__main__':
    asyncio.run(main())