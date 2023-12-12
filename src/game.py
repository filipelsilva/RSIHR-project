import sys, time, asyncio
from asyncio import sleep

from ElmoV2API import ElmoV2API


# Flags
callback = None
user_ready = None
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
    callback = sys.argv[2]

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
            user_ready = "yes"
            # Alright, let's go!
            robot.play_sound("R2.1.wav")
            valid = True
        elif op == "2":
            user_ready = "no"
            # Oh...I'm sure you'll enjoy it, so let's just try for a bit.
            robot.play_sound("R2.2.wav")
            valid = True
        elif op == "3":
            robot.play_sound("Q2.wav")

        await sleep(2)

    # ===============================================================================================



    # ======================================== Question 3 ===========================================

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
            activity_preference = "extroverted"
            valid = True
        elif op == "3":
            robot.play_sound("Q5.wav")
            await sleep(2)

    # ===============================================================================================



    # ======================================== Question 6 ===========================================


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