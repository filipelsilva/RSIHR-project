echo "Sending audio files to ELMO..."
address="192.168.0.$1"
scp audio/*.mp3 idmind@"$address":elmo-v2/src/static/sounds

python3 elmo_test.py "$address"
