# SRHRI Project

How to run this project:

1. Get the ELMO's IP address
2. Navigate to the `src` folder
3. Run `./send.sh <last 3 digits of the IP address>` to send the audio files and
images to the ELMO
4. Send the file `behaviour_look_around.py` to the ELMO, updating the original
file with the same name
5. Reboot the ELMO so that the changes in step 4 are applied
6. Run `python3 game.py <IP address> <callbaks enabled (1) or disabled (0)>`
